import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_05_HorizontalSlider.ui" #nombre del archivo aqui.
Ui_MainWindow, QtBaseCLass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.horizontalSlider.setMinimum(-10)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)

        self.horizontalSlider.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("o")

        # Area de los Slots
    def cambiaValor(self):
        self.txt_valor.setText(str(self.horizontalSlider.value()))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
