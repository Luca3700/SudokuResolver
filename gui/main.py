from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QComboBox, QGridLayout
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import QSize
import sys
# from PySide2.QtGui import QFocusEvent
# import PySide2.QtCore as qtCore

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sudoku Solver")
        self.setFixedSize(QSize(400, 300))

        items = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        cell1 = QComboBox()
        cell1.addItems(items)

        cell2 = QComboBox()
        # cell2.resize(200,200
        #     # self.tree.width() / 8,
        #     # self.tree.width() / 8,
        # )
        cell2.setFixedSize(200,200)
        cell2.addItems(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        cell3 = QComboBox()
        cell3.addItems(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        cell4 = QComboBox()
        cell4.addItems(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
      

        layout = QGridLayout()

        layout.addWidget(self.createCell(200), 0, 0)
        layout.addWidget(cell2, 1, 0)
        layout.addWidget(cell3, 1, 1)
        layout.addWidget(cell4, 2, 1)


        # Sends the current index (position) of the selected item.
        # widget.currentIndexChanged.connect( self.index_changed )

        # There is an alternate signal to send the text.
        cell1.currentTextChanged.connect( self.text_changed )

        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setCentralWidget(widget)

        # self.label = QLabel()

        # self.input = QLineEdit()
        # self.input.setMaxLength(1)
        # self.input.textChanged.connect(self.label.setText)

        # layout = QVBoxLayout()
        # layout.addWidget(self.input)
        # layout.addWidget(self.label)

        # container = QWidget()
        # container.setLayout(layout)

        # # Set the central widget of the Window.
        # self.setCentralWidget(container)

    def index_changed(self, i): # i is an int
        print(i)

    def text_changed(self, s): # s is a str
        print(s)

    def createCell(self, size):
        items = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        cell = QComboBox()
        cell.addItems(items)
        cell.setFixedSize(size, size)
        return cell

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()