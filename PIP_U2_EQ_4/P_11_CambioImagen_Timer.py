import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "P_11_CambioImagen_Timer.ui" #nombre del archivo aqui.
Ui_MainWindow, QtBaseCLass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.slider_imagenes)

        self.slider_img.setMinimum(0)
        self.slider_img.setMaximum(4)
        self.slider_img.setSingleStep(0)
        self.slider_img.setValue(0)


        self.slider_img.valueChanged.connect(self.cambiaImagen)

        self.listaImgs = []
        self.listaImgs.append(["Numero 1", ":/prefijoNuevo/Capturadepantalla(13).png"])
        self.listaImgs.append(["Numero 2", ":/prefijoNuevo/Capturadepantalla(16).png"])
        self.listaImgs.append(["Numero 3", ":/prefijoNuevo/Capturadepantalla(17).png"])
        self.listaImgs.append(["Numero 4", ":/prefijoNuevo/Capturadepantalla(4).png"])
        self.listaImgs.append(["Numero 5", ":/prefijoNuevo/Capturadepantalla(6).png"])

        self.txt_valorA.setText("Numero 1")

        self.IndexImagen = 0

        self.segundoPlano.start(250)

        # Area de los Slots
    def slider_imagenes(self):
        self.slider_img.setValue(self.IndexImagen)
        self.IndexImagen = (self.IndexImagen+1)%5

    def cambiaImagen(self):
        imagen = self.listaImgs[self.slider_img.value()]
        self.txt_valorA.setText(imagen[0])
        self.img.setPixmap(QtGui.QPixmap(imagen[1]))


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
