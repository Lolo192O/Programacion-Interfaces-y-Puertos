import sys

from PyQt5 import uic, QtWidgets

from UI_to_Python import Second_EnvioInfo as second

class MyDialog(QtWidgets.QDialog, second.Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        second.Ui_Dialog.__init__(self)
        self.setupUi(self)
        # Area de los Signals

        # Area de los Slots