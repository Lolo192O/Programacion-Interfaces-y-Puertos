import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_06_EvaluacionOpAritm.ui" #nombre del archivo aqui.
Ui_MainWindow, QtBaseCLass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.btn_calcular.clicked.connect(self.calcular)

    # Area de los Slots
    def calcular(self):
        try:
            expresion = self.txt_operacion.text()
            result = eval(expresion)
            print(result)
            self.txt_resultado.setText(str(result))
        except Exception as error:
            print(error)
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
