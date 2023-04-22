import sys
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "P_12_DatosImagenes.ui" #nombre del archivo aqui.
Ui_MainWindow, QtBaseCLass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
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

        import Modulo_Contactos as contactos
        self.contacts = contactos.cargarContactos()
        print()

        self.obtieneDatosContacto(0)

        # Area de los Slots
    def cambiaImagen(self):
        indice = self.slider_img.value()

        imagen = self.listaImgs[indice]
        self.txt_valorA.setText(imagen[0])
        self.img.setPixmap(QtGui.QPixmap(imagen[1]))

        self.obtieneDatosContacto(indice)

    def obtieneDatosContacto(self, indice):

        datosContacto = self.contacts[indice]
        self.txt_nombre.setText(datosContacto[0])
        self.txt_carrera.setText(datosContacto[1])
        self.txt_edad.setText(datosContacto[2])


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
