from PyQt6.QtWidgets import *
from PyQt6 import uic
from controller import Controller


class View(QMainWindow):
    lResult: QLabel

    cbOperator: QComboBox
    sbOperand1: QSpinBox
    sbOperand2: QSpinBox

    bReset: QPushButton
    bRun: QPushButton
    bExit: QPushButton

    statusbar: QStatusBar

    def __init__(self, c: Controller):
        super().__init__()

        uic.loadUi("view.ui", self)
        self.cbOperator.addItems(["+", "-", "*", "/"])
        self.bRun.clicked.connect(c.execute)
        self.bReset.clicked.connect(c.reset)

    def reset(self) -> None:
        self.cbOperator.setCurrentIndex(0)

        self.sbOperand1.setValue(0)
        self.sbOperand2.setValue(0)
        self.lResult.setText("Noch kein Ergebnis")
        self.set_text_statusbar(
            "Bitte zwei Werte für die Operanden eingeben."
            "Einen Operator auswählen und mit Ausführen "
            "berechnen lassen.")

    def set_ergebnis(self, t: str) -> None:
        self.lResult.setText(t)

    def set_text_statusbar(self, t: str) -> None:
        self.statusbar.showMessage(t)

    def get_op1(self) -> int:
        return self.sbOperand1.value()

    def get_op2(self) -> int:
        return self.sbOperand2.value()

    def get_operator(self) -> str:
        return self.cbOperator.currentText()
