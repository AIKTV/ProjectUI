# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AIKTVUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QVBoxLayout,QLabel,QLineEdit,QPushButton,QInputDialog,QMessageBox,QDialog
from PyQt5.QtCore import Qt,QProcess
from PyQt5 import QtCore,QtGui,QtWidgets


class Ui_MainWindow(object):
    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(932,674)
        MainWindow.setMinimumSize(QtCore.QSize(800,450))
        MainWindow.setMaximumSize(QtCore.QSize(1600,900))
        MainWindow.resize(932, 674)
        MainWindow.setMinimumSize(QtCore.QSize(800, 450))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 900))
        MainWindow.resize(932, 674)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/7.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setMinimumSize(QtCore.QSize(800, 450))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.configWidget = QtWidgets.QWidget(self.centralwidget)
        self.configWidget.setMinimumSize(QtCore.QSize(191,181))
        self.configWidget.setMaximumSize(QtCore.QSize(401,221))
        self.configWidget.setObjectName("configWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.configWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chooseRecordGroupBox = QtWidgets.QGroupBox(self.configWidget)
        self.chooseRecordGroupBox.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.chooseRecordGroupBox.setObjectName("chooseRecordGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.chooseRecordGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chooseRecord = QtWidgets.QPushButton(self.chooseRecordGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chooseRecord.sizePolicy().hasHeightForWidth())
        self.chooseRecord.setSizePolicy(sizePolicy)
        self.chooseRecord.setMaximumSize(QtCore.QSize(75,23))
        self.chooseRecord.setObjectName("chooseRecord")
        self.horizontalLayout_2.addWidget(self.chooseRecord)
        self.recordAddress = QtWidgets.QLineEdit(self.chooseRecordGroupBox)
        self.recordAddress.setObjectName("recordAddress")
        self.horizontalLayout_2.addWidget(self.recordAddress)
        self.verticalLayout_2.addWidget(self.chooseRecordGroupBox)
        self.chooseHandledGroupBox = QtWidgets.QGroupBox(self.configWidget)
        self.chooseHandledGroupBox.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.chooseHandledGroupBox.setObjectName("chooseHandledGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.chooseHandledGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chooseHandled = QtWidgets.QPushButton(self.chooseHandledGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chooseHandled.sizePolicy().hasHeightForWidth())
        self.chooseHandled.setSizePolicy(sizePolicy)
        self.chooseHandled.setMaximumSize(QtCore.QSize(75,23))
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
        self.gridLayout_2.addWidget(self.configWidget,0,0,1,1)
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
        self.gridLayout_2.addWidget(self.recordWidget,0,1,1,1)
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
        self.gridLayout.addWidget(self.recordPlayBox,0,0,1,1)
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
        self.gridLayout.addWidget(self.handledPlayBox,0,1,1,1)
        self.playFrame = QtWidgets.QFrame(self.playWidget)
        self.playFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.playFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.playFrame.setObjectName("playFrame")
        self.time_lbl = QtWidgets.QLabel(self.playFrame)
        self.time_lbl.setGeometry(QtCore.QRect(390,110,72,15))
        self.time_lbl.setObjectName("time_lbl")
        self.time_lbl_2 = QtWidgets.QLabel(self.playFrame)
        self.time_lbl_2.setGeometry(QtCore.QRect(480,110,72,15))
        self.time_lbl_2.setObjectName("time_lbl_2")
        self.time_slider = QtWidgets.QSlider(self.playFrame)
        self.time_slider.setGeometry(QtCore.QRect(170,70,571,22))
        self.time_slider.setOrientation(QtCore.Qt.Horizontal)
        self.time_slider.setObjectName("time_slider")
        self.play_btn = QtWidgets.QPushButton(self.playFrame)
        self.play_btn.setGeometry(QtCore.QRect(50,70,93,28))
        self.play_btn.setObjectName("play_btn")
        self.mode_btn = QtWidgets.QPushButton(self.playFrame)
        self.mode_btn.setGeometry(QtCore.QRect(770,70,93,28))
        self.mode_btn.setObjectName("mode_btn")
        self.gridLayout.addWidget(self.playFrame,1,0,1,2)
        self.gridLayout_2.addWidget(self.playWidget,1,0,1,2)
        self.gridLayout.addWidget(self.playFrame, 1, 0, 1, 2)
        self.gridLayout_2.addWidget(self.playWidget, 1, 0, 1, 2)
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
        self.time_lbl.setGeometry(QtCore.QRect(390, 110, 90, 18))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        self.time_lbl.setFont(font)
        self.time_lbl.setObjectName("time_lbl")

        self.time_lbl_2 = QtWidgets.QLabel(self.playFrame)
        self.time_lbl_2.setGeometry(QtCore.QRect(480, 110, 90, 18))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        self.time_lbl_2.setFont(font)
        self.time_lbl_2.setObjectName("time_lbl_2")

        self.time_slider = QtWidgets.QSlider(self.playFrame)
        self.time_slider.setGeometry(QtCore.QRect(170, 70, 571, 22))
        self.time_slider.setOrientation(QtCore.Qt.Horizontal)
        self.time_slider.setObjectName("time_slider")

        self.play_btn = QtWidgets.QPushButton(self.playFrame)
        self.play_btn.setEnabled(True)
        self.play_btn.setGeometry(QtCore.QRect(50, 70, 93, 28))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        self.play_btn.setFont(font)
        self.play_btn.setMouseTracking(False)
        self.play_btn.setTabletTracking(False)
        self.play_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_btn.setIcon(icon1)
        self.play_btn.setIconSize(QtCore.QSize(70, 150))
        self.play_btn.setObjectName("play_btn")

        self.mode_btn = QtWidgets.QPushButton(self.playFrame)
        self.mode_btn.setGeometry(QtCore.QRect(770, 70, 93, 28))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        self.mode_btn.setFont(font)
        self.mode_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/4.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mode_btn.setIcon(icon2)
        self.mode_btn.setIconSize(QtCore.QSize(130, 130))
        self.mode_btn.setObjectName("mode_btn")

        self.gridLayout.addWidget(self.playFrame, 1, 0, 1, 2)
        self.gridLayout_2.addWidget(self.playWidget, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.myWindowInit()



    def retranslateUi(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","MainWindow"))
        self.chooseRecordGroupBox.setTitle(_translate("MainWindow","选择录音/原始音频文件"))
        self.chooseRecord.setText(_translate("MainWindow","选择文件"))
        self.chooseHandledGroupBox.setTitle(_translate("MainWindow","选择处理后音频文件"))
        self.chooseHandled.setText(_translate("MainWindow","选择文件"))
        self.configButton.setText(_translate("MainWindow","AI模型配置"))
        self.recordTimeDisplay.setText(_translate("MainWindow","录音时长：你还没有开始录音哦"))
        self.recordButton.setText(_translate("MainWindow","开始"))
        self.pauseRecordButton.setText(_translate("MainWindow","暂停"))

    def openConfigDialog(self):
        dialog = QtWidgets.QDialog(MainWindow)
        dialog.setWindowTitle("AI模型配置")
        layout = QtWidgets.QVBoxLayout(dialog)

        self.model_name_label = QLabel("请输入使用的模型步数（例：模型为G_800.pth就输入800）")
        self.model_name_edit = QLineEdit()
        layout.addWidget(self.model_name_label)
        layout.addWidget(self.model_name_edit)

        self.wav_name_label = QLabel("请输入参考的wav干声文件名，该文件应放入raw文件夹下（例：文件名为test.wav就输入test）")
        self.wav_name_edit = QLineEdit()
        layout.addWidget(self.wav_name_label)
        layout.addWidget(self.wav_name_edit)

        self.key_num_label = QLabel("请输入音高（例：维持原调为0，支持正负，数字为半音）")
        self.key_num_edit = QLineEdit()
        layout.addWidget(self.key_num_label)
        layout.addWidget(self.key_num_edit)

        self.f0_predictor_label = QLabel("请选择使用的F0预测器，0为crepe，1为pm，2为dio，3为harvest")
        self.f0_predictor_edit = QLineEdit()
        layout.addWidget(self.f0_predictor_label)
        layout.addWidget(self.f0_predictor_edit)

        self.if_diffusion_label = QLabel("是否使用浅层扩散模型？使用后可解决一部分电音问题（推荐）\n请注意该模型需先单独训练好（y/n）")
        self.if_diffusion_edit = QLineEdit()
        layout.addWidget(self.if_diffusion_label)
        layout.addWidget(self.if_diffusion_edit)

        self.diffusion_name_label = QLabel("请输入使用的扩散模型步数（例：模型为model_2000.pt就输入2000）")
        self.diffusion_name_edit = QLineEdit()
        layout.addWidget(self.diffusion_name_label)
        layout.addWidget(self.diffusion_name_edit)

        self.diffusion_k_step_label = QLabel("请输入扩散步数，越大越接近扩散模型的结果，默认100（例：100）")
        self.diffusion_k_step_edit = QLineEdit()
        layout.addWidget(self.diffusion_k_step_label)
        layout.addWidget(self.diffusion_k_step_edit)

        self.if_cluster_label = QLabel("是否使用聚类模型？聚类模型可以减小音色泄漏，但会降低模型的咬字\n请注意该模型需先单独训练好（y/n）")
        self.if_cluster_edit = QLineEdit()
        layout.addWidget(self.if_cluster_label)
        layout.addWidget(self.if_cluster_edit)

        self.cluster_ratio_label = QLabel("请输入聚类方案占比，范围 0-1（例：0为不使用）")
        self.cluster_ratio_edit = QLineEdit()
        layout.addWidget(self.cluster_ratio_label)
        layout.addWidget(self.cluster_ratio_edit)

        self.if_auto_predict_f0_label = QLabel("是否使用自动音高预测？推荐语音转换开启，歌声转换开启会严重跑调（y/n）")
        self.if_auto_predict_f0_edit = QLineEdit()
        layout.addWidget(self.if_auto_predict_f0_label)
        layout.addWidget(self.if_auto_predict_f0_edit)

        self.if_clip_label = QLabel("是否使用音频强制切片？单位为秒（例：0为自动切片，10为强制10秒切一段）")
        self.if_clip_edit = QLineEdit()
        layout.addWidget(self.if_clip_label)
        layout.addWidget(self.if_clip_edit)

        self.if_linear_gradient_label = QLabel("请输入两段音频切片的交叉淡入长度，单位为秒")
        self.if_linear_gradient_edit = QLineEdit()
        layout.addWidget(self.if_linear_gradient_label)
        layout.addWidget(self.if_linear_gradient_edit)

        start_button = QtWidgets.QPushButton("开始转换")
        start_button.clicked.connect(self.start_conversion)
        layout.addWidget(start_button)
        dialog.exec_()

    def start_conversion(self):
        model_name = self.model_name_edit.text()
        wav_name = self.wav_name_edit.text()
        key_num = self.key_num_edit.text()
        f0_predictor = self.f0_predictor_edit.text()
        if f0_predictor == '0':
            f0_predictor = 'crepe'
        if f0_predictor == '1':
            f0_predictor = 'pm'
        if f0_predictor == '2':
            f0_predictor = 'dio'
        if f0_predictor == '3':
            f0_predictor = 'harvest'
        if_diffusion = self.if_diffusion_edit.text()
        diffusion_name = self.diffusion_name_edit.text()
        diffusion_k_step = self.diffusion_k_step_edit.text()

        if_cluster = self.if_cluster_edit.text()
        cluster_ratio = self.cluster_ratio_edit.text()

        if_auto_predict_f0 = self.if_auto_predict_f0_edit.text()

        if_clip = self.if_clip_edit.text()
        if_linear_gradient = self.if_linear_gradient_edit.text()

        inference_case = r'.\env\python.exe inference_main.py'
        inference_case = inference_case + f' -m "logs/44k/G_{model_name}.pth" -c "configs/config.json" -n "{wav_name}" -t {key_num} -s "barbara" -f0p {f0_predictor}'

        if if_diffusion == 'y':
            inference_case = inference_case + f' -shd -dm "logs/44k/diffusion/model_{diffusion_name}.pt" -ks {diffusion_k_step}'
        if if_cluster == 'y':
            inference_case = inference_case + f' -cm "logs/44k/kmeans_10000.pt" -cr {cluster_ratio}'
        if if_auto_predict_f0 == 'y':
            inference_case = inference_case + f' -a'

        inference_case = inference_case + f' -cl {if_clip} -lg {if_linear_gradient}'

        process = QProcess()
        process.start(inference_case)
        process.waitForFinished()
        process.close()
        process.deleteLater()

        QtWidgets.QMessageBox.information(MainWindow,"转换完成","转换已完成！")

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
        self.recordPlayBox.setTitle(_translate("MainWindow", "原始音频"))
        self.recordPlayButton.setText(_translate("MainWindow", "播放"))
        self.recordStopButton.setText(_translate("MainWindow", "停止"))
        self.handledPlayBox.setTitle(_translate("MainWindow", "处理后音频"))
        self.handledPlayButton.setText(_translate("MainWindow", "播放"))
        self.handledStopButton.setText(_translate("MainWindow", "停止"))

        self.play_btn.setText(_translate("MainWindow", "PushButton"))
        self.mode_btn.setText(_translate("MainWindow", "PushButton"))
        self.time_lbl.setText(_translate("MainWindow", "00:00/00:00"))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())