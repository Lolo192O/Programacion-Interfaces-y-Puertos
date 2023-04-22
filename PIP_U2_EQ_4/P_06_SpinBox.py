import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_06_SpinBox.ui" #nombre del archivo aqui.
Ui_MainWindow, QtBaseCLass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.spinBox.setMinimum(-10)
        self.spinBox.setMaximum(10)
        self.spinBox.setSingleStep(1)
        self.spinBox.setValue(0)

        self.spinBox.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("o")

        # Area de los Slots
    def cambiaValor(self):
        self.txt_valor.setText(str(self.spinBox.value()))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
