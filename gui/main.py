from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QGridLayout, QPushButton
from qt_material import apply_stylesheet
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sudoku Solver")
        self.resize(1000,1000)

        layout = QGridLayout() # to create the cells layout
        cellSize = 80

        # row 1
        self.cell11 = self.createCell(cellSize)
        self.cell12 = self.createCell(cellSize)
        self.cell13 = self.createCell(cellSize)
        self.cell14 = self.createCell(cellSize)
        self.cell15 = self.createCell(cellSize)
        self.cell16 = self.createCell(cellSize)
        self.cell17 = self.createCell(cellSize)
        self.cell18 = self.createCell(cellSize)
        self.cell19 = self.createCell(cellSize)
        layout.addWidget(self.cell11, 1, 1)
        layout.addWidget(self.cell12, 1, 2) 
        layout.addWidget(self.cell13, 1, 3)    
        layout.addWidget(self.cell14, 1, 4)   
        layout.addWidget(self.cell15, 1, 5)
        layout.addWidget(self.cell16, 1, 6)
        layout.addWidget(self.cell17, 1, 7)
        layout.addWidget(self.cell18, 1, 8)
        layout.addWidget(self.cell19, 1, 9)

        # row 2
        self.cell21 = self.createCell(cellSize)
        self.cell22 = self.createCell(cellSize)
        self.cell23 = self.createCell(cellSize)
        self.cell24 = self.createCell(cellSize)
        self.cell25 = self.createCell(cellSize)
        self.cell26 = self.createCell(cellSize)
        self.cell27 = self.createCell(cellSize)
        self.cell28 = self.createCell(cellSize)
        self.cell29 = self.createCell(cellSize)
        layout.addWidget(self.cell21, 2, 1)
        layout.addWidget(self.cell22, 2, 2) 
        layout.addWidget(self.cell23, 2, 3)    
        layout.addWidget(self.cell24, 2, 4)   
        layout.addWidget(self.cell25, 2, 5)
        layout.addWidget(self.cell26, 2, 6)
        layout.addWidget(self.cell27, 2, 7)
        layout.addWidget(self.cell28, 2, 8)
        layout.addWidget(self.cell29, 2, 9)

        # row 3
        self.cell31 = self.createCell(cellSize)
        self.cell32 = self.createCell(cellSize)
        self.cell33 = self.createCell(cellSize)
        self.cell34 = self.createCell(cellSize)
        self.cell35 = self.createCell(cellSize)
        self.cell36 = self.createCell(cellSize)
        self.cell37 = self.createCell(cellSize)
        self.cell38 = self.createCell(cellSize)
        self.cell39 = self.createCell(cellSize)
        layout.addWidget(self.cell31, 3, 1)
        layout.addWidget(self.cell32, 3, 2) 
        layout.addWidget(self.cell33, 3, 3)    
        layout.addWidget(self.cell34, 3, 4)   
        layout.addWidget(self.cell35, 3, 5)
        layout.addWidget(self.cell36, 3, 6)
        layout.addWidget(self.cell37, 3, 7)
        layout.addWidget(self.cell38, 3, 8)
        layout.addWidget(self.cell39, 3, 9)

        # row 4
        self.cell41 = self.createCell(cellSize)
        self.cell42 = self.createCell(cellSize)
        self.cell43 = self.createCell(cellSize)
        self.cell44 = self.createCell(cellSize)
        self.cell45 = self.createCell(cellSize)
        self.cell46 = self.createCell(cellSize)
        self.cell47 = self.createCell(cellSize)
        self.cell48 = self.createCell(cellSize)
        self.cell49 = self.createCell(cellSize)
        layout.addWidget(self.cell41, 4, 1)
        layout.addWidget(self.cell42, 4, 2) 
        layout.addWidget(self.cell43, 4, 3)    
        layout.addWidget(self.cell44, 4, 4)   
        layout.addWidget(self.cell45, 4, 5)
        layout.addWidget(self.cell46, 4, 6)
        layout.addWidget(self.cell47, 4, 7)
        layout.addWidget(self.cell48, 4, 8)
        layout.addWidget(self.cell49, 4, 9)

        # row 5
        self.cell51 = self.createCell(cellSize)
        self.cell52 = self.createCell(cellSize)
        self.cell53 = self.createCell(cellSize)
        self.cell54 = self.createCell(cellSize)
        self.cell55 = self.createCell(cellSize)
        self.cell56 = self.createCell(cellSize)
        self.cell57 = self.createCell(cellSize)
        self.cell58 = self.createCell(cellSize)
        self.cell59 = self.createCell(cellSize)
        layout.addWidget(self.cell51, 5, 1)
        layout.addWidget(self.cell52, 5, 2) 
        layout.addWidget(self.cell53, 5, 3)    
        layout.addWidget(self.cell54, 5, 4)   
        layout.addWidget(self.cell55, 5, 5)
        layout.addWidget(self.cell56, 5, 6)
        layout.addWidget(self.cell57, 5, 7)
        layout.addWidget(self.cell58, 5, 8)
        layout.addWidget(self.cell59, 5, 9)

        # row 6
        self.cell61 = self.createCell(cellSize)
        self.cell62 = self.createCell(cellSize)
        self.cell63 = self.createCell(cellSize)
        self.cell64 = self.createCell(cellSize)
        self.cell65 = self.createCell(cellSize)
        self.cell66 = self.createCell(cellSize)
        self.cell67 = self.createCell(cellSize)
        self.cell68 = self.createCell(cellSize)
        self.cell69 = self.createCell(cellSize)
        layout.addWidget(self.cell61, 6, 1)
        layout.addWidget(self.cell62, 6, 2) 
        layout.addWidget(self.cell63, 6, 3)    
        layout.addWidget(self.cell64, 6, 4)   
        layout.addWidget(self.cell65, 6, 5)
        layout.addWidget(self.cell66, 6, 6)
        layout.addWidget(self.cell67, 6, 7)
        layout.addWidget(self.cell68, 6, 8)
        layout.addWidget(self.cell69, 6, 9)

        # row 7
        self.cell71 = self.createCell(cellSize)
        self.cell72 = self.createCell(cellSize)
        self.cell73 = self.createCell(cellSize)
        self.cell74 = self.createCell(cellSize)
        self.cell75 = self.createCell(cellSize)
        self.cell76 = self.createCell(cellSize)
        self.cell77 = self.createCell(cellSize)
        self.cell78 = self.createCell(cellSize)
        self.cell79 = self.createCell(cellSize)
        layout.addWidget(self.cell71, 7, 1)
        layout.addWidget(self.cell72, 7, 2) 
        layout.addWidget(self.cell73, 7, 3)    
        layout.addWidget(self.cell74, 7, 4)   
        layout.addWidget(self.cell75, 7, 5)
        layout.addWidget(self.cell76, 7, 6)
        layout.addWidget(self.cell77, 7, 7)
        layout.addWidget(self.cell78, 7, 8)
        layout.addWidget(self.cell79, 7, 9)

        # row 8
        self.cell81 = self.createCell(cellSize)
        self.cell82 = self.createCell(cellSize)
        self.cell83 = self.createCell(cellSize)
        self.cell84 = self.createCell(cellSize)
        self.cell85 = self.createCell(cellSize)
        self.cell86 = self.createCell(cellSize)
        self.cell87 = self.createCell(cellSize)
        self.cell88 = self.createCell(cellSize)
        self.cell89 = self.createCell(cellSize)
        layout.addWidget(self.cell81, 8, 1)
        layout.addWidget(self.cell82, 8, 2) 
        layout.addWidget(self.cell83, 8, 3)    
        layout.addWidget(self.cell84, 8, 4)   
        layout.addWidget(self.cell85, 8, 5)
        layout.addWidget(self.cell86, 8, 6)
        layout.addWidget(self.cell87, 8, 7)
        layout.addWidget(self.cell88, 8, 8)
        layout.addWidget(self.cell89, 8, 9)

        # row 9
        self.cell91 = self.createCell(cellSize)
        self.cell92 = self.createCell(cellSize)
        self.cell93 = self.createCell(cellSize)
        self.cell94 = self.createCell(cellSize)
        self.cell95 = self.createCell(cellSize)
        self.cell96 = self.createCell(cellSize)
        self.cell97 = self.createCell(cellSize)
        self.cell98 = self.createCell(cellSize)
        self.cell99 = self.createCell(cellSize)
        layout.addWidget(self.cell91, 9, 1)
        layout.addWidget(self.cell92, 9, 2) 
        layout.addWidget(self.cell93, 9, 3)    
        layout.addWidget(self.cell94, 9, 4)   
        layout.addWidget(self.cell95, 9, 5)
        layout.addWidget(self.cell96, 9, 6)
        layout.addWidget(self.cell97, 9, 7)
        layout.addWidget(self.cell98, 9, 8)
        layout.addWidget(self.cell99, 9, 9)


        button = QPushButton("Solve it!")
        button.setCheckable(True)
        layout.addWidget(button, 10, 5)
        button.clicked.connect(self.the_button_was_clicked)

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
    
    def create_file(self):
        string = "pre = \n[| ", \
            {self.cell11.currentText()}, ",", \
            {self.cell12.currentText()}, ",", \
            {self.cell13.currentText()}, ",", \
            {self.cell14.currentText()}, ",", \
            {self.cell15.currentText()}, ",", \
            {self.cell16.currentText()}, ",", \
            {self.cell17.currentText()}, ",", \
            {self.cell18.currentText()}, ",", \
            {self.cell19.currentText()}, "\n| ", \
            \
            {self.cell21.currentText()}, ",", \
            {self.cell22.currentText()}, ",", \
            {self.cell23.currentText()}, ",", \
            {self.cell24.currentText()}, ",", \
            {self.cell25.currentText()}, ",", \
            {self.cell26.currentText()}, ",", \
            {self.cell27.currentText()}, ",", \
            {self.cell28.currentText()}, ",", \
            {self.cell29.currentText()}, "\n| ", \
            \
            {self.cell31.currentText()}, ",", \
            {self.cell32.currentText()}, ",", \
            {self.cell33.currentText()}, ",", \
            {self.cell34.currentText()}, ",", \
            {self.cell35.currentText()}, ",", \
            {self.cell36.currentText()}, ",", \
            {self.cell37.currentText()}, ",", \
            {self.cell38.currentText()}, ",", \
            {self.cell39.currentText()}, "\n| ", \
            \
            {self.cell41.currentText()}, ",", \
            {self.cell42.currentText()}, ",", \
            {self.cell43.currentText()}, ",", \
            {self.cell44.currentText()}, ",", \
            {self.cell45.currentText()}, ",", \
            {self.cell46.currentText()}, ",", \
            {self.cell47.currentText()}, ",", \
            {self.cell48.currentText()}, ",", \
            {self.cell49.currentText()}, "\n| ", \
            \
            {self.cell51.currentText()}, ",", \
            {self.cell52.currentText()}, ",", \
            {self.cell53.currentText()}, ",", \
            {self.cell54.currentText()}, ",", \
            {self.cell55.currentText()}, ",", \
            {self.cell56.currentText()}, ",", \
            {self.cell57.currentText()}, ",", \
            {self.cell58.currentText()}, ",", \
            {self.cell59.currentText()}, "\n| ", \
            \
            {self.cell61.currentText()}, ",", \
            {self.cell62.currentText()}, ",", \
            {self.cell63.currentText()}, ",", \
            {self.cell64.currentText()}, ",", \
            {self.cell65.currentText()}, ",", \
            {self.cell66.currentText()}, ",", \
            {self.cell67.currentText()}, ",", \
            {self.cell68.currentText()}, ",", \
            {self.cell69.currentText()}, "\n| ", \
            \
            {self.cell71.currentText()}, ",", \
            {self.cell72.currentText()}, ",", \
            {self.cell73.currentText()}, ",", \
            {self.cell74.currentText()}, ",", \
            {self.cell75.currentText()}, ",", \
            {self.cell76.currentText()}, ",", \
            {self.cell77.currentText()}, ",", \
            {self.cell78.currentText()}, ",", \
            {self.cell79.currentText()}, "\n| ", \
            \
            {self.cell81.currentText()}, ",", \
            {self.cell82.currentText()}, ",", \
            {self.cell83.currentText()}, ",", \
            {self.cell84.currentText()}, ",", \
            {self.cell85.currentText()}, ",", \
            {self.cell86.currentText()}, ",", \
            {self.cell87.currentText()}, ",", \
            {self.cell88.currentText()}, ",", \
            {self.cell89.currentText()}, "\n| ", \
            \
            {self.cell91.currentText()}, ",", \
            {self.cell92.currentText()}, ",", \
            {self.cell93.currentText()}, ",", \
            {self.cell94.currentText()}, ",", \
            {self.cell95.currentText()}, ",", \
            {self.cell96.currentText()}, ",", \
            {self.cell97.currentText()}, ",", \
            {self.cell98.currentText()}, ",", \
            {self.cell99.currentText()}, " |];"
        return string

    def the_button_was_clicked(self):
        string = self.create_string()
        # save the string in the file
        file = open('../model/file.dzn', 'w')
        file.write(string)
        file.close()

        # solving 
        

app = QApplication(sys.argv)

# setup stylesheet
apply_stylesheet(app, theme='light_blue.xml')

window = MainWindow()
window.show()

app.exec()