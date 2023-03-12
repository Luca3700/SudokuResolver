from PyQt5.QtWidgets import QComboBox
import darkdetect

class customComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        try:
            self.isDark = darkdetect.isDark()
        except:
            self.isDark = False

        items = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.addItems(items)
        self.setCurrentIndex(0)
        self.currentIndexChanged.connect(self.indexChanged)

    def indexChanged(self, index):
        if index == 0:
            if self.isDark:
                self.setStyleSheet("QComboBox"
                        "{"
                        "border : 1px white;"
                        "border-style : none;"
                        "}")
            else:
                self.setStyleSheet("QComboBox"
                        "{"
                        "border : 1px black;"
                        "border-style : none;"
                        "}")
        else:
            if self.isDark:
                self.setStyleSheet("QComboBox"
                        "{"
                        "border : 1px white;"
                        "border-style : none;"
                        "}")
            else: 
                self.setStyleSheet("QComboBox"
                        "{"
                        "border : 1px black;"
                        "border-style : solid;"
                        "}")
    