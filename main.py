from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet
import sys
from gui.mainWindow import *

app = QApplication(sys.argv)

# setup stylesheet
apply_stylesheet(app, theme='light_blue.xml')


window = MainWindow()
window.show()

app.exec()
