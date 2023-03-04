# -*- coding: utf-8 -*-
import math

import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets

import Conversion


class Ui_Form_1(object):
    def Geo2Cart(self):

        #Parametres ellipsoide Clarke 1880
        a = 6378249.20
        e_2 = 0.0068034876


        phi_degree = int(self.lineEdit.text())
        phi_minute = int(self.lineEdit_2.text())
        phi_second = float(self.lineEdit_3.text())

        Lambda_degree = int(self.lineEdit_4.text())
        Lambda_minute = int(self.lineEdit_5.text())
        Lambda_second = float(self.lineEdit_6.text())

        elevation = float(self.lineEdit_7.text())

        phi = Conversion.dms2rad(phi_degree, phi_minute, phi_second)
        Lambda = Conversion.dms2rad(Lambda_degree, Lambda_minute, Lambda_second)
        N = a / (math.sqrt(1 - e_2 * np.sin(phi) ** 2))

        X = (N + elevation) * np.cos(phi) * np.cos(Lambda)
        Y = (N + elevation) * np.cos(phi) * np.sin(Lambda)
        Z = (N * (1 - e_2) + elevation) * np.sin(phi)

        self.lineEdit_8.setText(str(X))
        self.lineEdit_9.setText(str(Y))
        self.lineEdit_10.setText(str(Z))

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 700)
        Form.setStyleSheet("background-color: rgb(201, 201, 201);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_17 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.frame_12 = QtWidgets.QFrame(Form)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout.addWidget(self.frame_12)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame_10 = QtWidgets.QFrame(Form)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout.addWidget(self.frame_10)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_18 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.label_18)
        self.label_21 = QtWidgets.QLabel(self.frame_3)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_2.addWidget(self.label_21)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.label_19 = QtWidgets.QLabel(self.frame_3)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_2.addWidget(self.label_19)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        self.label_20 = QtWidgets.QLabel(self.frame_3)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_2.addWidget(self.label_20)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_2.addWidget(self.lineEdit_6)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_4.addWidget(self.lineEdit_7)
        self.label_22 = QtWidgets.QLabel(self.frame_4)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_4.addWidget(self.label_22)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(Form)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 53))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 53))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout.addWidget(self.frame_8)
        self.pushButton = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(31, 97, 116);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout.addWidget(self.frame_9)
        self.verticalLayout.addWidget(self.frame_6)
        self.label_16 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_23 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_5.addWidget(self.label_23)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_5.addWidget(self.lineEdit_8)
        self.label_28 = QtWidgets.QLabel(self.frame_2)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_5.addWidget(self.label_28)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_7 = QtWidgets.QFrame(Form)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_26 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 0, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 0, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.frame_7)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_25 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 0, 3, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 0, 6, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.frame_5)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 0, 7, 1, 1)
        self.verticalLayout.addWidget(self.frame_5)

        self.pushButton.clicked.connect(self.Geo2Cart)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_10.setReadOnly(True)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "GeotoCart"))
        Form.setWindowIcon(QtGui.QIcon("icon.png"))
        self.label_17.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#7b7561;\">Transformation des coordonnées géographiques</span></p><p align=\"center\"><span style=\" color:#7b7561;\"> aux coordonnées cartésiennes </span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p>Entrer les coordonnées geographiques :</p></body></html>"))
        self.label_2.setText(_translate("Form", "Latitude"))
        self.label_3.setText(_translate("Form", "deg"))
        self.label_4.setText(_translate("Form", "min"))
        self.label_5.setText(_translate("Form", "sec"))
        self.label_18.setText(_translate("Form", "Longitude"))
        self.label_21.setText(_translate("Form", "deg"))
        self.label_19.setText(_translate("Form", "min"))
        self.label_20.setText(_translate("Form", "sec"))
        self.label_14.setText(_translate("Form", "Hauteur"))
        self.label_15.setText(_translate("Form", "h ="))
        self.label_22.setText(_translate("Form", "m"))
        self.pushButton.setText(_translate("Form", "Convertir"))
        self.label_16.setText(_translate("Form", "Les coordonnées cartésiennes :"))
        self.label_23.setText(_translate("Form", "X ="))
        self.label_28.setText(_translate("Form", "m"))
        self.label_26.setText(_translate("Form", "Y ="))
        self.label_27.setText(_translate("Form", "m"))
        self.label_25.setText(_translate("Form", "Z="))
        self.label_24.setText(_translate("Form", "m"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_1()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
