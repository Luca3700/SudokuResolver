from PyQt5.QtWidgets import QComboBox


class Utils():
    def __init__(self):
        super().__init__()

    def getResList(self, res):
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
    
    
    def createCell(self, size):
        # crete che combobox
        items = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        cell = QComboBox()
        cell.addItems(items)
        cell.setCurrentIndex(0)
        cell.setFixedSize(size, size)
        return cell
    
    def insertCell(self, cells, resList, data):
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