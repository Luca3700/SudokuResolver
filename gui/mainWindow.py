from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDir
import subprocess
from gui.customDialog import *
from gui.utils import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.utils = Utils()

        self.setWindowTitle("Sudoku Solver")
        # setting app icon (source: https://www.flaticon.com/free-icon/sudoku_5732078?term=sudoku&page=1&position=7&origin=tag&related_id=5732078)
        self.setWindowIcon(QIcon(QDir.currentPath() + '/gui/icons/sudoku.png'))
        self.resize(900,900)

        layout = QGridLayout() # to create the cells layout
        cellSize = 80

        label = QLabel()
        label.setFixedSize(10,10)

        # row 1
        self.cell11 = self.utils.createCell(cellSize)
        self.cell12 = self.utils.createCell(cellSize)
        self.cell13 = self.utils.createCell(cellSize)
        self.cell14 = self.utils.createCell(cellSize)
        self.cell15 = self.utils.createCell(cellSize)
        self.cell16 = self.utils.createCell(cellSize)
        self.cell17 = self.utils.createCell(cellSize)
        self.cell18 = self.utils.createCell(cellSize)
        self.cell19 = self.utils.createCell(cellSize)
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
        self.cell21 = self.utils.createCell(cellSize)
        self.cell22 = self.utils.createCell(cellSize)
        self.cell23 = self.utils.createCell(cellSize)
        self.cell24 = self.utils.createCell(cellSize)
        self.cell25 = self.utils.createCell(cellSize)
        self.cell26 = self.utils.createCell(cellSize)
        self.cell27 = self.utils.createCell(cellSize)
        self.cell28 = self.utils.createCell(cellSize)
        self.cell29 = self.utils.createCell(cellSize)
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
        self.cell31 = self.utils.createCell(cellSize)
        self.cell32 = self.utils.createCell(cellSize)
        self.cell33 = self.utils.createCell(cellSize)
        self.cell34 = self.utils.createCell(cellSize)
        self.cell35 = self.utils.createCell(cellSize)
        self.cell36 = self.utils.createCell(cellSize)
        self.cell37 = self.utils.createCell(cellSize)
        self.cell38 = self.utils.createCell(cellSize)
        self.cell39 = self.utils.createCell(cellSize)
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
        self.cell41 = self.utils.createCell(cellSize)
        self.cell42 = self.utils.createCell(cellSize)
        self.cell43 = self.utils.createCell(cellSize)
        self.cell44 = self.utils.createCell(cellSize)
        self.cell45 = self.utils.createCell(cellSize)
        self.cell46 = self.utils.createCell(cellSize)
        self.cell47 = self.utils.createCell(cellSize)
        self.cell48 = self.utils.createCell(cellSize)
        self.cell49 = self.utils.createCell(cellSize)
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
        self.cell51 = self.utils.createCell(cellSize)
        self.cell52 = self.utils.createCell(cellSize)
        self.cell53 = self.utils.createCell(cellSize)
        self.cell54 = self.utils.createCell(cellSize)
        self.cell55 = self.utils.createCell(cellSize)
        self.cell56 = self.utils.createCell(cellSize)
        self.cell57 = self.utils.createCell(cellSize)
        self.cell58 = self.utils.createCell(cellSize)
        self.cell59 = self.utils.createCell(cellSize)
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
        self.cell61 = self.utils.createCell(cellSize)
        self.cell62 = self.utils.createCell(cellSize)
        self.cell63 = self.utils.createCell(cellSize)
        self.cell64 = self.utils.createCell(cellSize)
        self.cell65 = self.utils.createCell(cellSize)
        self.cell66 = self.utils.createCell(cellSize)
        self.cell67 = self.utils.createCell(cellSize)
        self.cell68 = self.utils.createCell(cellSize)
        self.cell69 = self.utils.createCell(cellSize)
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
        self.cell71 = self.utils.createCell(cellSize)
        self.cell72 = self.utils.createCell(cellSize)
        self.cell73 = self.utils.createCell(cellSize)
        self.cell74 = self.utils.createCell(cellSize)
        self.cell75 = self.utils.createCell(cellSize)
        self.cell76 = self.utils.createCell(cellSize)
        self.cell77 = self.utils.createCell(cellSize)
        self.cell78 = self.utils.createCell(cellSize)
        self.cell79 = self.utils.createCell(cellSize)
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
        self.cell81 = self.utils.createCell(cellSize)
        self.cell82 = self.utils.createCell(cellSize)
        self.cell83 = self.utils.createCell(cellSize)
        self.cell84 = self.utils.createCell(cellSize)
        self.cell85 = self.utils.createCell(cellSize)
        self.cell86 = self.utils.createCell(cellSize)
        self.cell87 = self.utils.createCell(cellSize)
        self.cell88 = self.utils.createCell(cellSize)
        self.cell89 = self.utils.createCell(cellSize)
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
        self.cell91 = self.utils.createCell(cellSize)
        self.cell92 = self.utils.createCell(cellSize)
        self.cell93 = self.utils.createCell(cellSize)
        self.cell94 = self.utils.createCell(cellSize)
        self.cell95 = self.utils.createCell(cellSize)
        self.cell96 = self.utils.createCell(cellSize)
        self.cell97 = self.utils.createCell(cellSize)
        self.cell98 = self.utils.createCell(cellSize)
        self.cell99 = self.utils.createCell(cellSize)
        layout.addWidget(self.cell91, 9, 1)
        layout.addWidget(self.cell92, 9, 2) 
        layout.addWidget(self.cell93, 9, 3)    
        layout.addWidget(self.cell94, 9, 4)   
        layout.addWidget(self.cell95, 9, 5)
        layout.addWidget(self.cell96, 9, 6)
        layout.addWidget(self.cell97, 9, 7)
        layout.addWidget(self.cell98, 9, 8)
        layout.addWidget(self.cell99, 9, 9)


        button = QPushButton("Clear!")
        button.setCheckable(True)
        button.setFixedSize(cellSize, 50)
        layout.addWidget(button, 10, 2)
        button.clicked.connect(self.clearAll)

        button = QPushButton("Solve\nit!")
        button.setCheckable(True)
        button.setFixedSize(cellSize, 50)
        layout.addWidget(button, 10, 5)
        button.clicked.connect(self.the_button_was_clicked)

        button = QPushButton("Example\nFile!")
        button.setCheckable(True)
        button.setFixedSize(cellSize, 50)
        layout.addWidget(button, 10, 8)
        button.clicked.connect(self.add_test_file)

        # creting the widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def add_test_file(self):
        file = open("./model/exampleFile.dzn", "r")
        a = file.read()
        file.close()
        resList = self.utils.getResList(a)
        self.insertCell(resList)

    def the_button_was_clicked(self):
        string = self.create_string()
        # save the string in the file
        file = open('./model/data.dzn', 'w')
        file.write(string)
        file.close()

        # solving 
        res = subprocess.run(["minizinc", "./model/solver.mzn", "./model/data.dzn"], capture_output=True)
        if ("=====UNSATISFIABLE=====" in str(res.stdout)):
            dlg = CustomDialog()
            dlg.exec()
        else:
            resList = self.utils.getResList(str(res.stdout).split('\'')[1])
            self.insertCell(resList)
    
    
    def create_string(self):
        string = "pre = \n[| " + \
            self.cell11.currentText() + "," + \
            self.cell12.currentText() + "," + \
            self.cell13.currentText() + "," + \
            self.cell14.currentText() + "," + \
            self.cell15.currentText() + "," + \
            self.cell16.currentText() + "," + \
            self.cell17.currentText() + "," + \
            self.cell18.currentText() + "," + \
            self.cell19.currentText() + "\n| " + \
            \
            self.cell21.currentText() + "," + \
            self.cell22.currentText() + "," + \
            self.cell23.currentText() + "," + \
            self.cell24.currentText() + "," + \
            self.cell25.currentText() + "," + \
            self.cell26.currentText() + "," + \
            self.cell27.currentText() + "," + \
            self.cell28.currentText() + "," + \
            self.cell29.currentText() + "\n| " + \
            \
            self.cell31.currentText() + "," + \
            self.cell32.currentText() + "," + \
            self.cell33.currentText() + "," + \
            self.cell34.currentText() + "," + \
            self.cell35.currentText() + "," + \
            self.cell36.currentText() + "," + \
            self.cell37.currentText() + "," + \
            self.cell38.currentText() + "," + \
            self.cell39.currentText() + "\n| " + \
            \
            self.cell41.currentText() + "," + \
            self.cell42.currentText() + "," + \
            self.cell43.currentText() + "," + \
            self.cell44.currentText() + "," + \
            self.cell45.currentText() + "," + \
            self.cell46.currentText() + "," + \
            self.cell47.currentText() + "," + \
            self.cell48.currentText() + "," + \
            self.cell49.currentText() + "\n| " + \
            \
            self.cell51.currentText() + "," + \
            self.cell52.currentText() + "," + \
            self.cell53.currentText() + "," + \
            self.cell54.currentText() + "," + \
            self.cell55.currentText() + "," + \
            self.cell56.currentText() + "," + \
            self.cell57.currentText() + "," + \
            self.cell58.currentText() + "," + \
            self.cell59.currentText() + "\n| " + \
            \
            self.cell61.currentText() + "," + \
            self.cell62.currentText() + "," + \
            self.cell63.currentText() + "," + \
            self.cell64.currentText() + "," + \
            self.cell65.currentText() + "," + \
            self.cell66.currentText() + "," + \
            self.cell67.currentText() + "," + \
            self.cell68.currentText() + "," + \
            self.cell69.currentText() + "\n| " + \
            \
            self.cell71.currentText() + "," + \
            self.cell72.currentText() + "," + \
            self.cell73.currentText() + "," + \
            self.cell74.currentText() + "," + \
            self.cell75.currentText() + "," + \
            self.cell76.currentText() + "," + \
            self.cell77.currentText() + "," + \
            self.cell78.currentText() + "," + \
            self.cell79.currentText() + "\n| " + \
            \
            self.cell81.currentText() + "," + \
            self.cell82.currentText() + "," + \
            self.cell83.currentText() + "," + \
            self.cell84.currentText() + "," + \
            self.cell85.currentText() + "," + \
            self.cell86.currentText() + "," + \
            self.cell87.currentText() + "," + \
            self.cell88.currentText() + "," + \
            self.cell89.currentText() + "\n| " + \
            \
            self.cell91.currentText() + "," + \
            self.cell92.currentText() + "," + \
            self.cell93.currentText() + "," + \
            self.cell94.currentText() + "," + \
            self.cell95.currentText() + "," + \
            self.cell96.currentText() + "," + \
            self.cell97.currentText() + "," + \
            self.cell98.currentText() + "," + \
            self.cell99.currentText() + " |];"
        return string

    def insertCell(self, resList):
        self.cell11.setCurrentIndex(resList.pop(0))
        self.cell12.setCurrentIndex(resList.pop(0))
        self.cell13.setCurrentIndex(resList.pop(0))
        self.cell14.setCurrentIndex(resList.pop(0))
        self.cell15.setCurrentIndex(resList.pop(0))
        self.cell16.setCurrentIndex(resList.pop(0))
        self.cell17.setCurrentIndex(resList.pop(0))
        self.cell18.setCurrentIndex(resList.pop(0))
        self.cell19.setCurrentIndex(resList.pop(0))

        self.cell21.setCurrentIndex(resList.pop(0))
        self.cell22.setCurrentIndex(resList.pop(0))
        self.cell23.setCurrentIndex(resList.pop(0))
        self.cell24.setCurrentIndex(resList.pop(0))
        self.cell25.setCurrentIndex(resList.pop(0))
        self.cell26.setCurrentIndex(resList.pop(0))
        self.cell27.setCurrentIndex(resList.pop(0))
        self.cell28.setCurrentIndex(resList.pop(0))
        self.cell29.setCurrentIndex(resList.pop(0))

        self.cell31.setCurrentIndex(resList.pop(0))
        self.cell32.setCurrentIndex(resList.pop(0))
        self.cell33.setCurrentIndex(resList.pop(0))
        self.cell34.setCurrentIndex(resList.pop(0))
        self.cell35.setCurrentIndex(resList.pop(0))
        self.cell36.setCurrentIndex(resList.pop(0))
        self.cell37.setCurrentIndex(resList.pop(0))
        self.cell38.setCurrentIndex(resList.pop(0))
        self.cell39.setCurrentIndex(resList.pop(0))

        self.cell41.setCurrentIndex(resList.pop(0))
        self.cell42.setCurrentIndex(resList.pop(0))
        self.cell43.setCurrentIndex(resList.pop(0))
        self.cell44.setCurrentIndex(resList.pop(0))
        self.cell45.setCurrentIndex(resList.pop(0))
        self.cell46.setCurrentIndex(resList.pop(0))
        self.cell47.setCurrentIndex(resList.pop(0))
        self.cell48.setCurrentIndex(resList.pop(0))
        self.cell49.setCurrentIndex(resList.pop(0))

        self.cell51.setCurrentIndex(resList.pop(0))
        self.cell52.setCurrentIndex(resList.pop(0))
        self.cell53.setCurrentIndex(resList.pop(0))
        self.cell54.setCurrentIndex(resList.pop(0))
        self.cell55.setCurrentIndex(resList.pop(0))
        self.cell56.setCurrentIndex(resList.pop(0))
        self.cell57.setCurrentIndex(resList.pop(0))
        self.cell58.setCurrentIndex(resList.pop(0))
        self.cell59.setCurrentIndex(resList.pop(0))

        self.cell61.setCurrentIndex(resList.pop(0))
        self.cell62.setCurrentIndex(resList.pop(0))
        self.cell63.setCurrentIndex(resList.pop(0))
        self.cell64.setCurrentIndex(resList.pop(0))
        self.cell65.setCurrentIndex(resList.pop(0))
        self.cell66.setCurrentIndex(resList.pop(0))
        self.cell67.setCurrentIndex(resList.pop(0))
        self.cell68.setCurrentIndex(resList.pop(0))
        self.cell69.setCurrentIndex(resList.pop(0))

        self.cell71.setCurrentIndex(resList.pop(0))
        self.cell72.setCurrentIndex(resList.pop(0))
        self.cell73.setCurrentIndex(resList.pop(0))
        self.cell74.setCurrentIndex(resList.pop(0))
        self.cell75.setCurrentIndex(resList.pop(0))
        self.cell76.setCurrentIndex(resList.pop(0))
        self.cell77.setCurrentIndex(resList.pop(0))
        self.cell78.setCurrentIndex(resList.pop(0))
        self.cell79.setCurrentIndex(resList.pop(0))

        self.cell81.setCurrentIndex(resList.pop(0))
        self.cell82.setCurrentIndex(resList.pop(0))
        self.cell83.setCurrentIndex(resList.pop(0))
        self.cell84.setCurrentIndex(resList.pop(0))
        self.cell85.setCurrentIndex(resList.pop(0))
        self.cell86.setCurrentIndex(resList.pop(0))
        self.cell87.setCurrentIndex(resList.pop(0))
        self.cell88.setCurrentIndex(resList.pop(0))
        self.cell89.setCurrentIndex(resList.pop(0))

        self.cell91.setCurrentIndex(resList.pop(0))
        self.cell92.setCurrentIndex(resList.pop(0))
        self.cell93.setCurrentIndex(resList.pop(0))
        self.cell94.setCurrentIndex(resList.pop(0))
        self.cell95.setCurrentIndex(resList.pop(0))
        self.cell96.setCurrentIndex(resList.pop(0))
        self.cell97.setCurrentIndex(resList.pop(0))
        self.cell98.setCurrentIndex(resList.pop(0))
        self.cell99.setCurrentIndex(resList.pop(0))

    def clearAll(self):
        self.cell11.setCurrentIndex(0)
        self.cell12.setCurrentIndex(0)
        self.cell13.setCurrentIndex(0)
        self.cell14.setCurrentIndex(0)
        self.cell15.setCurrentIndex(0)
        self.cell16.setCurrentIndex(0)
        self.cell17.setCurrentIndex(0)
        self.cell18.setCurrentIndex(0)
        self.cell19.setCurrentIndex(0)

        self.cell21.setCurrentIndex(0)
        self.cell22.setCurrentIndex(0)
        self.cell23.setCurrentIndex(0)
        self.cell24.setCurrentIndex(0)
        self.cell25.setCurrentIndex(0)
        self.cell26.setCurrentIndex(0)
        self.cell27.setCurrentIndex(0)
        self.cell28.setCurrentIndex(0)
        self.cell29.setCurrentIndex(0)

        self.cell31.setCurrentIndex(0)
        self.cell32.setCurrentIndex(0)
        self.cell33.setCurrentIndex(0)
        self.cell34.setCurrentIndex(0)
        self.cell35.setCurrentIndex(0)
        self.cell36.setCurrentIndex(0)
        self.cell37.setCurrentIndex(0)
        self.cell38.setCurrentIndex(0)
        self.cell39.setCurrentIndex(0)

        self.cell41.setCurrentIndex(0)
        self.cell42.setCurrentIndex(0)
        self.cell43.setCurrentIndex(0)
        self.cell44.setCurrentIndex(0)
        self.cell45.setCurrentIndex(0)
        self.cell46.setCurrentIndex(0)
        self.cell47.setCurrentIndex(0)
        self.cell48.setCurrentIndex(0)
        self.cell49.setCurrentIndex(0)

        self.cell51.setCurrentIndex(0)
        self.cell52.setCurrentIndex(0)
        self.cell53.setCurrentIndex(0)
        self.cell54.setCurrentIndex(0)
        self.cell55.setCurrentIndex(0)
        self.cell56.setCurrentIndex(0)
        self.cell57.setCurrentIndex(0)
        self.cell58.setCurrentIndex(0)
        self.cell59.setCurrentIndex(0)

        self.cell61.setCurrentIndex(0)
        self.cell62.setCurrentIndex(0)
        self.cell63.setCurrentIndex(0)
        self.cell64.setCurrentIndex(0)
        self.cell65.setCurrentIndex(0)
        self.cell66.setCurrentIndex(0)
        self.cell67.setCurrentIndex(0)
        self.cell68.setCurrentIndex(0)
        self.cell69.setCurrentIndex(0)

        self.cell71.setCurrentIndex(0)
        self.cell72.setCurrentIndex(0)
        self.cell73.setCurrentIndex(0)
        self.cell74.setCurrentIndex(0)
        self.cell75.setCurrentIndex(0)
        self.cell76.setCurrentIndex(0)
        self.cell77.setCurrentIndex(0)
        self.cell78.setCurrentIndex(0)
        self.cell79.setCurrentIndex(0)

        self.cell81.setCurrentIndex(0)
        self.cell82.setCurrentIndex(0)
        self.cell83.setCurrentIndex(0)
        self.cell84.setCurrentIndex(0)
        self.cell85.setCurrentIndex(0)
        self.cell86.setCurrentIndex(0)
        self.cell87.setCurrentIndex(0)
        self.cell88.setCurrentIndex(0)
        self.cell89.setCurrentIndex(0)

        self.cell91.setCurrentIndex(0)
        self.cell92.setCurrentIndex(0)
        self.cell93.setCurrentIndex(0)
        self.cell94.setCurrentIndex(0)
        self.cell95.setCurrentIndex(0)
        self.cell96.setCurrentIndex(0)
        self.cell97.setCurrentIndex(0)
        self.cell98.setCurrentIndex(0)
        self.cell99.setCurrentIndex(0)
