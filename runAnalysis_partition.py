import glob
import sqlite3
from sqlite3 import Error
import numpy as np
from numpy.linalg import norm
import collections as clctns
import re
import matplotlib.pyplot as plt
import os

def reformatColors(clrs):
    newClrs = []
    for clr in clrs:
        findDelim = [m.start() for m in re.finditer(', ', clr)]
        if not findDelim:
            newClrs.append(clr)
        else:
            for ii in findDelim:
                newClrs.append(clr[ii-1])
                
            newClrs.append(clr[ii+len(', ')])
                
    return np.unique(newClrs)
        

### SQLite3 Queries
sqlt_create_decklists_table = """ CREATE TABLE IF NOT EXISTS decks (                                    
                                    name text NOT NULL,
                                    quantity integer NOT NULL,
                                    deckNum integer
                                    );"""

sqlt_create_network_table = """ CREATE TABLE IF NOT EXISTS networkData (                                  
                                    deckNum integer NOT NULL,
                                    cardID integer NOT NULL,
                                    oldID integer NOT NULL,
                                    quantity integer NOT NULL,
                                    type text,
                                    convertedManaCost float,
                                    colors text,
                                    textData text);"""

sqlt_insertData_fromFile = """ INSERT INTO decks (name, quantity, deckNum) VALUES (?, ?, ?)""";
                                    
sqlt_insertData_networkData = """INSERT INTO networkData (deckNum, cardID, oldID, quantity, type, convertedManaCost, colors, textData) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""";

sqlt_getFullCardInformation = """WITH cards_sorted AS
(   SELECT *, ROW_NUMBER() OVER (PARTITION BY name) AS rn
    FROM cards

) 
SELECT DISTINCT deckNum, cards_sorted.id, quantity, type, cards_sorted.name, convertedManaCost, colors, text   
FROM cards_sorted 
INNER JOIN decks ON decks.name = cards_sorted.name
WHERE rn = 1;""";

sqlt_getNetData = """SELECT deckNum, cardID, quantity FROM networkData""";

### SQLite Query Builder

def whereBinding(data_to_feed):
    strVal = "(" + len(data_to_feed)*"%d, ";
    strVal = strVal[:-2] + ")";
    strVal = strVal%tuple(data_to_feed)

    return strVal    


### File Names

baseDir = r"C:\Users\Quinton\Documents\Classes\ComplexSystems_501\project\Decklists\Standard\2015-2016";

direcList = []

for subdir, dirs, files in os.walk(baseDir):
    direcList.append(subdir)

MTG_DB_local = r"C:\Users\Quinton\Documents\Classes\ComplexSystems_501\project\rawData\AllPrintings.sqlite";
deckLists = glob.glob(r"C:\Users\Quinton\Documents\Classes\ComplexSystems_501\project\Decklists\Standard\2015-2016\GP-SanDiego\*.txt");
matFile = r"C:\Users\Quinton\Documents\Classes\ComplexSystems_501\project\Decklists\Standard\2015-2016\GP-SanDiego\adjMat_2-tite.dat";
idFile = r"C:\Users\Quinton\Documents\Classes\ComplexSystems_501\project\Decklists\Standard\2015-2016\GP-SanDiego\nodeTypes_2-tite.dat";
partitionFile = r"C:\Users\Quinton\Documents\Classes\ComplexSystems_501\project\Decklists\Standard\2015-2016\GP-SanDiego\partitionVector.dat";

### Establish SQLite3 connection, query O.G. data, create tables

conn = sqlite3.connect(MTG_DB_local);
db_cursor = conn.cursor();

db_cursor.execute("""DROP TABLE IF EXISTS decks""")
db_cursor.execute("""DROP TABLE IF EXISTS networkData""")

db_cursor.execute(sqlt_create_decklists_table)
db_cursor.execute(sqlt_create_network_table)

### Upload decklists to database

count = -1;
for deck in deckLists:
    
    f = open(deck,'r');
    cardData = f.readlines();
    
    count = count + 1;
    
    for card in cardData:
        find_delimiter = card.find(' ');
        
        if(find_delimiter < 0):
            continue
        
        db_cursor.execute(sqlt_insertData_fromFile, (card[(find_delimiter+1):-1], int(card[0:find_delimiter]), count))
    #thisDeck = np.genfromtxt(deck, delimiter=", ", dtype='str')
    
### Query data from (existing) cards table using (created) decks table

netData = db_cursor.execute(sqlt_getFullCardInformation)
netData = netData.fetchall();

#Finds the unique number of cards in the decks table
unqCardIDs, unqIndices = np.unique([cardIDs[1] for cardIDs in netData], return_inverse=True);
new_unqCardIDs = list(range(len(unqCardIDs)));

matSize = len(deckLists) + len(new_unqCardIDs);
kPart_adjMat = np.zeros([matSize, matSize]);

#Upload relevant network data into the networkData table
ind = 0;
for card in netData:
    db_cursor.execute(sqlt_insertData_networkData, (card[0], new_unqCardIDs[unqIndices[ind]], card[1], card[2], card[3], card[5], card[6], card[7]))
    
    kPart_adjMat[card[0]][new_unqCardIDs[unqIndices[ind]]+len(deckLists)] = 1;#card[2];
    kPart_adjMat[new_unqCardIDs[unqIndices[ind]]+len(deckLists)][card[0]] = 1;#card[2];
    
    ind = ind + 1;

kPart_adjMat = np.matrix(kPart_adjMat);
with open(matFile, 'wb') as f:
    for line in kPart_adjMat:
        np.savetxt(f, line, fmt="%d")
        
skipList = np.zeros([len(deckLists), 2]);
cosCount = 0;
maxCount = 0;
        
for ind in range(len(deckLists)):
    
    deck_i = kPart_adjMat[len(deckLists):, ind]
    if(np.count_nonzero(deck_i) > maxCount):
        maxCount = np.count_nonzero(deck_i)
    
    for jnd in range(ind+1, len(deckLists)):

        if(skipList.__contains__(ind)):
            continue
        
        deck_j = kPart_adjMat[len(deckLists):, jnd]
        
        sumTotl = 0;
        
        for kk in range(len(deck_i)):
            sumTotl = sumTotl + deck_i[kk]*deck_j[kk]
        
        cos_ij = sumTotl/(norm(deck_i)*norm(deck_j))
        
        if(cos_ij >= 0.75):
            skipList[cosCount,:] = [ind, jnd]
            cosCount = cosCount + 1
 
skipList = skipList[0:cosCount-1,:]       
        
node_types = np.zeros([matSize, 1], dtype=int);

for ind in range(matSize):
    if ind < len(deckLists):
        node_types[ind] = 1
    else:
        node_types[ind] = 2

node_types = np.matrix(node_types)
 
f = open(partitionFile,'r');
gID = f.readlines();
partID = np.zeros([matSize, 1]);
count = -1
for g_i in gID:
    count = count + 1
    partID[count] = int(g_i)
    
cardIDs_fromPart = partID[len(deckLists):]
unqPartIDs = np.unique(cardIDs_fromPart)

clusterSize = np.zeros([len(unqPartIDs), 1])
numDecks_given_clusterSize = np.zeros([len(unqPartIDs), 1])
numDecks_gCS_dist = []
textSize = []
CMC = []
unqColors = []

ind = 0
for unqID in unqPartIDs:
    findGroup = np.where(cardIDs_fromPart == unqID)[0]
    
    getCardData = """SELECT DISTINCT * FROM networkData WHERE cardID IN """ + whereBinding(findGroup);
    cards_in_cluster = db_cursor.execute(getCardData).fetchall()
    
    clusterSize[ind] = len(findGroup)
    
    decks_in_cluster = [x[0] for x in cards_in_cluster]
    unqDecks_c = np.unique(decks_in_cluster)
    
    get_unqCards_in_cluster = """WITH unqCards AS
        (   SELECT *, ROW_NUMBER() OVER (PARTITION BY cardID) AS rn
             FROM networkData

        ) 
        SELECT DISTINCT deckNum, cardID, type, convertedManaCost, colors, textData   
        FROM unqCards 
        WHERE cardID IN """ + whereBinding(findGroup) + " AND rn = 1;";
        
    unqCards_in_cluster = db_cursor.execute(get_unqCards_in_cluster).fetchall()
    
    numDecks_given_clusterSize[ind] = len(unqDecks_c)
    numDecks_gCS_dist.append(clctns.Counter([x[0] for x in cards_in_cluster]))
    CMC.append([x[3] for x in unqCards_in_cluster])
    textSize.append([len(x[-1]) for x in unqCards_in_cluster])
    colors_i = [x[-2] for x in unqCards_in_cluster if x[-2] != None]
    
    unqColors.append(reformatColors(colors_i))
    
    ind = ind + 1   
    #textSize.append([x[-1] for x in cards_in_cluster])
    #unqCard_atrbts = cards_in_cluster[np.unique([x[1] for x in cards_in_cluster])[2]]
 
plt.scatter(clusterSize, numDecks_given_clusterSize)

plt.figure()
for ind in range(len(CMC)):
    plt.scatter(CMC[ind], textSize[ind])

    
    
    
    
#test = test.fetchall();

#test2 = [description[0] for description in db_cursor.description];

### Close SQLite connections

#db_cursor.execute("""DROP TABLE decks""")
#db_cursor.execute("""DROP TABLE networkData""")

#db_cursor.close()
#conn.close()
