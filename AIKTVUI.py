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
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(210, 540, 111, 51))
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(670, 400, 101, 41))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 450, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")
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
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(330, 520, 91, 71))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(100, 610, 121, 61))
        self.label1.setTextFormat(QtCore.Qt.PlainText)
        self.label1.setWordWrap(False)
        self.label1.setIndent(2)
        self.label1.setOpenExternalLinks(False)
        self.label1.setObjectName("label1")
        self.table1 = QtWidgets.QLineEdit(self.centralwidget)
        self.table1.setGeometry(QtCore.QRect(60, 110, 411, 261))
        self.table1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.table1.setObjectName("table1")
        self.table2 = QtWidgets.QLineEdit(self.centralwidget)
        self.table2.setGeometry(QtCore.QRect(660, 110, 411, 261))
        self.table2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.table2.setObjectName("table2")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(350, 30, 481, 51))
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setWordWrap(False)
        self.title.setIndent(-1)
        self.title.setOpenExternalLinks(False)
        self.title.setObjectName("title")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(670, 450, 291, 161))
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton3.setText(_translate("MainWindow", "录音"))
        self.pushButton_1.setText(_translate("MainWindow", "ai模型"))
        self.pushButton_2.setText(_translate("MainWindow", "音乐"))
        self.pushButton_4.setText(_translate("MainWindow", "播放"))
        self.pushButton_5.setText(_translate("MainWindow", "ai音效"))
        self.pushButton_6.setText(_translate("MainWindow", "退出"))
        self.lineEdit.setText(_translate("MainWindow", "00：00"))
        self.lineEdit_2.setText(_translate("MainWindow", "/00：00"))
        self.lineEdit_7.setText(_translate("MainWindow", "录音计时n秒"))
        self.label1.setText(_translate("MainWindow", "音乐名"))
        self.table1.setText(_translate("MainWindow", "未处理音频文件或录音的声波图"))
        self.table2.setText(_translate("MainWindow", "已处理音频文件或录音的声波图"))
        self.title.setText(_translate("MainWindow", "ai音频信号处理"))
        self.lineEdit_3.setText(_translate("MainWindow", "显示选中模型路径"))
