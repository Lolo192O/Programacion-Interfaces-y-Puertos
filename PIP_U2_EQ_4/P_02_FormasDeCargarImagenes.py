import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_02FormasDeCargarImagenes.UI" #nombre del archivo aqui.
Ui_MainWindow, QtBaseCLass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals

        # Area de los Slots

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
