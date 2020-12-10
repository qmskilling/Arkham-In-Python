from PyQt5 import QtWidgets, QtCore, QtGui
import sys

#Requires screeninfo package (pip install screeninfo)
import screeninfo

class gameWindow(QtWidgets.QWidget):

    #Class initializer and main window properties
    def __init__(self):
        
        super().__init__()

        #Gets information about monitor
        self.mon = screeninfo.get_monitors()

        self.filePath = "/home/q/Documents/ArkhamHorror/Images/"#Change this line to local directory. Note: you may need to change direction of slashes.
        self.windowTitle = "Arkham Horror: A Digital Experience"
        self.iconName = self.filePath + "/GUI/ES_icon2.png"
        
        #Creates GUI and sets window size, title, icon (image)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(100, 100, self.mon[0].width-100, self.mon[0].height-100)
        self.setWindowTitle(self.windowTitle)

        self.mainLayout = QtWidgets.QGridLayout(self)

        self.frame_board()
        self.frame_tabSection()
        self.frame_chat()
        self.setLayout(self.mainLayout)
    
    #Instantiates frame that holds the game board
    def frame_board(self):
        
        #Board Frame
        boardFrame = QtWidgets.QFrame()
        boardFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)

        rightLayout = QtWidgets.QVBoxLayout(boardFrame)

        rightLayout.addWidget(QtWidgets.QLabel("Game Board Placeholder"))

        boardFrame.setLayout(rightLayout)

        self.mainLayout.addWidget(boardFrame,0,1,2,1)

    #Instantiates frame that holds tabs used for various game pieces
    def frame_tabSection(self):

        #Tab'd section frame
        tabFrame = QtWidgets.QFrame()
        tabFrame.setFrameShape(QtWidgets.QFrame.NoFrame)

        tabLayout = QtWidgets.QVBoxLayout(tabFrame)

        tabs_obj = QtWidgets.QTabWidget()

        tabs = {}
        tab_labels = ("Ancient One","Heralds & Gaurdians","Monsters","Characters")
        for i in range(len(tab_labels)):
            tabs[i] = QtWidgets.QWidget()
            tabs_obj.addTab(tabs[i],tab_labels[i])
            tabs_obj.setMovable(True)

        # tab1 = QtWidgets.QWidget()
        # tab2 = QtWidgets.QWidget()
        # tab3 = QtWidgets.QWidget()
        # tab4 = QtWidgets.QWidget()

        # tabs.addTab(tab1,"Ancient One")
        # tabs.addTab(tab2, "Heralds/Gaurdians")
        # tabs.addTab(tab3, "Monsters")        
        # tabs.addTab(tab4, "Characters")


        tabLayout.addWidget(tabs_obj)

        tabFrame.setFixedWidth(int(0.25*self.mon[0].width))
        tabFrame.setFixedHeight(int(0.5*self.mon[0].height))

        self.mainLayout.addWidget(tabFrame,0,0,1,1)

    #Instantiates frame that holds the chat window
    def frame_chat(self):

        #Chat Frame
        chatFrame = QtWidgets.QFrame()
        chatFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)

        chatLayout = QtWidgets.QVBoxLayout(chatFrame)

        chatLayout.addWidget(QtWidgets.QLabel("Chat Window Placeholder"))

        self.mainLayout.addWidget(chatFrame,1,0,1,1)



gameApp = QtWidgets.QApplication(sys.argv)

game = gameWindow()
game.show()

sys.exit(gameApp.exec())

