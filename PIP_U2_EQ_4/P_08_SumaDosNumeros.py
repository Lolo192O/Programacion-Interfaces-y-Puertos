import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_08_SumaDosNumeros.ui" #nombre del archivo aqui.
Ui_MainWindow, QtBaseCLass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.slider_A.setMinimum(0)
        self.slider_A.setMaximum(100)
        self.slider_A.setSingleStep(1)
        self.slider_A.setValue(0)

        self.slider_B.setMinimum(0)
        self.slider_B.setMaximum(100)
        self.slider_B.setSingleStep(1)
        self.slider_B.setValue(0)

        self.slider_A.valueChanged.connect(self.cambiaValorA)
        self.slider_B.valueChanged.connect(self.cambiaValorB)

        self.txt_valorA.setText("o")
        self.txt_valorB.setText("o")

        # Area de los Slots
    def cambiaValorA(self):
        self.txt_valorA.setText(str(self.slider_A.value()))
        self.realizarSuma()

    def cambiaValorB(self):
        self.txt_valorB.setText(str(self.slider_B.value()))
        self.realizarSuma()

    def realizarSuma(self):
        a = self.slider_A.value()
        b = self.slider_B.value()
        self.txt_resultado.setText(str(a+b))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
