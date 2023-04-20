from gui import CalculatorUI
from PyQt6.QtWidgets import QApplication
from calculator_logic import Calc
import sys
from functools import partial

ERROR_MSG = "#ERROR"

class Calculator():
    def __init__(self, gui, logic):
        self.gui = gui
        self.logic = logic
        self._connectSignalsAndSlots()

    def _buildExpression(self, symbol):
        line = self.gui.getDisplayLine()
        if line == ERROR_MSG:
            self.gui.deleteDisplayLine()
            line = ""

        line = line + symbol
        self.gui.setDisplayLine(line)
        
    def _calculateResult(self):
        try:
            line = self.gui.getDisplayLine()
            result = self.logic.eval(line)

        except Exception:
            result = ERROR_MSG

        self.gui.setDisplayLine(result)


    def _connectSignalsAndSlots(self):
        self.gui.buttons.keymap["C"].clicked.connect(self.gui.deleteDisplayLine)
        self.gui.buttons.keymap["="].clicked.connect(self._calculateResult)

        for keySymbol, btn in self.gui.buttons.keymap.items():
            if keySymbol not in {"C", "="}:
                self.gui.buttons.keymap[keySymbol].clicked.connect(partial(self._buildExpression, keySymbol))
        


if __name__ == "__main__":
    app = QApplication([])

    window = CalculatorUI()
    calculator_logic = Calc()
    calculator = Calculator(gui=window, logic=calculator_logic)
    window.show()

    sys.exit(app.exec())