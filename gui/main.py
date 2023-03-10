from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QGridLayout
from qt_material import apply_stylesheet
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sudoku Solver")
        self.resize(1000,1000)

        layout = QGridLayout() # to create the cells layout

        for i in range(9):
            for j in range(9):
                # adding in each position the combobox
                layout.addWidget(self.createCell(100), i, j)
        
        # creting the widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def createCell(self, size):
        # crete che combobox
        items = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        cell = QComboBox()
        cell.addItems(items)
        cell.setFixedSize(size, size)
        return cell

app = QApplication(sys.argv)

# setup stylesheet
apply_stylesheet(app, theme='light_blue.xml')

window = MainWindow()
window.show()

app.exec()