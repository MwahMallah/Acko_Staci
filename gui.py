from PyQt6.QtCore import Qt 

from PyQt6.QtWidgets import QApplication, QPushButton, QLineEdit, QMainWindow, QVBoxLayout, QGridLayout, QWidget


WINDOW_WIDTH = 330
WINDOW_HEIGHT = 300

DISPLAY_HEIGHT = 35

BUTTON_SIZE = 40


class Display(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setFixedHeight(DISPLAY_HEIGHT)

class Buttons(QWidget):
    def __init__(self):
        super().__init__()        
        layout = QGridLayout()
        keyboard = [["7", "8", "9", "/", "C"],
        ["4", "5", "6", "*", "("],
        ["1", "2", "3", "-", ")"],
        ["0", "00", ".", "+", "="]]

        self.keymap = {}

        for row, key in enumerate(keyboard):
            for column, btn in enumerate(key):
                self.keymap[btn] = QPushButton(btn)
                self.keymap[btn].setFixedSize(int(BUTTON_SIZE*1.5), BUTTON_SIZE)
                layout.addWidget(self.keymap[btn], row, column)

        self.setLayout(layout)


class CalculatorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        centralWidget = QWidget(self)

        layout =  QVBoxLayout()
        self.display = Display()
        self.buttons = Buttons()
        layout.addWidget(self.display)
        layout.addWidget(self.buttons)

        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)

    def setDisplayLine(self, text):
        self.display.setText(text)

    def deleteDisplayLine(self):
        self.setDisplayLine("")

    def getDisplayLine(self):
        return self.display.text()



