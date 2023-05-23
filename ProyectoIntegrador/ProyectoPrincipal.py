import sys

import serial as controlador

from PyQt5 import uic, QtWidgets
qtCreatorFile = "Principal.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals

        # Conecta el botón "btn_accion" al método "accion" cuando se hace clic
        self.btn_accion.clicked.connect(self.accion)

        # Conecta cada botón "btn_focoX" a los métodos "control_focoX" correspondientes cuando se hace clic
        self.btn_foco1.clicked.connect(self.control_foco1)
        self.btn_foco2.clicked.connect(self.control_foco2)
        self.btn_foco3.clicked.connect(self.control_foco3)
        self.btn_foco4.clicked.connect(self.control_foco4)

        # Configura los rangos y valores iniciales de los diales de foco 5, 6 y 7
        self.dial_foco5.setMinimum(0)
        self.dial_foco5.setMaximum(255)
        self.dial_foco5.setSingleStep(1)
        self.dial_foco5.setValue(0)
        self.dial_foco5.valueChanged.connect(self.control_foco5)

        self.dial_foco6.setMinimum(0)
        self.dial_foco6.setMaximum(255)
        self.dial_foco6.setSingleStep(1)
        self.dial_foco6.setValue(0)
        self.dial_foco6.valueChanged.connect(self.control_foco6)

        self.dial_foco7.setMinimum(0)
        self.dial_foco7.setMaximum(255)
        self.dial_foco7.setSingleStep(1)
        self.dial_foco7.setValue(0)
        self.dial_foco7.valueChanged.connect(self.control_foco7)

        # Variables para almacenar el estado de los focos
        self.foco1 = 0
        self.foco2 = 0
        self.foco3 = 0
        self.foco4 = 0
        self.foco5 = 0
        self.foco6 = 0
        self.foco7 = 0

        self.arduino = None

        # Deshabilita la edición del campo de texto "txt_estado"
        self.txt_estado.setEnabled(False)

    # Área de los Slots

    # Slot para el botón "btn_accion"
    def accion(self):
        # Si el objeto Arduino no está inicializado
        if self.arduino == None:
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("CONECTADO")
            # Inicializa el objeto Arduino
            self.arduino = controlador.Serial("/dev/cu.usbmodem101", baudrate=9600, timeout=1)
        # Si el puerto está abierto
        elif self.arduino.isOpen():
            self.btn_accion.setText("RECONECTAR")
            self.txt_estado.setText("DESCONECTADO")
            # Cierra el puerto
            self.arduino.close()
        # Si el puerto está cerrado
        else:
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("RECONECTADO")
            # Abre el puerto
            self.arduino.open()

    # Método para generar la cadena de control de los focos
    def generaCadenaControlFocos(self):
        cadena = str(self.foco1) + "-" + str(self.foco2) + "-" + \
                 str(self.foco3) + "-" + str(self.foco4) + "-" + \
                 str(self.foco5) + "-" + str(self.foco6) + "-" + str(self.foco7)
        print(cadena)

    # Métodos para controlar el estado de cada foco
    def control_foco1(self):
        txtBoton = self.btn_foco1.text()
        if txtBoton == "PRENDER":
            self.btn_foco1.setText("APAGAR")
            self.foco1 = 1
        else:
            self.btn_foco1.setText("PRENDER")
            self.foco1 = 0
        self.generaCadenaControlFocos()

    def control_foco2(self):
        txtBoton = self.btn_foco2.text()
        if txtBoton == "PRENDER":
            self.btn_foco2.setText("APAGAR")
            self.foco2 = 1
        else:
            self.btn_foco2.setText("PRENDER")
            self.foco2 = 0
        self.generaCadenaControlFocos()

    def control_foco3(self):
        txtBoton = self.btn_foco3.text()
        if txtBoton == "PRENDER":
            self.btn_foco3.setText("APAGAR")
            self.foco3 = 1
        else:
            self.btn_foco3.setText("PRENDER")
            self.foco3 = 0
        self.generaCadenaControlFocos()

    def control_foco4(self):
        txtBoton = self.btn_foco4.text()
        if txtBoton == "PRENDER":
            self.btn_foco4.setText("APAGAR")
            self.foco4 = 1
        else:
            self.btn_foco4.setText("PRENDER")
            self.foco4 = 0
        self.generaCadenaControlFocos()

    def control_foco5(self):
        self.foco5 = self.dial_foco5.value()
        self.generaCadenaControlFocos()

    def control_foco6(self):
        self.foco6 = self.dial_foco6.value()
        self.generaCadenaControlFocos()

    def control_foco7(self):
        self.foco7 = self.dial_foco7.value()
        self.generaCadenaControlFocos()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
