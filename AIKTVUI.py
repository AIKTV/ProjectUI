# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AIKTVUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(932, 674)
        MainWindow.setMinimumSize(QtCore.QSize(800, 450))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.configWidget = QtWidgets.QWidget(self.centralwidget)
        self.configWidget.setMinimumSize(QtCore.QSize(191, 181))
        self.configWidget.setMaximumSize(QtCore.QSize(401, 221))
        self.configWidget.setObjectName("configWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.configWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chooseRecordGroupBox = QtWidgets.QGroupBox(self.configWidget)
        self.chooseRecordGroupBox.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.chooseRecordGroupBox.setObjectName("chooseRecordGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.chooseRecordGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chooseRecord = QtWidgets.QPushButton(self.chooseRecordGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chooseRecord.sizePolicy().hasHeightForWidth())
        self.chooseRecord.setSizePolicy(sizePolicy)
        self.chooseRecord.setMaximumSize(QtCore.QSize(75, 23))
        self.chooseRecord.setObjectName("chooseRecord")
        self.horizontalLayout_2.addWidget(self.chooseRecord)
        self.recordAddress = QtWidgets.QLineEdit(self.chooseRecordGroupBox)
        self.recordAddress.setObjectName("recordAddress")
        self.horizontalLayout_2.addWidget(self.recordAddress)
        self.verticalLayout_2.addWidget(self.chooseRecordGroupBox)
        self.chooseHandledGroupBox = QtWidgets.QGroupBox(self.configWidget)
        self.chooseHandledGroupBox.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.chooseHandledGroupBox.setObjectName("chooseHandledGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.chooseHandledGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chooseHandled = QtWidgets.QPushButton(self.chooseHandledGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chooseHandled.sizePolicy().hasHeightForWidth())
        self.chooseHandled.setSizePolicy(sizePolicy)
        self.chooseHandled.setMaximumSize(QtCore.QSize(75, 23))
        self.chooseHandled.setObjectName("chooseHandled")
        self.horizontalLayout.addWidget(self.chooseHandled)
        self.handledAddress = QtWidgets.QLineEdit(self.chooseHandledGroupBox)
        self.handledAddress.setObjectName("handledAddress")
        self.horizontalLayout.addWidget(self.handledAddress)
        self.verticalLayout_2.addWidget(self.chooseHandledGroupBox)
        self.frame = QtWidgets.QFrame(self.configWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2.addWidget(self.frame)
        self.configButton = QtWidgets.QPushButton(self.configWidget)
        self.configButton.setObjectName("configButton")
        self.verticalLayout_2.addWidget(self.configButton)
        self.gridLayout_2.addWidget(self.configWidget, 0, 0, 1, 1)
        self.recordWidget = QtWidgets.QWidget(self.centralwidget)
        self.recordWidget.setObjectName("recordWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.recordWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.recordTimeDisplay = QtWidgets.QLabel(self.recordWidget)
        self.recordTimeDisplay.setObjectName("recordTimeDisplay")
        self.verticalLayout.addWidget(self.recordTimeDisplay)
        self.recordButtonWidget = QtWidgets.QWidget(self.recordWidget)
        self.recordButtonWidget.setObjectName("recordButtonWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.recordButtonWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.recordButton = QtWidgets.QPushButton(self.recordButtonWidget)
        self.recordButton.setObjectName("recordButton")
        self.horizontalLayout_3.addWidget(self.recordButton)
        self.pauseRecordButton = QtWidgets.QPushButton(self.recordButtonWidget)
        self.pauseRecordButton.setObjectName("pauseRecordButton")
        self.horizontalLayout_3.addWidget(self.pauseRecordButton)
        self.verticalLayout.addWidget(self.recordButtonWidget)
        self.recordOutputDisplay = QtWidgets.QLabel(self.recordWidget)
        self.recordOutputDisplay.setText("")
        self.recordOutputDisplay.setObjectName("recordOutputDisplay")
        self.verticalLayout.addWidget(self.recordOutputDisplay)
        self.gridLayout_2.addWidget(self.recordWidget, 0, 1, 1, 1)
        self.playWidget = QtWidgets.QWidget(self.centralwidget)
        self.playWidget.setObjectName("playWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.playWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.recordPlayBox = QtWidgets.QGroupBox(self.playWidget)
        self.recordPlayBox.setAlignment(QtCore.Qt.AlignCenter)
        self.recordPlayBox.setObjectName("recordPlayBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.recordPlayBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.recordPlayButton = QtWidgets.QPushButton(self.recordPlayBox)
        self.recordPlayButton.setObjectName("recordPlayButton")
        self.horizontalLayout_4.addWidget(self.recordPlayButton)
        self.recordStopButton = QtWidgets.QPushButton(self.recordPlayBox)
        self.recordStopButton.setObjectName("recordStopButton")
        self.horizontalLayout_4.addWidget(self.recordStopButton)
        self.gridLayout.addWidget(self.recordPlayBox, 0, 0, 1, 1)
        self.handledPlayBox = QtWidgets.QGroupBox(self.playWidget)
        self.handledPlayBox.setAlignment(QtCore.Qt.AlignCenter)
        self.handledPlayBox.setObjectName("handledPlayBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.handledPlayBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.handledPlayButton = QtWidgets.QPushButton(self.handledPlayBox)
        self.handledPlayButton.setObjectName("handledPlayButton")
        self.horizontalLayout_5.addWidget(self.handledPlayButton)
        self.handledStopButton = QtWidgets.QPushButton(self.handledPlayBox)
        self.handledStopButton.setObjectName("handledStopButton")
        self.horizontalLayout_5.addWidget(self.handledStopButton)
        self.gridLayout.addWidget(self.handledPlayBox, 0, 1, 1, 1)
        self.playFrame = QtWidgets.QFrame(self.playWidget)
        self.playFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.playFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.playFrame.setObjectName("playFrame")
        self.time_lbl = QtWidgets.QLabel(self.playFrame)
        self.time_lbl.setGeometry(QtCore.QRect(390, 110, 72, 15))
        self.time_lbl.setObjectName("time_lbl")
        self.time_lbl_2 = QtWidgets.QLabel(self.playFrame)
        self.time_lbl_2.setGeometry(QtCore.QRect(480, 110, 72, 15))
        self.time_lbl_2.setObjectName("time_lbl_2")
        self.time_slider = QtWidgets.QSlider(self.playFrame)
        self.time_slider.setGeometry(QtCore.QRect(170, 70, 571, 22))
        self.time_slider.setOrientation(QtCore.Qt.Horizontal)
        self.time_slider.setObjectName("time_slider")
        self.play_btn = QtWidgets.QPushButton(self.playFrame)
        self.play_btn.setGeometry(QtCore.QRect(50, 70, 93, 28))
        self.play_btn.setObjectName("play_btn")
        self.mode_btn = QtWidgets.QPushButton(self.playFrame)
        self.mode_btn.setGeometry(QtCore.QRect(770, 70, 93, 28))
        self.mode_btn.setObjectName("mode_btn")
        self.gridLayout.addWidget(self.playFrame, 1, 0, 1, 2)
        self.gridLayout_2.addWidget(self.playWidget, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chooseRecordGroupBox.setTitle(_translate("MainWindow", "选择录音/原始音频文件"))
        self.chooseRecord.setText(_translate("MainWindow", "选择文件"))
        self.chooseHandledGroupBox.setTitle(_translate("MainWindow", "选择处理后音频文件"))
        self.chooseHandled.setText(_translate("MainWindow", "选择文件"))
        self.configButton.setText(_translate("MainWindow", "AI模型配置"))
        self.recordTimeDisplay.setText(_translate("MainWindow", "录音时长：你还没有开始录音哦"))
        self.recordButton.setText(_translate("MainWindow", "开始"))
        self.pauseRecordButton.setText(_translate("MainWindow", "暂停"))
        self.recordPlayBox.setTitle(_translate("MainWindow", "原始音频"))
        self.recordPlayButton.setText(_translate("MainWindow", "播放"))
        self.recordStopButton.setText(_translate("MainWindow", "停止"))
        self.handledPlayBox.setTitle(_translate("MainWindow", "处理后音频"))
        self.handledPlayButton.setText(_translate("MainWindow", "播放"))
        self.handledStopButton.setText(_translate("MainWindow", "停止"))
        self.time_lbl.setText(_translate("MainWindow", "TextLabel"))
        self.time_lbl_2.setText(_translate("MainWindow", "TextLabel"))
        self.play_btn.setText(_translate("MainWindow", "PushButton"))
        self.mode_btn.setText(_translate("MainWindow", "PushButton"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())