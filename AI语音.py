# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AI语音.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(721, 679)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        Form.setAcceptDrops(False)
        self.Model = QtWidgets.QComboBox(Form)
        self.Model.setGeometry(QtCore.QRect(70, 290, 71, 22))
        self.Model.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Model.setToolTipDuration(-1)
        self.Model.setEditable(False)
        self.Model.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.Model.setDuplicatesEnabled(False)
        self.Model.setFrame(True)
        self.Model.setModelColumn(0)
        self.Model.setObjectName("Model")
        self.Model.addItem("")
        self.Model.addItem("")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 210, 71, 21))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setBackgroundVisible(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(310, 210, 101, 21))
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setPlaceholderText("")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(310, 290, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(530, 210, 111, 21))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.horizontalScrollBar = QtWidgets.QScrollBar(Form)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(530, 290, 111, 20))
        self.horizontalScrollBar.setMinimum(0)
        self.horizontalScrollBar.setMaximum(10)
        self.horizontalScrollBar.setSingleStep(1)
        self.horizontalScrollBar.setPageStep(1)
        self.horizontalScrollBar.setProperty("value", 0)
        self.horizontalScrollBar.setSliderPosition(0)
        self.horizontalScrollBar.setTracking(True)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setInvertedAppearance(False)
        self.horizontalScrollBar.setInvertedControls(True)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 370, 75, 23))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit.raise_()
        self.Model.raise_()
        self.plainTextEdit_2.raise_()
        self.comboBox.raise_()
        self.plainTextEdit_3.raise_()
        self.horizontalScrollBar.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)
        self.Model.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "AI语音"))
        self.Model.setCurrentText(_translate("Form", "符玄"))
        self.Model.setPlaceholderText(_translate("Form", "Model"))
        self.Model.setItemText(0, _translate("Form", "符玄"))
        self.Model.setItemText(1, _translate("Form", "魈"))
        self.plainTextEdit.setPlainText(_translate("Form", "模型选择"))
        self.plainTextEdit_2.setPlainText(_translate("Form", "F0预测器选择"))
        self.comboBox.setItemText(0, _translate("Form", "0：crepe"))
        self.comboBox.setItemText(1, _translate("Form", "1：pm"))
        self.comboBox.setItemText(2, _translate("Form", "2：dio"))
        self.comboBox.setItemText(3, _translate("Form", "3：harvest"))
        self.comboBox.setItemText(4, _translate("Form", "4：rmvpe"))
        self.comboBox.setItemText(5, _translate("Form", "5：fcpe"))
        self.plainTextEdit_3.setPlainText(_translate("Form", "特征检索占比"))
        self.pushButton.setText(_translate("Form", "推理"))
