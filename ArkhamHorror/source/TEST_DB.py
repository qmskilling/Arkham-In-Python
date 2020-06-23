#@ Author: Quinton Skilling

"""
This is a test code to set up a SQLite class.

The class will handle all SQLite queires, creations, etc.

It will be callable from external scripts.
"""

import sqlite3
import sys

class DB_():
    def __init__(self, db_name):
        super().__init__()

        con = sqlite3.connect(db_name)

        self.cur = con.cursor()

        self.cur.execute('''CREATE TABLE IF NOT EXISTS monsters_new
            (id int PRIMARY KEY,
            name TEXT,
            movement text,
            symbol text,
            sneak int,
            horror_mod int,
            combat_mod int,
            horror_dmg int,
            combat_dmg int,
            toughness int,
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
            elusive int,
            special text,
            expansion text
            )''')
    
        

    def submitData(self, formData):
            subVec  = ['name','movement','symbol','sneak','horror_mod','combat_mod','horror_dmg',\
            'combat_dmg','toughness','endless','undead','ambush','mag_res','phys_res','mag_imm',\
            'phys_imm','weapon_imm','overwhelming','nightmarish','elusive','special','expansion']



#dataBase = DB_('arkham.db')




