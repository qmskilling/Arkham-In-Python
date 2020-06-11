from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QCheckBox, QGridLayout, QVBoxLayout, QButtonGroup
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QRadioButton, QGroupBox, QLineEdit, QFileDialog, QLabel
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class Window(QDialog):
    def __init__(self):
        super().__init__()
        
        self.filePath = "/home/q/Documents/ArkhamHorror/Images/"
        self.windowTitle = "New Monster Data"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 400
        self.iconName = self.filePath + "/GUI/ES_icon2.png"
        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.windowTitle)

        vbox = QVBoxLayout()

        self.name = QLineEdit()
        self.name.setPlaceholderText('Monster Name')
        vbox.addWidget(self.name)

        self.monsterMovement()
        vbox.addWidget(self.mv_groupBox)

        self.dimSymbol()
        vbox.addWidget(self.dimSym_groupBox)

        self.monstAbilities()
        vbox.addWidget(self.abil_groupBox)

        self.monstMods()
        vbox.addWidget(self.mod_groupBox)

        self.selectImageFiles()
        vbox.addWidget(self.img_groupBox)

        self.btn = QPushButton("Submit Data")
        self.btn.clicked.connect(self.getData)
        vbox.addWidget(self.btn)

        self.setLayout(vbox)
        self.show()

    def monsterMovement(self):
        self.mv_groupBox = QGroupBox('Monster Movement')
        gridLayout = QGridLayout()
        self.mvType = ['Flying','Fast','Immobile','Normal','Special','Stalker']
        self.mv_RB = [None]*len(self.mvType)

        for i in range(len(self.mvType)):
            self.mv_RB[i] = QRadioButton(self.mvType[i])
            gridLayout.addWidget(self.mv_RB[i], 0, i)

        self.mv_specBox = QLineEdit()        
        self.mv_specBox.setPlaceholderText('Input special monster movement here.')
        self.mv_specBox.setEnabled(False)
        self.mv_RB[4].toggled.connect(self.mv_enableTB)

        gridLayout.addWidget(self.mv_specBox, 1, 0, 1, len(self.mvType))

        self.mv_groupBox.setLayout(gridLayout)
    
    def mv_enableTB(self):
        if self.mv_RB[4].isChecked():
            self.mv_specBox.setEnabled(True)
        else:
            self.mv_specBox.setEnabled(False)

    def dimSymbol(self):
        self.dimSym_groupBox = QGroupBox('Dimensional Symbol')
        gridLayout = QGridLayout()
        self.dimImages = ['circle.png','diamond.png','plus.png','slash.png','hexagon.png','star.png','moon.png','square.png','triangle.png']
        self.dim_RB = [None]*len(self.dimImages)

        print('/home/q/Documents/ArkhamHorror/Images/dims/'+self.dimImages[0])

        for i in range(len(self.dimImages)):
            self.dim_RB[i] = QRadioButton()
            self.dim_RB[i].setIcon(QtGui.QIcon('../Images/dims/'+self.dimImages[i]))
            gridLayout.addWidget(self.dim_RB[i], 0, i)

        self.dimSym_groupBox.setLayout(gridLayout)

    def monstAbilities(self):
        self.abil_groupBox = QGroupBox('Monster Abilities')
        gridLayout = QGridLayout()
        self.abilities = ['Nightmarish','Overwhelming','Special','Ambush','Mask','Undead']
        self.abil_cb = [None]*len(self.abilities)

        for i in range(len(self.abilities)):
            self.abil_cb[i] = QCheckBox(self.abilities[i])
            gridLayout.addWidget(self.abil_cb[i], 0, i, 1, 1)

        self.nightBox = QLineEdit()
        self.nightBox.setPlaceholderText('Nightmarish')
        self.nightBox.setEnabled(False)
        self.abil_cb[0].stateChanged.connect(self.abil_NMTB)
        gridLayout.addWidget(self.nightBox, 1, 0)

        self.overBox = QLineEdit()
        self.overBox.setPlaceholderText('Overwhelming')
        self.overBox.setEnabled(False)
        self.abil_cb[1].stateChanged.connect(self.abil_OWTB)
        gridLayout.addWidget(self.overBox, 1, 1)

        self.abil_specBox = QLineEdit()        
        self.abil_specBox.setPlaceholderText('Input special monster abilities here.')
        self.abil_specBox.setEnabled(False)
        self.abil_cb[2].stateChanged.connect(self.abil_enableTB)
        gridLayout.addWidget(self.abil_specBox, 1, 2, 1, len(self.abilities)-2)

        self.abil_groupBox.setLayout(gridLayout)

    def abil_enableTB(self):
        if self.abil_cb[2].isChecked():
            self.abil_specBox.setEnabled(True)
        else:
            self.abil_specBox.setEnabled(False)
    
    def abil_NMTB(self):
        if self.abil_cb[0].isChecked():
            self.nightBox.setEnabled(True)
        else:
            self.nightBox.setEnabled(False)
    
    def abil_OWTB(self):
        if self.abil_cb[1].isChecked():
            self.overBox.setEnabled(True)
        else:
            self.overBox.setEnabled(False)
    
    def monstMods(self):
        self.mod_groupBox = QGroupBox('Modifiers, Damages, and Toughness')
        hbox = QHBoxLayout()

        self.evasion = QLineEdit()
        self.evasion.setPlaceholderText('Evasion')
        hbox.addWidget(self.evasion)

        self.horMod = QLineEdit()
        self.horMod.setPlaceholderText('Horror Mod')
        hbox.addWidget(self.horMod)

        self.horDmg = QLineEdit()
        self.horDmg.setPlaceholderText('Sanity Dmg')
        hbox.addWidget(self.horDmg)

        self.comMod = QLineEdit()
        self.comMod.setPlaceholderText('Combat Mod')
        hbox.addWidget(self.comMod)

        self.comDmg = QLineEdit()
        self.comDmg.setPlaceholderText('Stamina Dmg')
        hbox.addWidget(self.comDmg)

        self.toughness = QLineEdit()
        self.toughness.setPlaceholderText('Toughness')
        hbox.addWidget(self.toughness)

        self.mod_groupBox.setLayout(hbox)

    def selectImageFiles(self):
        self.img_groupBox = QGroupBox('Select Image Files')
        gridLayout = QGridLayout()

        self.imgBtnGrp = QButtonGroup()

        self.frontImgBtn = QPushButton("Select Front Image")
        self.imgBtnGrp.addButton(self.frontImgBtn, 1)
        self.frontLabel = QLabel("")
        self.frontImgBtn.clicked.connect(self.selectFrontImage)                
        gridLayout.addWidget(self.frontImgBtn, 0, 0)
        gridLayout.addWidget(self.frontLabel, 1, 0)

        self.backImgBtn = QPushButton("Select Back Image")
        self.imgBtnGrp.addButton(self.backImgBtn, 2)
        self.backLabel = QLabel("")
        self.backImgName = self.backImgBtn.clicked.connect(self.selectBackImage)        
        gridLayout.addWidget(self.backImgBtn, 0, 1)
        gridLayout.addWidget(self.backLabel, 1, 1)

        self.img_groupBox.setLayout(gridLayout)
    
    def selectFrontImage(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open File', self.filePath + "Monsters/")
        imgPath = fileName[0]
        self.frontImgPath = imgPath
        pMap = QPixmap(imgPath)
        self.frontLabel.setPixmap(QPixmap(pMap))

    def selectBackImage(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open File', self.filePath + "Monsters/")
        imgPath = fileName[0]
        self.backImgPath = imgPath
        pMap = QPixmap(imgPath)
        self.backLabel.setPixmap(QPixmap(pMap))

    def getData(self):

        monsterAttributes = {}

        monsterAttributes["Name"] = self.name.text()

        for i in range(len(self.mvType)):
            if(self.mv_RB[i].isChecked()):

                if(self.mvType[i] == 'Special'):
                    specVal = [self.mvType[i], self.mv_specBox.text()]
                    monsterAttributes["Movement"] = specVal
                else:
                    monsterAttributes["Movement"] = self.mvType[i]
                self.mv_RB[i].setChecked(False)
                break

        for i in range(len(self.dim_RB)):
            if(self.dim_RB[i].isChecked()):
                monsterAttributes["Dimensional Symbol"] = self.dimImages[i][:-4]
                break
        
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
        
        monsterAttributes["Abilities"] = abilVec

        monsterAttributes["Evasion"] = self.evasion.text()
        monsterAttributes["Horror Rating"] = self.horMod.text()
        monsterAttributes["Sanity Damage"] = self.horDmg.text()
        monsterAttributes["Combat Rating"] = self.comMod.text()
        monsterAttributes["Combat Damage"] = self.comDmg.text()
        monsterAttributes["Toughness"] = self.toughness.text()
        monsterAttributes["Image Files"] = [self.frontImgPath, self.backImgPath]

        self.initWindow()
                
        print(monsterAttributes)
      
StyleSheet = '''
QCheckBox {         
    font-family:'Arial';      
    font-size:15px;
}
'''

if __name__ == "__main__":
    App = QApplication(sys.argv)
    App.setStyleSheet(StyleSheet)
    window = Window()

    sys.exit(App.exec())

    window.abil_cb[4].stateChanged.connect(window.enableTextBox)
