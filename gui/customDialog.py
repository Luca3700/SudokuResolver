from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel

"source https://www.pythonguis.com/tutorials/pyqt-dialogs/"
class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Error")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("This sudoku is not solvable")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        