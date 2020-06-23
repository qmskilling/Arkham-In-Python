import PyQt5
import sys
import MonsterForm_Class
import CharacterForm_Classy

App = PyQt5.QtWidgets.QApplication(sys.argv)
#window = MonsterForm_Class.Window()

window = CharacterForm_Classy.CF_Window()

sys.exit(App.exec())


