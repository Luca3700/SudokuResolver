from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QComboBox, QGridLayout
from PyQt5.QtGui import QPalette, QColor
import sys
# from PySide2.QtGui import QFocusEvent
# import PySide2.QtCore as qtCore

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sudoku Solver")


        self.input = QLineEdit()
        self.input.setMaxLength(1)
        #self.input.textChanged.connect(self.label.setText)
        
        layout = QGridLayout()

        layout.addWidget(input, 0, 0)
        # layout.addWidget(cell2, 1, 0)
        # layout.addWidget(cell3, 1, 1)
        # layout.addWidget(cell4, 2, 1)


        # Sends the current index (position) of the selected item.
        # widget.currentIndexChanged.connect( self.index_changed )

        # There is an alternate signal to send the text.
        #cell.currentTextChanged.connect( self.text_changed )

        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setCentralWidget(widget)

        
        

        container = QWidget()
        container.setLayout(layout)

        

    def index_changed(self, i): # i is an int
        print(i)

    def text_changed(self, s): # s is a str
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()