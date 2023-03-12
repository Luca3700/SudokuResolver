from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet
import darkdetect
import sys
from gui.mainWindow import *

app = QApplication(sys.argv)

# setup stylesheet
try:
    if darkdetect.isDark():
        apply_stylesheet(app, theme='dark_blue.xml')
    else:
        apply_stylesheet(app, theme='light_blue.xml')
except:
    pass
finally:
    apply_stylesheet(app, theme='light_blue.xml')


window = MainWindow()
window.show()

app.exec()
