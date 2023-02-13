import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_03_SaludarA.ui" #nombre del archivo aqui.
Ui_MainWindow, QtBaseCLass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.btn_saludar.clicked.connect(self.saludar)

    # Area de los Slots
    def saludar(self):
        n = self.txt_nombre.text()
        self.mensaje("Hola! " + n + " saludos!😊")

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
