# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P1_Ejemplo.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 659)
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_agregar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_agregar.setGeometry(QtCore.QRect(30, 170, 411, 101))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_agregar.setFont(font)
        self.btn_agregar.setStyleSheet("background-color: cyan;\n"
"border: 4px solid red;\n"
"border-radius:20px;\n"
"color: black;")
        self.btn_agregar.setObjectName("btn_agregar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 40, 271, 81))
        self.label.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.label.setObjectName("label")
        self.txt_promedio = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_promedio.setGeometry(QtCore.QRect(370, 500, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.txt_promedio.setFont(font)
        self.txt_promedio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_promedio.setText("")
        self.txt_promedio.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_promedio.setObjectName("txt_promedio")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 370, 271, 81))
        self.label_3.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.txt_calificacion = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_calificacion.setGeometry(QtCore.QRect(550, 40, 151, 81))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.txt_calificacion.setFont(font)
        self.txt_calificacion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_calificacion.setText("")
        self.txt_calificacion.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_calificacion.setObjectName("txt_calificacion")
        self.btn_calcular = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calcular.setGeometry(QtCore.QRect(470, 170, 411, 101))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_calcular.setFont(font)
        self.btn_calcular.setStyleSheet("background-color: cyan;\n"
"border: 4px solid red;\n"
"border-radius:20px;\n"
"color: black;")
        self.btn_calcular.setObjectName("btn_calcular")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 940, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_agregar.setText(_translate("MainWindow", "Agregar"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Calif:</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Promedio</span></p><p align=\"center\"><br/></p></body></html>"))
        self.btn_calcular.setText(_translate("MainWindow", "Calcular"))
