import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_05_PromedioAlumnos.ui" #nombre del archivo aqui.
Ui_MainWindow, QtBaseCLass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_calcular.clicked.connect(self.calcular)

        self.calificaciones = [] #lista vacia

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
