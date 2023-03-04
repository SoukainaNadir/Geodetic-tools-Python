# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets

from Menu import Ui_Form_menu




class Ui_MainWindow(object):

    def open3_(self):
        self.formSecond = QtWidgets.QWidget()
        self.ui = Ui_Form_menu()
        self.ui.setupUi(self.formSecond)
        MainWindow.close()
        self.formSecond.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 800)
        MainWindow.setStyleSheet("background-color: rgb(25, 79, 95);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setMouseTracking(True)
        self.label_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.label_2.setAcceptDrops(False)
        self.label_2.setStyleSheet("image: url(image.png);\n"
"image: url(image.png);")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setMinimumSize(QtCore.QSize(0, 100))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: qconicalgradient(cx:0, cy:1, angle:0, stop:0 rgba(151, 151, 151, 169), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.frame_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(self.open3_)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Form", "Bienvenue"))
        MainWindow.setWindowIcon(QtGui.QIcon("icon.png"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">GEODETIC TOOLS</span></p><p align=\"center\"></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-style:italic;\">Bienvenue</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Préparé par : NADIR Soukaina</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Encadré par : Mr Boulaassel</span><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">GeoInfo 2022/2023</span></p></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Commencer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
