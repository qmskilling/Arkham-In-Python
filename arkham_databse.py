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


c.execute('DROP TABLE monsters') #drops monsters table; useful in debugging comment/uncomment as needed
c.execute('DROP TABLE characters') #drops monsters table; useful in debugging comment/uncomment as needed
c.execute('DROP TABLE items') #drops monsters table; useful in debugging comment/uncomment as needed

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



######## INCOMPLETE #######
######## INCOMPLETE #######
#Impletment:items, abilities,#
######## INCOMPLETE #######
######## INCOMPLETE #######

c.execute('''CREATE TABLE characters
(id int PRIMARY KEY,
name text,
title text,
home text,
money int,
clue_tokens int,
focus int,
max_speed int,
max_sneak int,
max_fight int,
max_will int,
max_lore int,
max_luck int,
max_sanity int,
max_stamina int
)''')


c.execute("INSERT INTO characters VALUES (1, 'Carolyn Fern', 'the Psychologist', 'Arkham Asylum',7,1,2,3,3,4,4,5,5,6,4)")
c.execute('INSERT INTO characters VALUES (2, "Michael McGlen", "the Gangster", "Ma\'s Boarding House",8,0,1,5,4,6,4,3,3,3,7)')
c.execute("INSERT INTO characters VALUES (3, 'Sister Mary', 'the Nun', 'South Church',0,0,1,4,4,3,4,4,6,7,3)")

con.commit()


c.execute('''CREATE TABLE items
(id int PRIMARY KEY,
name text,
type text,
is_weapon int,
combat_bonus int,
is_tome int,
discard_on_use int
)''')


c.execute("INSERT INTO items VALUES (1, 'Holy Water', 'unique', 1,6,0,1)")
c.execute('INSERT INTO items VALUES (2, "Dynamite", "common", 1,8,0,1)')
c.execute("INSERT INTO items VALUES (3, 'Tommy Gun', 'common', 1,6,0,0)")

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




class character:
    def __init__(self, name='NULL'):
            conn = sqlite3.connect('arkham.db')
            cursor = conn.cursor()
            if name == 'NULL':
                cursor.execute('SELECT MAX(id) FROM characters')
                mons = (random.randint(1,cursor.fetchone()[0]),)
                cursor.execute('SELECT * FROM characters WHERE id = ?', mons)
            else:
                t =(name,)
                mons = cursor.execute('Select * FROM characters WHERE name = ?', t)
            spawn = cursor.fetchone()
            conn.close()
            self.name = spawn[1]
            self.title = spawn[2]
            self.home = spawn[3]
            self.money = spawn[4]
            self.clue_tokens = spawn[5]
            self.focus = spawn[6]
            self.max_speed = spawn[7]
            self.max_sneak = spawn[8]
            self.max_fight = spawn[9]
            self.max_will = spawn[10]
            self.max_lore = spawn[7]
            self.max_luck = spawn[8]
            self.max_sanity = spawn[9]
            self.max_stamina = spawn[10]
    


player1 = character('Sister Mary')
print(player1.name)
print(player1.title)


rando_character = character()
print(rando_character.name)
print(rando_character.title)
print(rando_character.home)



class item:
    def __init__(self, name='NULL'):
        conn = sqlite3.connect('arkham.db')
        cursor = conn.cursor()
        if name == 'NULL':
            cursor.execute('SELECT MAX(id) FROM items')
            mons = (random.randint(1,cursor.fetchone()[0]),)
            cursor.execute('SELECT * FROM items WHERE id = ?', mons)
        else:
            t =(name,)
            mons = cursor.execute('Select * FROM items WHERE name = ?', t)
        spawn = cursor.fetchone()
        conn.close()
        self.name =spawn[1]
        self.type =spawn[2]
        self.is_weapon = spawn[3]
        
        
            
        
item1 = item()
print(item1.name)
print(item1.type)

print(item1.is_weapon)


class inventory:
    def __init__(self, character):
        self.character = character.name
        self.contents = []
        self.size = len(self.contents)
    
    def add_item(self, item):
        self.contents.append(item.name)
    
    def display(self):
        if self.contents == []:
            print(self.character, " has no items.")
        for i in self.contents:
            print(i)
            
    def remove_item(self, item):
        self.contents.remove(item.name)
    
    
        
    
        


inventory1 = inventory(player1)
                  
inventory1.display()

inventory1.add_item(item1)
inventory1.add_item(item1)
inventory1.add_item(item1)


inventory1.display()
    
    
    
    
    
    
    
            