import sys
from PyQt5 import uic, QtWidgets, QtCore

from UI_to_Python import P2_Ejemplo as interfaz

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.btn_sumar.clicked.connect(self.sumar)

    # Area de los Slots
    def sumar(self):
        a = int(self.txt_A.text())
        b = int(self.txt_B.text())
        r = a+b
        self.txt_resultado.setText(str(r))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
