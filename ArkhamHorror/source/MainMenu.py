from PyQt5 import QtWidgets, QtCore, QtGui
import CharacterForm_Classy, MonsterForm_Class
import sys


class MainMenu(QtWidgets.QWidget):

    switch_HG = QtCore.pyqtSignal()
    switch_JG = QtCore.pyqtSignal()
    switch_MNG = QtCore.pyqtSignal()
    switch_info = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        #Initializes GUI with provided info: size, icon, title, etc.

        self.filePath = "/home/q/Documents/ArkhamHorror/Images/"#Change this line to local directory. Note: you may need to change direction of slashes.
        self.windowTitle = "Arkham Horror: A Digital Experience"
        self.top = 100
        self.left = 100
        self.width = 200
        self.height = 250
        self.iconName = self.filePath + "/GUI/ES_icon2.png"
        self.mainWindow()

    def mainWindow(self):
        """
        Window instantiation. Holds all feature creation (buttons, boxes, etc.)        
        """

        #Creates GUI and sets window size, title, icon (image)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.windowTitle)

        #This controls placement of objects vertically in window
        vbox = QtWidgets.QVBoxLayout()

        self.btn_hostGame = QtWidgets.QPushButton("Host Game")
        self.btn_hostGame.clicked.connect(self.hostGame)
        vbox.addWidget(self.btn_hostGame)

        self.btn_joinGame = QtWidgets.QPushButton("Join Game")
        self.btn_joinGame.clicked.connect(self.joinGame)
        vbox.addWidget(self.btn_joinGame)

        self.btn_mngCont = QtWidgets.QPushButton("Manage Content")
        self.btn_mngCont.clicked.connect(self.manage)
        vbox.addWidget(self.btn_mngCont)

        self.btn_info = QtWidgets.QPushButton("Game Information")
        self.btn_info.clicked.connect(self.info)
        vbox.addWidget(self.btn_info)

        self.setLayout(vbox)
    
    def hostGame(self):
        self.switch_HG.emit()

    def joinGame(self):
        self.switch_JG.emit()
    
    def manage(self):
        self.switch_MNG.emit()
    
    def info(self):
        self.switch_info.emit()

class window_hostGame(QtWidgets.QWidget):
    
    switch_main = QtCore.pyqtSignal()
    
    def __init__(self):
        super().__init__()

        #Initializes GUI with provided info: size, icon, title, etc.

        self.filePath = "/home/q/Documents/ArkhamHorror/Images/"#Change this line to local directory. Note: you may need to change direction of slashes.
        self.windowTitle = "Arkham Horror: A Digital Experience"
        self.top = 100
        self.left = 100
        self.width = 200
        self.height = 250
        self.iconName = self.filePath + "/GUI/ES_icon2.png"
        self.window()

    def window(self):
        """
        Window instantiation. Holds all feature creation (buttons, boxes, etc.)        
        """

        #Creates GUI and sets window size, title, icon (image)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.windowTitle)

        vBox = QtWidgets.QVBoxLayout()

        self.btn_newGame = QtWidgets.QPushButton("New Game")
        self.btn_newGame.clicked.connect(self.newGame)
        vBox.addWidget(self.btn_newGame)

        self.btn_loadGame = QtWidgets.QPushButton("Load Game")
        self.btn_loadGame.clicked.connect(self.loadGame)
        vBox.addWidget(self.btn_loadGame)

        self.btn_return = QtWidgets.QPushButton("Return to Main Menu")
        self.btn_return.clicked.connect(self.returnToMain)
        vBox.addWidget(self.btn_return)

        self.setLayout(vBox)

    def returnToMain(self):
        self.switch_main.emit()
    
    def newGame(self):
        return

    def loadGame(self):
        return
        
class window_joinGame(QtWidgets.QDialog):
    
    switch_main = QtCore.pyqtSignal()
    
    def __init__(self):
        super().__init__()

        #Initializes GUI with provided info: size, icon, title, etc.

        self.filePath = "/home/q/Documents/ArkhamHorror/Images/"#Change this line to local directory. Note: you may need to change direction of slashes.
        self.windowTitle = "Arkham Horror: A Digital Experience"
        self.top = 100
        self.left = 100
        self.width = 200
        self.height = 250
        self.iconName = self.filePath + "/GUI/ES_icon2.png"
        self.window()

    def window(self):
        """
        Window instantiation. Holds all feature creation (buttons, boxes, etc.)        
        """

        #Creates GUI and sets window size, title, icon (image)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.windowTitle)

        gridBox = QtWidgets.QGridLayout()

        self.inp_ipAddress = QtWidgets.QLineEdit()
        self.inp_ipAddress.setPlaceholderText("IP Address")
        gridBox.addWidget(self.inp_ipAddress,0,0,1,4)

        self.inp_pw = QtWidgets.QLineEdit()
        self.inp_pw.setPlaceholderText("Password")
        gridBox.addWidget(self.inp_pw,1,0,1,4)

        self.btn_joinGame = QtWidgets.QPushButton("Join Game")
        self.btn_joinGame.clicked.connect(self.joinGame)
        gridBox.addWidget(self.btn_joinGame,2,0,1,2)

        self.btn_return = QtWidgets.QPushButton("Return to Main Menu")
        self.btn_return.clicked.connect(self.returnToMain)
        gridBox.addWidget(self.btn_return,2,2,1,2)

        self.setLayout(gridBox)

    def returnToMain(self):
        self.switch_main.emit()
    
    def joinGame(self):
        return
                
class window_manageContent(QtWidgets.QDialog):

    switch_main = QtCore.pyqtSignal() 
    switch_monstForm = QtCore.pyqtSignal()
    switch_charForm = QtCore.pyqtSignal()
    
    def __init__(self):
        super().__init__()

        #Initializes GUI with provided info: size, icon, title, etc.

        self.filePath = "/home/q/Documents/ArkhamHorror/Images/"#Change this line to local directory. Note: you may need to change direction of slashes.
        self.windowTitle = "Arkham Horror: A Digital Experience"
        self.top = 100
        self.left = 100
        self.width = 200
        self.height = 250
        self.iconName = self.filePath + "/GUI/ES_icon2.png"
        self.window()

    def window(self):
        """
        Window instantiation. Holds all feature creation (buttons, boxes, etc.)        
        """

        #Creates GUI and sets window size, title, icon (image)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.windowTitle)

        vBox = QtWidgets.QVBoxLayout()

        self.btn_monsters = QtWidgets.QPushButton("Monsters")
        self.btn_monsters.clicked.connect(self.monstWindow)
        vBox.addWidget(self.btn_monsters)

        self.btn_characters = QtWidgets.QPushButton("Characters")
        self.btn_characters.clicked.connect(self.charWindow)
        vBox.addWidget(self.btn_characters)

        self.btn_gods = QtWidgets.QPushButton("Ancient Ones")
        self.btn_gods.clicked.connect(self.godWindow)
        vBox.addWidget(self.btn_gods)

        self.btn_items = QtWidgets.QPushButton("Items")
        self.btn_items.clicked.connect(self.itemWindow)
        vBox.addWidget(self.btn_items)

        self.btn_allies = QtWidgets.QPushButton("Allies")
        self.btn_allies.clicked.connect(self.allyWindow)
        vBox.addWidget(self.btn_allies)

        self.btn_HandG = QtWidgets.QPushButton("Heralds and Gardians")
        self.btn_HandG.clicked.connect(self.hrldWindow)
        vBox.addWidget(self.btn_HandG)

        self.btn_return = QtWidgets.QPushButton("Return to Main Menu")
        self.btn_return.clicked.connect(self.returnToMain)
        vBox.addWidget(self.btn_return)

        self.setLayout(vBox)

    def returnToMain(self):
        self.switch_main.emit()
    
    def hrldWindow(self):
        return

    def itemWindow(self):
        return
    
    def godWindow(self):
        return
    
    def monstWindow(self):
        self.switch_monstForm.emit()

    def charWindow(self):
        self.switch_charForm.emit()

    def allyWindow(self):
        return

class window_information(QtWidgets.QDialog):
        
    switch_main = QtCore.pyqtSignal()
    
    def __init__(self):
        super().__init__()

        #Initializes GUI with provided info: size, icon, title, etc.

        self.filePath = "/home/q/Documents/ArkhamHorror/Images/"#Change this line to local directory. Note: you may need to change direction of slashes.
        self.windowTitle = "Arkham Horror: A Digital Experience"
        self.top = 100
        self.left = 100
        self.width = 200
        self.height = 250
        self.iconName = self.filePath + "/GUI/ES_icon2.png"
        self.window()

    def window(self):
        """
        Window instantiation. Holds all feature creation (buttons, boxes, etc.)        
        """

        #Creates GUI and sets window size, title, icon (image)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.windowTitle)

        vBox = QtWidgets.QVBoxLayout()

        disclaimer = """Arkham Horror and all its contents belong to Fantasy Flight. This is merely a fanbased parody."""

        vBox.addWidget(QtWidgets.QLabel(disclaimer))

        self.btn_return = QtWidgets.QPushButton("Return to Main Menu")
        self.btn_return.clicked.connect(self.returnToMain)
        vBox.addWidget(self.btn_return)

        self.setLayout(vBox)
        
    def returnToMain(self):
        self.switch_main.emit()

class Controller():
    def __init__(self):
        pass

    def mainMenu(self):
        self.window_main = MainMenu()
        self.window_main.switch_HG.connect(self.hostGame)
        self.window_main.switch_JG.connect(self.joinGame)
        self.window_main.switch_MNG.connect(self.manageContent)
        self.window_main.switch_info.connect(self.info)
        
        self.window_main.show()

    def hostGame(self):
        def closeWindow():
            self.window_HG.close()
            self.window_main.show()
        
        self.window_HG = window_hostGame()
        self.window_HG.switch_main.connect(closeWindow)
        self.window_main.hide()
        self.window_HG.show()

    def joinGame(self):
        def closeWindow():
            self.window_JG.close()
            self.window_main.show()

        self.window_JG = window_joinGame()
        self.window_JG.switch_main.connect(closeWindow)
        self.window_main.hide()
        self.window_JG.show()
    
    def manageContent(self):
        def closeWindow():
            self.window_MNG.close()
            self.window_main.show()

        self.window_MNG = window_manageContent()
        
        self.window_MNG.switch_main.connect(closeWindow)
        self.window_MNG.switch_monstForm.connect(self.monstForm)
        self.window_MNG.switch_charForm.connect(self.charForm)

        self.window_main.hide()
        self.window_MNG.show()
    
    def monstForm(self):
        self.window_MF = MonsterForm_Class.Window()
        self.window_MNG.hide()
        self.window_MF.show()
    
    def charForm(self):
        self.window_CF = CharacterForm_Classy.CF_Window()
        self.window_MNG.hide()
        self.window_CF.show()

    def info(self):
        def closeWindow():
            self.window_info.close()
            self.window_main.show()
            
        self.window_info = window_information()
        self.window_info.switch_main.connect(closeWindow)
        self.window_main.hide()
        self.window_info.show()
        
if __name__ == '__main__':
    MainApp = QtWidgets.QApplication(sys.argv)

    mainMenu = Controller()
    mainMenu.mainMenu()

    sys.exit(MainApp.exec())
