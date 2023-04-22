import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_07_ProgressBar.ui" #nombre del archivo aqui.
Ui_MainWindow, QtBaseCLass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)

        self.progressBar.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("o")

        import time as t

        for i in range(100):
            self.progressBar.setValue(i)
            t.sleep(0.1)

        # Area de los Slots
    def cambiaValor(self):
        self.txt_valor.setText(str(self.progressBar.value()))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
