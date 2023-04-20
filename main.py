from gui import CalculatorUI
from PyQt6.QtWidgets import QApplication
import sys


class Calculator():
    def __init__(self, gui, logic):
        self.gui = gui
        self.logic = logic


if __name__ == "__main__":
    app = QApplication([])

    window = CalculatorUI()
    calc = Calculator(gui=window, logic=)
    window.show()

    sys.exit(app.exec())