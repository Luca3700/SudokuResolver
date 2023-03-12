from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDir
import subprocess
from gui.customDialog import *
from gui.utils import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # importing utils file
        self.utils = Utils()

        self.setWindowTitle("Sudoku Solver")
        # setting app icon (source: https://www.flaticon.com/free-icon/sudoku_5732078?term=sudoku&page=1&position=7&origin=tag&related_id=5732078)
        self.setWindowIcon(QIcon(QDir.currentPath() + '/gui/icons/sudoku.png'))
        self.resize(900,900)

        # to creating the cells layout
        layout = QGridLayout() 
        cellSize = 80

        # label used to create padding between the macro cells
        label = QLabel()
        label.setFixedSize(10,10)

        # defining the cells
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
        layout.addWidget(label, 1, 4)   
        layout.addWidget(self.cell14, 1, 5)   
        layout.addWidget(self.cell15, 1, 6)
        layout.addWidget(self.cell16, 1, 7)
        layout.addWidget(label, 1, 8) 
        layout.addWidget(self.cell17, 1, 9)
        layout.addWidget(self.cell18, 1, 10)
        layout.addWidget(self.cell19, 1, 11)

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
        layout.addWidget(label, 2, 4)     
        layout.addWidget(self.cell24, 2, 5)   
        layout.addWidget(self.cell25, 2, 6)
        layout.addWidget(self.cell26, 2, 7)
        layout.addWidget(label, 2, 8) 
        layout.addWidget(self.cell27, 2, 9)
        layout.addWidget(self.cell28, 2, 10)
        layout.addWidget(self.cell29, 2, 11)

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
        layout.addWidget(label, 3, 4)     
        layout.addWidget(self.cell34, 3, 5)   
        layout.addWidget(self.cell35, 3, 6)
        layout.addWidget(self.cell36, 3, 7)
        layout.addWidget(label, 3, 8) 
        layout.addWidget(self.cell37, 3, 9)
        layout.addWidget(self.cell38, 3, 10)
        layout.addWidget(self.cell39, 3, 11)

        #padding
        layout.addWidget(label, 4, 5) 

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
        layout.addWidget(self.cell41, 5, 1)
        layout.addWidget(self.cell42, 5, 2) 
        layout.addWidget(self.cell43, 5, 3) 
        layout.addWidget(label, 5, 4)    
        layout.addWidget(self.cell44, 5, 5)   
        layout.addWidget(self.cell45, 5, 6)
        layout.addWidget(self.cell46, 5, 7)
        layout.addWidget(label, 5, 8) 
        layout.addWidget(self.cell47, 5, 9)
        layout.addWidget(self.cell48, 5, 10)
        layout.addWidget(self.cell49, 5, 11)

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
        layout.addWidget(self.cell51, 6, 1)
        layout.addWidget(self.cell52, 6, 2) 
        layout.addWidget(self.cell53, 6, 3)  
        layout.addWidget(label, 6, 4)   
        layout.addWidget(self.cell54, 6, 5)   
        layout.addWidget(self.cell55, 6, 6)
        layout.addWidget(self.cell56, 6, 7)
        layout.addWidget(label, 6, 8) 
        layout.addWidget(self.cell57, 6, 9)
        layout.addWidget(self.cell58, 6, 10)
        layout.addWidget(self.cell59, 6, 11)

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
        layout.addWidget(self.cell61, 7, 1)
        layout.addWidget(self.cell62, 7, 2) 
        layout.addWidget(self.cell63, 7, 3) 
        layout.addWidget(label, 7, 4)    
        layout.addWidget(self.cell64, 7, 5)   
        layout.addWidget(self.cell65, 7, 6)
        layout.addWidget(self.cell66, 7, 7)
        layout.addWidget(label, 7, 8) 
        layout.addWidget(self.cell67, 7, 9)
        layout.addWidget(self.cell68, 7, 10)
        layout.addWidget(self.cell69, 7, 11)

        #padding
        layout.addWidget(label, 8, 5)

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
        layout.addWidget(self.cell71, 9, 1)
        layout.addWidget(self.cell72, 9, 2) 
        layout.addWidget(self.cell73, 9, 3)  
        layout.addWidget(label, 9, 4)   
        layout.addWidget(self.cell74, 9, 5)   
        layout.addWidget(self.cell75, 9, 6)
        layout.addWidget(self.cell76, 9, 7)
        layout.addWidget(label, 9, 8) 
        layout.addWidget(self.cell77, 9, 9)
        layout.addWidget(self.cell78, 9, 10)
        layout.addWidget(self.cell79, 9, 11)

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
        layout.addWidget(self.cell81, 10, 1)
        layout.addWidget(self.cell82, 10, 2) 
        layout.addWidget(self.cell83, 10, 3) 
        layout.addWidget(label, 10, 4)    
        layout.addWidget(self.cell84, 10, 5)   
        layout.addWidget(self.cell85, 10, 6)
        layout.addWidget(self.cell86, 10, 7)
        layout.addWidget(label, 10, 8) 
        layout.addWidget(self.cell87, 10, 9)
        layout.addWidget(self.cell88, 10, 10)
        layout.addWidget(self.cell89, 10, 11)

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
        layout.addWidget(self.cell91, 11, 1)
        layout.addWidget(self.cell92, 11, 2) 
        layout.addWidget(self.cell93, 11, 3) 
        layout.addWidget(label, 11, 4)    
        layout.addWidget(self.cell94, 11, 5)   
        layout.addWidget(self.cell95, 11, 6)
        layout.addWidget(self.cell96, 11, 7)
        layout.addWidget(label, 11, 8) 
        layout.addWidget(self.cell97, 11, 9)
        layout.addWidget(self.cell98, 11, 10)
        layout.addWidget(self.cell99, 11, 11)

        # list containing all the cells
        self.cells = [self.cell11, self.cell12, self.cell13, self.cell14, self.cell15, self.cell16, self.cell17, self.cell18, self.cell19, \
                      self.cell21, self.cell22, self.cell23, self.cell24, self.cell25, self.cell26, self.cell27, self.cell28, self.cell29, \
                        self.cell31, self.cell32, self.cell33, self.cell34, self.cell35, self.cell36, self.cell37, self.cell38, self.cell39, \
                            self.cell41, self.cell42, self.cell43, self.cell44, self.cell45, self.cell46, self.cell47, self.cell48, self.cell49, \
                                self.cell51, self.cell52, self.cell53, self.cell54, self.cell55, self.cell56, self.cell57, self.cell58, self.cell59, \
                                    self.cell61, self.cell62, self.cell63, self.cell64, self.cell65, self.cell66, self.cell67, self.cell68, self.cell69, \
                                        self.cell71, self.cell72, self.cell73, self.cell74, self.cell75, self.cell76, self.cell77, self.cell78, self.cell79, \
                                            self.cell81, self.cell82, self.cell83, self.cell84, self.cell85, self.cell86, self.cell87, self.cell88, self.cell89, \
                                                self.cell91, self.cell92, self.cell93, self.cell94, self.cell95, self.cell96, self.cell97, self.cell98, self.cell99]

        # defining buttons
        button = QPushButton("Clear!")
        button.setCheckable(True)
        button.setFixedSize(cellSize, 50)
        layout.addWidget(button, 12, 3)
        button.clicked.connect(self.clearAll)

        button = QPushButton("Solve\nit!")
        button.setCheckable(True)
        button.setFixedSize(cellSize, 50)
        layout.addWidget(button, 12, 6)
        button.clicked.connect(self.the_button_was_clicked)

        # button to load the example sudoku
        button = QPushButton("Load\nmodel")
        button.setCheckable(True)
        button.setFixedSize(cellSize, 50)
        layout.addWidget(button, 12, 9)
        button.clicked.connect(self.add_test_file)

        # creting the widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    # action of the "Clear" button
    def clearAll(self):
        self.utils.clearAll(self.cells)

    # action of the "Load model" button
    def add_test_file(self):
        file = open("./model/exampleFile.dzn", "r")
        a = file.read()
        file.close()
        resList = self.utils.getResList(a)
        #self.insertCell(resList)
        self.utils.add_test_file(self.cells, resList)

    # action of the "Solve it!" button
    def the_button_was_clicked(self):
        string = self.utils.create_string(self.cells)
        # save the string in the file
        file = open('./model/data.dzn', 'w')
        file.write(string)
        file.close()

        # solving 
        res = subprocess.run(["minizinc", "./model/solver.mzn", "./model/data.dzn"], capture_output=True)
        if ("=====UNSATISFIABLE=====" in str(res.stdout)):
            # popup that shows that the sudoku is not solvable
            dlg = CustomDialog()
            dlg.exec()
        else:
            resList = self.utils.getResList(str(res.stdout).split('\'')[1])
            # inserting the results
            self.utils.insertInTheCell(self.cells, resList, string)

