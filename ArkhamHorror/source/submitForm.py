from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLineEdit, QMessageBox, QVBoxLayout
from PyQt5 import QtGui
import sys

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.windowTitle = "Grid Layout"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 400
        self.iconName = "C:/Users/Quinton/Documents/ArkhamHorror/Images/GUI/ES_icon2.png"

        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.windowTitle)

        vbox = QVBoxLayout()
        
        self.name = QLineEdit()
        self.name.setPlaceholderText("Please Enter Your Name")
        self.name.setStyleSheet('background:yellow')
        self.name.setFont(QtGui.QFont("Arial", 15))
        vbox.addWidget(self.name)

        self.email = QLineEdit()
        self.email.setPlaceholderText("Please Enter Your Email")
        self.email.setStyleSheet('background:yellow')
        self.email.setFont(QtGui.QFont("Arial", 15))
        vbox.addWidget(self.email)

        self.btn = QPushButton("Insert Data")
        self.btn.setStyleSheet('background:green')
        self.btn.setFont(QtGui.QFont('Arial',15))
        vbox.addWidget(self.btn)

        self.setLayout(vbox)
        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())