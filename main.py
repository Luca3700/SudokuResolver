from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet
import sys
from gui.mainWindow import *

app = QApplication(sys.argv)

stylesheet = '''
    #MainWindow {
        background-image: url(./gui/icons/sudoku.png);
        background-repeat: no-repeat;
        background-position: center;
    }
'''

# setup stylesheet
apply_stylesheet(app, theme='light_blue.xml')


window = MainWindow()
window.setObjectName('MainWindow')
window.setStyleSheet(stylesheet)
window.show()

app.exec()
