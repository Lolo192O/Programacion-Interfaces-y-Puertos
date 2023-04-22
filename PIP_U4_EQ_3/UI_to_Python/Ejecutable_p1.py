import sys
from PyQt5 import uic, QtWidgets, QtCore

from UI_to_Python import P1_Ejemplo as interfaz

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_calcular.clicked.connect(self.calcular)

        self.calificaciones = []

    # Area de los Slots
    def agregar(self):
        num = float(self.txt_calificacion.text())
        self.calificaciones.append(num)
        print(self.calificaciones)

    def calcular(self):
        prom = sum(self.calificaciones) / len(self.calificaciones)
        print(prom)
        self.txt_promedio.setText(str(prom))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
