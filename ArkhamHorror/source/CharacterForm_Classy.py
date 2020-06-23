from PyQt5 import QtWidgets,QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import TEST_DB, Locations, ArkPossessions
import sys


class CF_Window(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.filePath = "/home/q/Documents/ArkhamHorror/Images/"#Change this line to local directory. Note: you may need to change direction of slashes.
        self.windowTitle = "New Character Data"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 400
        self.iconName = self.filePath + "/GUI/ES_icon2.png"
        self.initWindow()
    
    def initWindow(self):

        """
        Window instantiation. Holds all feature creation (buttons, boxes, etc.)        
        """

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.windowTitle)

        self.main_vBox = QtWidgets.QVBoxLayout()

        self.DB_connection()
        self.main_vBox.addWidget(self.db_groupBox)

        self.charBox = QtWidgets.QGroupBox("Character")
        self.char_vBox = QtWidgets.QGridLayout()

        self.name = QtWidgets.QLineEdit()
        self.name.setPlaceholderText("Character Name")
        self.char_vBox.addWidget(self.name,0,0,1,2)

        self.title = QtWidgets.QLineEdit()
        self.title.setPlaceholderText("Character Title")
        self.char_vBox.addWidget(self.title, 0, 2, 1, 2)

        self.expansionSet()
        self.comboBox_expansion.currentIndexChanged.connect(self.expansionChosen)
        self.char_vBox.addWidget(self.comboBox_expansion,1,0)

        self.incStreets = QtWidgets.QCheckBox("Include Streets")
        self.incStreets.setEnabled(False)
        self.incStreets.clicked.connect(self.includeStreets)
        self.char_vBox.addWidget(self.incStreets,1,1)

        self.incOW = QtWidgets.QCheckBox("Include Other Worlds")
        self.incOW.setEnabled(False)
        self.incOW.clicked.connect(self.includeOW)
        self.char_vBox.addWidget(self.incOW,1,2)

        self.isCustom = QtWidgets.QCheckBox("Custom")
        self.isCustom.setEnabled(False)
        self.char_vBox.addWidget(self.isCustom,1,3)

        self.charBox.setLayout(self.char_vBox)

        locLabel = QtWidgets.QLabel("Home Location:")
        self.char_vBox.addWidget(locLabel, 2, 0)

        self.locationClass = Locations.Locations()
        self.homeLocation()
        self.char_vBox.addWidget(self.comboBox_locations,3,0,1,4)

        self.main_vBox.addWidget(self.charBox)

        #
        self.charAttributes()
        self.main_vBox.addWidget(self.attrbBox)

        self.possessions()
        self.posClass = ArkPossessions.possessions()

        self.fp_IType1.currentIndexChanged.connect(self.set_IL1)
        self.fp_IType2.currentIndexChanged.connect(self.set_IL2)
        self.fp_IType3.currentIndexChanged.connect(self.set_IL3)
        self.main_vBox.addWidget(self.fPosBox)

        self.submitButton = QtWidgets.QPushButton("Submit Character")
        self.submitButton.clicked.connect(self.submitCharacter)
        self.main_vBox.addWidget(self.submitButton)

        self.setLayout(self.main_vBox)
        self.show()

    def DB_connection(self):
        self.db_groupBox = QtWidgets.QGroupBox('Database Connection')
        self.db_vBox = QtWidgets.QVBoxLayout()

        self.db_conn_btn = QtWidgets.QPushButton("Open Database")
        self.db_conn_btn.clicked.connect(self.openDB)
        self.db_vBox.addWidget(self.db_conn_btn)
        self.db_groupBox.setLayout(self.db_vBox)

    def openDB(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', self.filePath)

        self.database = TEST_DB.DB_(fileName[0])

        if(self.database.cur):
            print('Connection Successful')      

    def expansionSet(self):
        self.comboBox_expansion = QtWidgets.QComboBox()
        self.comboBox_expansion.setPlaceholderText("Expansion")

        expansions = ['Base Game','Dunwich Horror','Kingsport','Innsmouth']

        for expan in expansions:
            self.comboBox_expansion.addItem(expan)

    def expansionChosen(self):
        thisExpan = self.comboBox_expansion.currentText()

        self.comboBox_locations.clear()
        self.locations = []

        if(thisExpan == 'Dunwich Horror'):
            self.locations = self.locationClass.locations_dunwich
        elif(thisExpan == 'Innsmouth'):
            self.locations = self.locationClass.locations_innsmouth
        elif(thisExpan == 'Kingsport'):
            self.locations = self.locationClass.locations_kingsport
        else:
            self.locations = self.locationClass.locations_base
        
        self.locations = [item for sublist in self.locations for item in sublist]

        for loc in self.locations:
            self.comboBox_locations.addItem(loc)
        
        self.comboBox_locations.setEnabled(True)
        self.incStreets.setEnabled(True)
        self.incOW.setEnabled(True)
        self.isCustom.setEnabled(True)

    def includeStreets(self):

        if(self.incStreets.isChecked()):
            thisExpan = self.comboBox_expansion.currentText()
        
            streetLocations = []

            if(thisExpan == 'Dunwich Horror'):
                streetLocations = self.locationClass.streets_dunwich
            elif(thisExpan == 'Kingsport'):
                streetLocations = self.locationClass.streets_kingsport
            elif(thisExpan == 'Innsmouth'):
                streetLocations = self.locationClass.streets_innsmouth
            else:
                streetLocations = self.locationClass.streets_base

            #streetLocations = [item for sublist in streetLocations for item in sublist]

            for sLoc in streetLocations:
                self.comboBox_locations.addItem(sLoc+" Streets")
            
        else:
            self.expansionChosen()

    def includeOW(self):
        if(self.incOW.isChecked()):
            thisExpan = self.comboBox_expansion.currentText()
        
            owLocations = []

            if(thisExpan == 'Dunwich Horror'):
                owLocations = self.locationClass.otherWorlds_dunwich
            elif(thisExpan == 'Kingsport'):
                owLocations = self.locationClass.otherWorlds_kingsport
            elif(thisExpan == 'Base Game'):
                owLocations = self.locationClass.otherWorlds_base

            for loc in owLocations:
                self.comboBox_locations.addItem(loc)
                self.incStreets.setChecked(False)
            
        else:
            self.expansionChosen()

    def homeLocation(self):

        self.comboBox_locations = QtWidgets.QComboBox()
        
        self.comboBox_locations.setEnabled(False)

    def charAttributes(self):

        self.attrbBox = QtWidgets.QGroupBox("Character Attributes")
        hBox = QtWidgets.QGridLayout()

        self.maxStamLine = QtWidgets.QLineEdit()
        self.maxStamLine.setPlaceholderText("Max Stamina")
        hBox.addWidget(self.maxStamLine,0,0)

        self.maxSntyLine = QtWidgets.QLineEdit()
        self.maxSntyLine.setPlaceholderText("Max Sanity")
        hBox.addWidget(self.maxSntyLine,0,1)

        self.focusLine = QtWidgets.QLineEdit()
        self.focusLine.setPlaceholderText("Focus")
        hBox.addWidget(self.focusLine,0,2)

        self.maxSpdLine = QtWidgets.QLineEdit()
        self.maxSpdLine.setPlaceholderText("Max Speed")
        hBox.addWidget(self.maxSpdLine,1,0)

        self.maxSnkLine = QtWidgets.QLineEdit()
        self.maxSnkLine.setPlaceholderText("Max Sneak")
        hBox.addWidget(self.maxSnkLine,1,1)

        self.maxFghtLine = QtWidgets.QLineEdit()
        self.maxFghtLine.setPlaceholderText("Max Fight")
        hBox.addWidget(self.maxFghtLine,1,2)

        self.maxWillLine = QtWidgets.QLineEdit()
        self.maxWillLine.setPlaceholderText("Max Will")
        hBox.addWidget(self.maxWillLine,2,0)

        self.maxLoreLine = QtWidgets.QLineEdit()
        self.maxLoreLine.setPlaceholderText("Max Lore")
        hBox.addWidget(self.maxLoreLine,2,1)

        self.maxLuckLine = QtWidgets.QLineEdit()
        self.maxLuckLine.setPlaceholderText("Max Luck")
        hBox.addWidget(self.maxLuckLine,2,2)

        self.attrbBox.setLayout(hBox)

    def possessions(self):
        
        def IT_comboBox(itemType):

            temp = QtWidgets.QComboBox()
            temp.addItems(itemType)
            temp.setCurrentIndex(len(itemType)-1)
            return temp
        
        def Item_comboBox():
            temp = QtWidgets.QComboBox()
            temp.setEnabled(False)
            return temp

        self.fPosBox = QtWidgets.QGroupBox("Possessions")
        grdLayout = QtWidgets.QGridLayout()

        fpLabel = QtWidgets.QLabel("Fixed Possessions:")
        grdLayout.addWidget(fpLabel,0,0)

        self.moneyLine = QtWidgets.QLineEdit()
        self.moneyLine.setPlaceholderText("Money")
        grdLayout.addWidget(self.moneyLine, 1,0)

        self.clueLine = QtWidgets.QLineEdit()
        self.clueLine.setPlaceholderText("Clue Tokens")
        grdLayout.addWidget(self.clueLine, 1,1)

        self.itemType = ['Common','Unique','Spell','Ally','Special','Item Type']

        self.fp_IType1 = IT_comboBox(self.itemType)
        self.fp_IType2 = IT_comboBox(self.itemType)
        self.fp_IType3 = IT_comboBox(self.itemType)

        grdLayout.addWidget(self.fp_IType1, 2, 0)
        grdLayout.addWidget(self.fp_IType2, 3, 0)
        grdLayout.addWidget(self.fp_IType3, 4, 0)

        self.fp_Item1 = Item_comboBox()
        self.fp_Item2 = Item_comboBox()
        self.fp_Item3 = Item_comboBox()

        grdLayout.addWidget(self.fp_Item1, 2, 1)
        grdLayout.addWidget(self.fp_Item2, 3, 1)
        grdLayout.addWidget(self.fp_Item3, 4, 1)

        ###
        ###
        ###

        rLabel = QtWidgets.QLabel("Random Possessions")
        grdLayout.addWidget(rLabel, 5, 0)

        self.commonLine = QtWidgets.QLineEdit()
        self.commonLine.setPlaceholderText("Common Items")
        grdLayout.addWidget(self.commonLine, 6, 0)

        self.unqLine = QtWidgets.QLineEdit()
        self.unqLine.setPlaceholderText("Unique Items")
        grdLayout.addWidget(self.unqLine, 6, 1)

        self.spellLine = QtWidgets.QLineEdit()
        self.spellLine.setPlaceholderText("Spells")
        grdLayout.addWidget(self.spellLine, 6, 2)

        self.allyLine = QtWidgets.QLineEdit()
        self.allyLine.setPlaceholderText("Allies")
        grdLayout.addWidget(self.allyLine, 7, 0)

        self.monstLine = QtWidgets.QLineEdit()
        self.monstLine.setPlaceholderText("Monsters")
        grdLayout.addWidget(self.monstLine, 7, 1)

        self.gateLine = QtWidgets.QLineEdit()
        self.gateLine.setPlaceholderText("Gates")
        grdLayout.addWidget(self.gateLine, 7, 2)

        self.fPosBox.setLayout(grdLayout) 

    def set_IL1(self):
        thisType = self.fp_IType1.currentText()

        self.fp_Item1.clear()

        if(thisType != self.itemType[-1]):

            self.fp_Item1.setEnabled(True)
            
            items = self.posClass.allPossessions[self.itemType.index(thisType)]
        
            for item in items:
                self.fp_Item1.addItem(item)
        
        else:
            self.fp_Item1.setEnabled(False)

    def set_IL2(self):
        thisType = self.fp_IType2.currentText()

        self.fp_Item2.clear()

        if(thisType != self.itemType[-1]):

            self.fp_Item2.setEnabled(True)
            
            items = self.posClass.allPossessions[self.itemType.index(thisType)]
        
            for item in items:
                self.fp_Item2.addItem(item)
        
        else:
            self.fp_Item2.setEnabled(False)

    def set_IL3(self):
        thisType = self.fp_IType3.currentText()

        self.fp_Item3.clear()

        if(thisType != self.itemType[-1]):

            self.fp_Item3.setEnabled(True)
            

            items = self.posClass.allPossessions[self.itemType.index(thisType)]
        
            for item in items:
                self.fp_Item3.addItem(item)
        else:
            self.fp_Item3.setEnabled(False)

    def submitCharacter(self):

        charAttributes = {}
        charAttributes["name"] = self.name.text()
        charAttributes["title"] = self.title.text()        
        charAttributes["home"] = self.comboBox_locations.currentText()
        charAttributes["money"] = int(self.moneyLine.text())
        charAttributes["clue_tokens"] = int(self.clueLine.text())
        charAttributes["focus"] = int(self.focusLine.text())
        charAttributes["max_speed"] = int(self.maxSpdLine.text())
        charAttributes["max_sneak"] = int(self.maxSnkLine.text())
        charAttributes["max_fight"] = int(self.maxFghtLine.text())
        charAttributes["max_will"] = int(self.maxWillLine.text())
        charAttributes["max_lore"] = int(self.maxLoreLine.text())
        charAttributes["max_luck"] = int(self.maxLuckLine.text())
        charAttributes["max_sanity"] = int(self.maxSntyLine.text())
        charAttributes["max_stamina"] = int(self.maxStamLine.text())
        
        charAttributes["expSet"] = self.comboBox_expansion.currentText()
        charAttributes["rand_commons"] = int(self.commonLine.text())
        charAttributes["rand_uniques"] = int(self.unqLine.text())
        charAttributes["rand_spells"] = int(self.spellLine.text())
        charAttributes["rand_allies"] = int(self.allyLine.text())
        charAttributes["rand_monsters"] = int(self.monstLine.text())
        charAttributes["rand_gates"] = int(self.gateLine.text())

        fp_types = ["Common", "Unique", "Spell", "Ally", "Special"]
        fp_types_attrb = ["fixed_commons","fixed_uniques", "fixed_spells","fixed_allies","fixed_special"]
        fixed_possessions = [[], [], [], [], []]# Common, Unique, Spell, Ally, Special

        if(self.fp_Item1.isEnabled()):
            fixed_possessions[fp_types.index(self.fp_IType1.currentText())].append(self.fp_Item1.currentText())
        
        if(self.fp_Item2.isEnabled()):
            fixed_possessions[fp_types.index(self.fp_IType2.currentText())].append(self.fp_Item2.currentText())
        
        if(self.fp_Item3.isEnabled()):
            fixed_possessions[fp_types.index(self.fp_IType3.currentText())].append(self.fp_Item3.currentText())

        for ind in range(len(fp_types_attrb)):
            charAttributes[fp_types_attrb[ind]] = fixed_possessions[ind]

        print(charAttributes)
