# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:29:47 2020

@author: Jeffrey Folz
"""

##################################
#First draft of arkham databse. Will hold information on characters, monsters, items, and cards

#06132020: Monsers table added with function to retrieve random monster information, which is returned as a tuple.

##################################

import sqlite3
import random

con = sqlite3.connect('arkham.db')
c = con.cursor()


c.execute('DROP TABLE monsters') #drops monsters table; useful in debugging
c.execute('DROP TABLE prac')

c.execute('''CREATE TABLE monsters
(id int PRIMARY KEY,
name TEXT,
color text,
symbol text,
sneak_mod int,
horror_mod int,
combat_mod int,
horror_dmg int,
combat_dmg int,
toughness int
endless int,
undead int,
ambush int,
mag_res int,
phys_res int,
mag_imm int,
phys_imm int,
weapon_imm int,
overwhelming int,
nightmarish int,
elusive int
)''')

c.execute("INSERT INTO monsters VALUES (1,'Byakhee','Blue','circle',-2,-1,0,1,2,1,0,0,0,0,0,0,0,0,0,0)")
c.execute("INSERT INTO monsters VALUES (2,'Zombie','Black','moon', 1,-1,-1,1,2,1,0,1,0,0,0,0,0,0,0,0)")
c.execute("INSERT INTO monsters VALUES (3,'Ghoul','Black','hexagon',-3,0,-1,1,1,1,0,0,1,0,0,0,0,0,0,0)")

con.commit()

c.execute('''CREATE TABLE prac
(id int PRIMARY KEY,
name text,
color text)''')


c.execute("INSERT INTO prac VALUES (1,'First','b')")
c.execute("INSERT INTO prac VALUES (2,'2nd','r')")
c.execute("INSERT INTO prac VALUES (3,'third','r')")
con.commit()

con.close()




#Defition of monster class that accesses arkham.db to populate monster stats.
class monster:
    def __init__(self, name='NULL'):
            conn = sqlite3.connect('arkham.db')
            cursor = conn.cursor()
            if name == 'NULL':
                cursor.execute('SELECT MAX(id) FROM monsters')
                mons = (random.randint(1,cursor.fetchone()[0]),)
                cursor.execute('SELECT * FROM monsters WHERE id = ?', mons)
            else:
                t =(name,)
                mons = cursor.execute('Select * FROM monsters WHERE name = ?', t)
            spawn = cursor.fetchone()
            conn.close()
            self.name = spawn[1]
            self.color = spawn[2]
            self.symbol = spawn[3]
            self.sneak_md = spawn[4]
            self.horror_mod = spawn[5]
            self.combat_mod = spawn[6]
            self.horror_dmg = spawn[7]
            self.combat_dmg = spawn[8]
            self.toughness = spawn[9]
            
            
# use monster() to generate a random monster

             
 #use monster('name') to generate a specific mosnter
 
#Example:

    


zombie = monster('Zombie')
print(zombie.name)
print("Zombie's have a toughness of %i" % zombie.toughness)