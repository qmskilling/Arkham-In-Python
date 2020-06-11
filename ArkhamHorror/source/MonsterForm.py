from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QCheckBox, QGridLayout, QVBoxLayout, QButtonGroup
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QRadioButton, QGroupBox, QLineEdit, QFileDialog, QLabel
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

"""
Monster form submission v 1.0
This code will create a GUI to submit a new monster.

In this version (v 1.0):
A GUI will prompt user for monster information, including images to be used for monster tokens.
Upon submitting data, it is saved to a dictionary and printed to the console.
Only one monster can be submitted at this time (due to nature of python dictionaries).

For future versions:
Connect to monster database.
Option to add, edit, or delete monsters (will include search feature).
Reduce number of packages needed to be imported, possibly by using PyQt5 objects
"""

#Class object for the GUI
class Window(QDialog):
    def __init__(self):
        super().__init__()
        
        #Initializes GUI with provided info: size, icon, title, etc.

        self.filePath = "/home/q/Documents/ArkhamHorror/Images/"#Change this line to local directory. Note: you may need to change direction of slashes.
        self.windowTitle = "New Monster Data"
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

        #Creates GUI and sets window size, title, icon (image)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.windowTitle)

        #This controls placement of objects vertically in window
        vbox = QVBoxLayout()

        #Input for monster name
        self.name = QLineEdit()
        self.name.setPlaceholderText('Monster Name')
        vbox.addWidget(self.name)

        #Input for monster movement
        self.monsterMovement()
        vbox.addWidget(self.mv_groupBox)

        #Input for dimensional symbols
        self.dimSymbol()
        vbox.addWidget(self.dimSym_groupBox)

        #input for monster abilities
        self.monstAbilities()
        vbox.addWidget(self.abil_groupBox)

        #Input for modifiers (horror, combat, etc)
        self.monstMods()
        vbox.addWidget(self.mod_groupBox)

        #Allows user to upload monster token images
        self.selectImageFiles()
        vbox.addWidget(self.img_groupBox)

        #Button to submit the data
        self.btn = QPushButton("Submit Data")
        self.btn.clicked.connect(self.getData)
        vbox.addWidget(self.btn)

        self.setLayout(vbox)
        self.show()

    def monsterMovement(self):
        """
        Monster movement uses radio button to ensure only one type of movement possible.
        This can be easily changed to checkboxes (see modifiers) for movement combos.
        New movement types are also easily added.
        """

        #Group box to separate monster movement from other attributes. Uses a grid layout for placement of buttons.
        self.mv_groupBox = QGroupBox('Monster Movement')
        gridLayout = QGridLayout()
        
        #Creates buttons for each movement type
        self.mvType = ['Flying','Fast','Immobile','Normal','Special','Stalker']
        self.mv_RB = [None]*len(self.mvType)

        for i in range(len(self.mvType)):
            self.mv_RB[i] = QRadioButton(self.mvType[i])
            gridLayout.addWidget(self.mv_RB[i], 0, i)

        #Text box that becomes actived when 'Special' movement is selected (think Cthonian)
        self.mv_specBox = QLineEdit()        
        self.mv_specBox.setPlaceholderText('Input special monster movement here.')
        self.mv_specBox.setEnabled(False)
        self.mv_RB[4].toggled.connect(self.mv_enableTB)

        gridLayout.addWidget(self.mv_specBox, 1, 0, 1, len(self.mvType))

        #Places all objects in the grid
        self.mv_groupBox.setLayout(gridLayout)
    
    def mv_enableTB(self):
        """
        Function that controls whether the 'Special' movement input is enabled.
        Can be removed without loss of generality.
        """

        if self.mv_RB[4].isChecked():
            self.mv_specBox.setEnabled(True)
        else:
            self.mv_specBox.setEnabled(False)

    def dimSymbol(self):
        """
        Function to create dimensional symbol radio buttons. Each monster can have only one symbol.
        """

        #Another group box to separate data.
        self.dimSym_groupBox = QGroupBox('Dimensional Symbol')
        gridLayout = QGridLayout()

        #Creates the radio buttons and uses images instead of words (I just wanted to be fancy)
        self.dimImages = ['circle.png','diamond.png','plus.png','slash.png','hexagon.png','star.png','moon.png','square.png','triangle.png']
        self.dim_RB = [None]*len(self.dimImages)

        print('/home/q/Documents/ArkhamHorror/Images/dims/'+self.dimImages[0])

        for i in range(len(self.dimImages)):
            self.dim_RB[i] = QRadioButton()
            self.dim_RB[i].setIcon(QtGui.QIcon('../Images/dims/'+self.dimImages[i]))
            gridLayout.addWidget(self.dim_RB[i], 0, i)

        #Places objects in the grid.
        self.dimSym_groupBox.setLayout(gridLayout)

    def monstAbilities(self):
        
        #Another group box to separate data.
        self.abil_groupBox = QGroupBox('Monster Abilities')
        gridLayout = QGridLayout()

        #Creates checkboxes for the abilities. Each monster can have any number of abilities.
        self.abilities = ['Nightmarish','Overwhelming','Special','Ambush','Mask','Undead']
        self.abil_cb = [None]*len(self.abilities)

        for i in range(len(self.abilities)):
            self.abil_cb[i] = QCheckBox(self.abilities[i])
            gridLayout.addWidget(self.abil_cb[i], 0, i, 1, 1)

        #Text input for Nightmarish value. Only positive numbers should be input, but this feature needs to be added.
        self.nightBox = QLineEdit()
        self.nightBox.setPlaceholderText('Nightmarish')
        self.nightBox.setEnabled(False)
        self.abil_cb[0].stateChanged.connect(self.abil_NMTB)
        gridLayout.addWidget(self.nightBox, 1, 0)

        #Text input for Overwhelming value. Only positive numbers should be input, but this feature needs to be added.
        self.overBox = QLineEdit()
        self.overBox.setPlaceholderText('Overwhelming')
        self.overBox.setEnabled(False)
        self.abil_cb[1].stateChanged.connect(self.abil_OWTB)
        gridLayout.addWidget(self.overBox, 1, 1)

        #Text input for special ability. Think Mi-Go
        self.abil_specBox = QLineEdit()        
        self.abil_specBox.setPlaceholderText('Input special monster abilities here.')
        self.abil_specBox.setEnabled(False)
        self.abil_cb[2].stateChanged.connect(self.abil_enableTB)
        gridLayout.addWidget(self.abil_specBox, 1, 2, 1, len(self.abilities)-2)

        #Adds all objects to the grid
        self.abil_groupBox.setLayout(gridLayout)

    def abil_enableTB(self):
        """
        Function for enabling special ability text input.
        All instances can be deleted without loss of functionality.
        """
        if self.abil_cb[2].isChecked():
            self.abil_specBox.setEnabled(True)
        else:
            self.abil_specBox.setEnabled(False)
    
    def abil_NMTB(self):
        """
        Function for enabling nightmarish input.
        All instances can be deleted without loss of functionality.
        """
        if self.abil_cb[0].isChecked():
            self.nightBox.setEnabled(True)
        else:
            self.nightBox.setEnabled(False)
    
    def abil_OWTB(self):
        """
        Function for enabling overwhelming input.
        All instances can be deleted without loss of functionality.
        """
        if self.abil_cb[1].isChecked():
            self.overBox.setEnabled(True)
        else:
            self.overBox.setEnabled(False)
    
    def monstMods(self):
        """
        Function for inputing monster modifiers, damage, and toughness.
        Here, all input is through text and no assurances are used to keep values in appropriate ranges (e.g. toughness > 1)
        """
        self.mod_groupBox = QGroupBox('Modifiers, Damages, and Toughness')
        hbox = QHBoxLayout()

        #Monster evasion
        self.evasion = QLineEdit()
        self.evasion.setPlaceholderText('Evasion')
        hbox.addWidget(self.evasion)

        #Horror Rating
        self.horMod = QLineEdit()
        self.horMod.setPlaceholderText('Horror Mod')
        hbox.addWidget(self.horMod)

        #Sanity Damage
        self.horDmg = QLineEdit()
        self.horDmg.setPlaceholderText('Sanity Dmg')
        hbox.addWidget(self.horDmg)

        #Combat Rating
        self.comMod = QLineEdit()
        self.comMod.setPlaceholderText('Combat Mod')
        hbox.addWidget(self.comMod)

        #Stamina damage
        self.comDmg = QLineEdit()
        self.comDmg.setPlaceholderText('Stamina Dmg')
        hbox.addWidget(self.comDmg)

        #toughness
        self.toughness = QLineEdit()
        self.toughness.setPlaceholderText('Toughness')
        hbox.addWidget(self.toughness)

        #Adds objects to group
        self.mod_groupBox.setLayout(hbox)

    def selectImageFiles(self):
        """
        This function allows users to upload image files for monster tokens(stored as path name)
        In the future, maybe it will be possible to create a token template so that new monster tokens can be easily created.
        """
        self.img_groupBox = QGroupBox('Select Image Files')
        gridLayout = QGridLayout()

        self.imgBtnGrp = QButtonGroup()

        #Button to get front of monster token. Displays image to GUI, saves file path to dict
        self.frontImgBtn = QPushButton("Select Front Image")
        self.imgBtnGrp.addButton(self.frontImgBtn, 1)
        self.frontLabel = QLabel("")
        self.frontImgBtn.clicked.connect(self.selectFrontImage)                
        gridLayout.addWidget(self.frontImgBtn, 0, 0)
        gridLayout.addWidget(self.frontLabel, 1, 0)

        #Button to get back of monster token. Displays image to GUI, saves file path to dict
        self.backImgBtn = QPushButton("Select Back Image")
        self.imgBtnGrp.addButton(self.backImgBtn, 2)
        self.backLabel = QLabel("")
        self.backImgName = self.backImgBtn.clicked.connect(self.selectBackImage)        
        gridLayout.addWidget(self.backImgBtn, 0, 1)
        gridLayout.addWidget(self.backLabel, 1, 1)

        self.img_groupBox.setLayout(gridLayout)
    
    def selectFrontImage(self):
        """
        Function to select image. Gets file path and displays image.
        Ideally, making this more abstract to avoid duplication would be nice.
        """
        fileName = QFileDialog.getOpenFileName(self, 'Open File', self.filePath + "Monsters/")
        imgPath = fileName[0]
        self.frontImgPath = imgPath
        pMap = QPixmap(imgPath)
        self.frontLabel.setPixmap(QPixmap(pMap))

    def selectBackImage(self):
        """
        Function to select image. Gets file path and displays image.
        Ideally, making this more abstract to avoid duplication would be nice.
        """
        fileName = QFileDialog.getOpenFileName(self, 'Open File', self.filePath + "Monsters/")
        imgPath = fileName[0]
        self.backImgPath = imgPath
        pMap = QPixmap(imgPath)
        self.backLabel.setPixmap(QPixmap(pMap))

    def getData(self):
        """
        This function is actived when "submit data" is pressed.
        Saves input information to a dictionary and prints it to screen.
        Due to nature of dictionary, only one monster can currently be saved.
        """

        #Instantiates dictionary
        monsterAttributes = {}

        #Gets monster name
        monsterAttributes["Name"] = self.name.text()

        #Gets monster movement. Special movement vlue is saved as array: ['Special','Movement'] e.g. ['Special','Cthonian movement ability']
        for i in range(len(self.mvType)):
            if(self.mv_RB[i].isChecked()):

                if(self.mvType[i] == 'Special'):
                    specVal = [self.mvType[i], self.mv_specBox.text()]
                    monsterAttributes["Movement"] = specVal
                else:
                    monsterAttributes["Movement"] = self.mvType[i]
                self.mv_RB[i].setChecked(False)
                break

        #Gets dimensional symbol.
        for i in range(len(self.dim_RB)):
            if(self.dim_RB[i].isChecked()):
                monsterAttributes["Dimensional Symbol"] = self.dimImages[i][:-4]
                break
        
        #Creates a vector of monster abilities. Special abilities are saved as just the ability, e.g. 'When you defeat Mi-Go...'
        abilVec = []
        for i in range(len(self.abil_cb)):
            if(self.abil_cb[i].isChecked()):
                if(self.abilities[i] == 'Nightmarish'):
                    abilVec.append(self.abilities[i] + " " + str(self.nightBox.text()))
                elif(self.abilities[i] == 'Overwhelming'):
                    abilVec.append(self.abilities[i] + " " + str(self.overBox.text()))
                elif(self.abilities[i] == 'Special'):
                    abilVec.append(self.abil_specBox.text())
                else:
                    abilVec.append(self.abilities[i])
        
        #Saves monster abilities to the dictionary
        monsterAttributes["Abilities"] = abilVec

        #Saves monster modifiers, damage, toughness, and image files to the dictionary.
        monsterAttributes["Evasion"] = self.evasion.text()
        monsterAttributes["Horror Rating"] = self.horMod.text()
        monsterAttributes["Sanity Damage"] = self.horDmg.text()
        monsterAttributes["Combat Rating"] = self.comMod.text()
        monsterAttributes["Combat Damage"] = self.comDmg.text()
        monsterAttributes["Toughness"] = self.toughness.text()
        monsterAttributes["Image Files"] = [self.frontImgPath, self.backImgPath]

        #Just a check to see that data in input properly.                
        print(monsterAttributes)

#CSS-like style. Will expand on this more.
StyleSheet = '''
QCheckBox {         
    font-family:'Arial';      
    font-size:15px;
}
'''

#Creates the window
if __name__ == "__main__":
    App = QApplication(sys.argv)
    App.setStyleSheet(StyleSheet)
    window = Window()

    sys.exit(App.exec())
