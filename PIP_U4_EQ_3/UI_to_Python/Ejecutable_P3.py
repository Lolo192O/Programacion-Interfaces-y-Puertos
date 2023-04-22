import sys
from PyQt5 import uic, QtWidgets

from UI_to_Python import P3_Ejemplo as interfaz

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.btn_mensaje.clicked.connect(self.saludar)

    # Area de los Slots
    def saludar(self):
        self.mensaje("Hola!, saludos!😊")

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
