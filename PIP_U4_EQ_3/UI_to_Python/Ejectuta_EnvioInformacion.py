import sys
from PyQt5 import uic, QtWidgets

from UI_to_Python import Main_EnvioInfo as main,SecondWindow as second

class MyMainWindow(QtWidgets.QMainWindow, main.Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        main.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals

        # Area de los Slots

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

##############################################################


