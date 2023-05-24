import sys

import serial as controlador

from statistics import median

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Principal.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los SignalsSS
        self.btn_accion.clicked.connect(self.accion)

        self.btn_foco1.clicked.connect(self.control_foco1)
        self.btn_foco2.clicked.connect(self.control_foco2)
        self.btn_foco3.clicked.connect(self.control_foco3)
        self.btn_foco4.clicked.connect(self.control_foco4)

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

        self.foco1 = 0
        self.foco2 = 0
        self.foco3 = 0
        self.foco4 = 0
        self.foco5 = 0
        self.foco6 = 0
        self.foco7 = 0

        self.arduino = None

        # ACTUALIZACION .... VIERNES 19 DE MAYO

        self.txt_estado.setEnabled(False)
        self.txt_com.setText("/dev/cu.usbmodem101")

        # self.btn_accion.setFocus()
        # or ...
        self.txt_com.selectAll()
        self.txt_com.setFocus()

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lectura_datos_arduino)

        #agrega datos al combobox
        self.cb_potenciometros.addItem("Sensor 1", 10)
        self.cb_potenciometros.addItem("Sensor 2", 12)
        self.cb_potenciometros.addItem("Sensor 3", 16)
        self.cb_potenciometros.currentIndexChanged.connect(self.cambiaComboBoxSeleleccion)

        # datos leidos de los sensores ---z igual se podria agregar a : min, max, promedio, mediana
        self.datos_sensores = {10: [],  # sensor 1
                               12: [],  # sensor 2
                               16: []}  # sensor 3

        # Área de los Slots

    def accion(self):
        com = self.txt_com.text()

        if self.arduino == None:
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("CONECTADO")
            ##establece la conexion con arduino la primera vez  ## COM5
            self.arduino = controlador.Serial(com, baudrate=9600, timeout=1)
            self.segundoPlano.start(100)
        elif self.arduino.isOpen():  # Si das clic y esta abierta la conexion, entonces se pasa a desconectar
            self.btn_accion.setText("RECONECTAR")
            self.txt_estado.setText("DESCONECTADO")
            self.segundoPlano.stop()
            self.arduino.close()
        else:  # reconectar
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("RECONECTADO")
            self.arduino.open()
            self.segundoPlano.start(100)

    def generaCadenaControlFocos(self):
        # 1-1-0-1-100-240-50
        cadena = str(self.foco1) + "-" + str(self.foco2) + "-" + \
                 str(self.foco3) + "-" + str(self.foco4) + "-" + \
                 str(self.foco5) + "-" + str(self.foco6) + "-" + str(self.foco7)
        print(cadena)
        # Si se ha establecido la conexion con arduno y esta se encuentra abierta...
        if not self.arduino is None and self.arduino.isOpen():
            self.arduino.write(cadena.encode())

    # Métodos para controlar el estado de cada foco
    def control_foco1(self):
        # Obtiene el texto del botón "btn_foco1"
        txtBoton = self.btn_foco1.text()
        if txtBoton == "PRENDER":
            # Si el texto es "PRENDER", cambia el texto a "APAGAR"
            self.btn_foco1.setText("APAGAR")
            # Asigna el valor 1 al foco1 para indicar que está encendido
            self.foco1 = 1
        else:
            # Si el texto es "APAGAR", cambia el texto a "PRENDER"
            self.btn_foco1.setText("PRENDER")
            # Asigna el valor 0 al foco1 para indicar que está apagado
            self.foco1 = 0
        # Genera la cadena de control de los focos
        self.generaCadenaControlFocos()

    # Métodos similares para los demás focos
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
        # Obtiene el valor actual del dial_foco5
        self.foco5 = self.dial_foco5.value()
        # Genera la cadena de control de los focos
        self.generaCadenaControlFocos()

    def control_foco6(self):
        # Obtiene el valor actual del dial_foco6
        self.foco6 = self.dial_foco6.value()
        # Genera la cadena de control de los focos
        self.generaCadenaControlFocos()

    def control_foco7(self):
        # Obtiene el valor actual del dial_foco7
        self.foco7 = self.dial_foco7.value()
        # Genera la cadena de control de los focos
        self.generaCadenaControlFocos()



    def cambiaComboBoxSeleleccion(self):
        clave = self.cb_potenciometros.currentData()
        print(clave)
        self.lw_datos_potenciometros.clear() ##limpia los registros anteriores para cambiar de sensor...
        self.datos_sensores[clave] = [] #limpia el registro  --- podria no limpiarse y entonces sería un historico...

    def lectura_datos_arduino(self):
        try:
            # Si se ha establecido la conexiSSón con Arduino y esta está abierta...
            if not self.arduino is None and self.arduino.isOpen():
                if self.arduino.inWaiting():  # Si hay información que leer
                    cadena_recibida = self.arduino.readline().decode().strip()
                    # print(cadena_recibida)

                    datos = cadena_recibida.split("-")
                    print(datos[0] + " - " + datos[1] + " - " + datos[2])

                    indice = self.cb_potenciometros.currentIndex()
                    clave = self.cb_potenciometros.currentData()

                    self.lw_datos_potenciometros.addItem(datos[indice])
                    self.lw_datos_potenciometros.setCurrentRow(self.lw_datos_potenciometros.count() - 1)

                    self.datos_sensores[clave].append(int(
                        datos[indice]))  # Lo añade a la lista del diccionario correspondiente al sensor seleccionado

                    min_val = min(self.datos_sensores[clave])
                    max_val = max(self.datos_sensores[clave])

                    avg_val = sum(self.datos_sensores[clave]) / len(self.datos_sensores[clave])
                    avg_val = round(avg_val, 2)

                    mediana_val = median(self.datos_sensores[clave])

                    self.txt_min.setText(str(min_val))  # Actualiza el campo de texto con el valor mínimo
                    self.txt_max.setText(str(max_val))  # Actualiza el campo de texto con el valor máximo
                    self.txt_promedio.setText(str(avg_val))  # Actualiza el campo de texto con el valor promedio
                    self.txt_mediana.setText(str(mediana_val))  # Actualiza el campo de texto con el valor de la mediana

        except KeyboardInterrupt:
            self.close()  # Maneja la interrupción de teclado (Ctrl+C) y cierra la aplicación
        except Exception as E:
            print(E)  # Muestra cualquier otra excepción en la consola de salida

    def closeEvent(self, event):
        # reply = QtWidgets.QMessageBox.question(self, "Mensaje", "Esta seguro de salir?", QtWidgets.QMessageBox.Yes,
        #                                       QtWidgets.QMessageBox.No)

        # if reply == QtWidgets.QMessageBox.Yes:
        self.segundoPlano.stop()
        event.accept()
        # else:
        #    event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
