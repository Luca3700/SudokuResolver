from PyQt5.QtWidgets import QComboBox


class Utils():
    def __init__(self):
        super().__init__()

    def createCell(self, size):
        # crete che combobox
        items = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        cell = QComboBox()
        cell.addItems(items)
        cell.setCurrentIndex(0)
        cell.setFixedSize(size, size)
        return cell

    def create_string(self, cells):
        # create the string that will be printed in the data.dzn file
        # that will be used from minizinc to get the cell inserted from the user
        string = "pre = \n[| "
        for i in range(81):
            string = string + cells[i].currentText()
            if i == 80:
                string = string + "\n|];"
            elif ((i+1) % 9 == 0):
                string = string + "\n| "
            else:
                string = string + ", "
        return string

    def getResList(self, res):
        # method used to parse the result of minizinc into a list of numbers
        # see exampleFile.dzn to see an example of output
        resList = []
        a1 = res.split('=')[1]
        a1 = a1.split(';')[0]
        a1 = a1.split('[')[1]
        a1 = a1.split(']')[0]
        blocks = a1.strip().split('|')
        
        for i in range(1,10):
            b = blocks[i].split(' ')
            for j in range(1,9):
                resList.append(int(b[j].split(',')[0]))
            resList.append(int(b[9].split('\\')[0]))
        
        return resList
    
    def insertInTheCell(self, cells, resList, data):
        # insert in the cells the numbers of resList
        dataList = self.getResList(data)
        for cell in cells:
            number1 = resList.pop(0)
            number2 = dataList.pop(0)
            if number2 == 0:
                cell.setCurrentIndex(int(number1))
                cell.setStyleSheet("QComboBox"
                                     "{"
                                     "border : 2px black;"
                                     "border-style : dashed;"
                                     "}")
                
    def clearAll(self, cells):
        # clear all the cells
        for cell in cells:
            cell.setCurrentIndex(0)
            cell.setStyleSheet("QComboBox"
                        "{"
                        "border : 1px black;"
                        "border-style : none;"
                        "}")   

    def add_test_file(self, cells, resList):
        # insert in the cells the numbers in exampleFile.dzn
        for i in range(len(resList)):
            cells[i].setCurrentIndex(resList[i])
            if resList[i] == 0:
                cells[i].setStyleSheet("QComboBox"
                        "{"
                        "border : 1px black;"
                        "border-style : none;"
                        "}")
            else:
                cells[i].setStyleSheet("QComboBox"
                        "{"
                        "border : 1px black;"
                        "border-style : solid;"
                        "}")
