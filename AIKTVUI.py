# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AIKTVUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1213, 741)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 540, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 400, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 450, 111, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 540, 111, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 450, 111, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1050, 670, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(100, 670, 881, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(820, 630, 61, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(880, 630, 61, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(330, 520, 91, 71))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 610, 121, 61))
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setWordWrap(False)
        self.label.setIndent(2)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 110, 411, 261))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(660, 110, 411, 261))
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(670, 440, 351, 141))
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 30, 481, 51))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setIndent(-1)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "录音"))
        self.pushButton_2.setText(_translate("MainWindow", "ai模型"))
        self.pushButton_3.setText(_translate("MainWindow", "音乐"))
        self.pushButton_4.setText(_translate("MainWindow", "播放"))
        self.pushButton_5.setText(_translate("MainWindow", "ai音效"))
        self.pushButton_6.setText(_translate("MainWindow", "退出"))
        self.lineEdit.setText(_translate("MainWindow", "00：00"))
        self.lineEdit_2.setText(_translate("MainWindow", "/00：00"))
        self.lineEdit_4.setText(_translate("MainWindow", "录音计时n秒"))
        self.label.setText(_translate("MainWindow", "音乐名"))
        self.lineEdit_3.setText(_translate("MainWindow", "未处理音频文件或录音的声波图"))
        self.lineEdit_5.setText(_translate("MainWindow", "已处理音频文件或录音的声波图"))
        self.lineEdit_6.setText(_translate("MainWindow", "选中模型路径"))
        self.label_2.setText(_translate("MainWindow", "ai音频信号处理"))
