# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myMusics.ui'
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


def fileNames(args):
    pass


class QMeduaContent(object):
    pass


def fromLocalFile(i):
    pass


class MainWindow(object):
    pass


class MainWindow(object):
    pass


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 148)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/7.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.play_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn.setEnabled(True)
        self.play_btn.setGeometry(QtCore.QRect(0, -10, 181, 161))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        self.play_btn.setFont(font)
        self.play_btn.setMouseTracking(False)
        self.play_btn.setTabletTracking(False)
        self.play_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_btn.setIcon(icon1)
        self.play_btn.setIconSize(QtCore.QSize(130, 130))
        self.play_btn.setObjectName("play_btn")
        self.mode_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mode_btn.setGeometry(QtCore.QRect(500, -10, 191, 161))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        self.mode_btn.setFont(font)
        self.mode_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/4.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mode_btn.setIcon(icon2)
        self.mode_btn.setIconSize(QtCore.QSize(130, 130))
        self.mode_btn.setObjectName("mode_btn")
        self.time_slider = QtWidgets.QSlider(self.centralwidget)
        self.time_slider.setGeometry(QtCore.QRect(240, 60, 211, 20))
        self.time_slider.setOrientation(QtCore.Qt.Horizontal)
        self.time_slider.setObjectName("time_slider")
        self.time_lbl = QtWidgets.QLabel(self.centralwidget)
        self.time_lbl.setGeometry(QtCore.QRect(300, 90, 90, 18))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        self.time_lbl.setFont(font)
        self.time_lbl.setObjectName("time_lbl")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 调用自定义的窗体初始化属性函数
        self.myWindowInit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AI"))
        self.time_lbl.setText(_translate("MainWindow", "00:00/00:00"))

    # 自定义窗体初始化属性的函数
    def myWindowInit(self):
        # 创建播放列表对象（窗体属性）
        self.playList = QMediaPlaylist()
        # 初始化播放列表对象的播放模式Loop(顺序播放）
        self.playList.setPlaybackMode(QMediaPlaylist.Loop)
        # 创建播放器对象（窗体属性）
        self.player = QMediaPlayer()
        # 初始化播放器的播放音量最大
        self.player.setVolume(100)
        # 设置播放器的播放列表
        self.player.setPlaylist(self.playList)
        # 创建列表对像（窗体属性）
        self.musicNames = []
        # 设置按钮的提示信息
        self.play_btn.setToolTip("播放")
        self.mode_btn.setToolTip("顺序播放")
        # 给播放按钮的单击信号（clicke)调用函数musicPlay
        self.play_btn.clicked.connect(self.musicPlay)
        # 给播放器的播放音频持续时长改变信号（durationChang)调用getTotalTime
        self.player.durationChanged.connect(self.getTotalTime)
        # 给播放器的当前播放位置更改信号（positionChanged)调用getCurrentTime
        self.player.positionChanged.connect(self.getCurrentTime)
        # 给时间进度条的拖拽移动（sliderMoved)调用自主定义函数timeChanfed
        self.time_slider.sliderMoved.connect(self.timeChanged)
        # 给模式按钮点击（clicked信号）调用自定义函数modeChanged
        self.mode_btn.clicked.connect(self.modeChanged)

    # 自定义函数，更改播放模式

    def modeChanged(self):
        # 判断播放列表的播放模式是否是顺序播放
        if self.playList.playbackMode() == QMediaPlaylist.Loop:
            # 1)更改播放列表当前播放模式为单曲循环
            self.playList.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
            # 2)更改模式按钮的图片为单曲循环图片
            self.mode_btn.setIcon(QIcon("images/3.ico"))
            # 3)更改模式按钮提示信息
            self.mode_btn.setToolTip("单曲循环")
            # 否则单曲循环
        else:
            # 1)更改播放列表当前播放模式为顺序播放
            self.playList.setPlaybackMode(QMediaPlaylist.Loop)
            # 2)更改模式按钮的图片为顺序图片
            self.mode_btn.setIcon(QIcon("images/4.ico"))
            # 3)更改模式按钮提示信息
            self.mode_btn.setToolTip("顺序播放")

    # 自定义函数，获取播放音频的总时长,参数d保存的音频的总时长 （毫秒）
    def getTotalTime(self, d):
        # .设置时间进度条的进度值和正在播放的音频总时长一致
        self.time_slider.setRange(0, d)
        # 获取当前播放列表
        index = self.playList.currentIndex()
        # 设置窗体标题显示播放音频名称
        MainWindow.setWindowTitle(f"AI--{self.musicNames[index]}")

    # 自定义函数，获取播放音频的当前时长，参数p保存的是音频当前时长（毫秒）
    def getCurrentTime(self, p):
        # 设置时长进度条的当前进度
        self.time_slider.setValue(p)
        # 获取时长的秒
        seconds = int(p / 1000)
        # 获取时长的分钟
        minutes = int(seconds / 60)
        seconds = seconds - -minutes * 60
        str_time = ""
        if minutes < 10:
            str_time = str_time + "0" + str(minutes)
        else:
            str_time = str_time + str(minutes)
        str_time = str_time + ":"
        if seconds < 10:
            str_time = str_time + "0" + str(seconds)
        else:
            str_time = str_time + str(seconds)

        # 把分钟和秒设置在时间标签中显示
        a = str_time + "/" + str_time
        self.time_lbl.setText(f"{a}")

    # 自定义函数，更改当前播放位置
    def timeChanged(self, t):
        # 设置播放器的当前位置为进度条的当前进度
        self.player.setPosition(t)

    # 自定义播放函数
    def musicPlay(self):
        # 判断播放器是否是播放状态
        if self.player.state() == QMediaPlayer.State.PlayingState:
            # 更改播放器为暂停状态
            self.player.pause()
            # 更改播放按钮的图片为暂停图片
            self.play_btn.setIcon(QIcon("images/1.ico"))
            # 更改播放按钮的提示信息为“播放”
            self.play_btn.setToolTip("播放")

        # 判断播放器是否是暂停状态
        elif self.player.state() == QMediaPlayer.State.PausedState:
            # 更改播放器为播放状态
            self.player.play()
            # 更改播放按钮的图片为播放图片
            self.play_btn.setIcon(QIcon("images/2.ico"))
            # 更改播放按钮的提示信息为“暂停”
            self.play_btn.setToolTip("暂停")
        # 否则（停止状态）
        else:
            # 获取本地音频文件
            fileNames, typeName = QFileDialog.getOpenFileNames(None, "选择音乐", 'D:/ai', "*")
            # 循环音频文件的列表
            for i in fileNames:
                # 把音频文件加载到播放列表对象中
                self.playList.addMedia(QMediaContent(QUrl.fromLocalFile(i)))
                # 获取音频文件路径最后一个“/"字符的位置
                start = i.rfind('/')
                end = i.rfind('.')
                # 获取音频文件中文件名称，追加到列表对象中
                self.musicNames.append(i[start + 1:end])
            # 设置当前播放列表的播放音频索引
            self.playList.setCurrentIndex(0)
            # 开始播放
            self.player.play()
            # 更改播放按钮的图片为暂停图片
            self.play_btn.setIcon(QIcon("images/2.ico"))
            # 更改播放按钮的提示信息为“暂停”
            self.play_btn.setToolTip("暂停")
            # 设置窗体标题显示当前播放名称
            MainWindow.setWindowTitle(f"我的音乐酷--{self.musicNames[0]}")


# 程序入口
if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)
    # 创建主窗体对象
    MainWindow = QMainWindow()
    # 创建我们自定义的窗体对象
    ui = Ui_MainWindow()
    # 设置自定义窗体对象为主窗体
    ui.setupUi(MainWindow)
    # 设置窗体大小不可更改
    MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
    # 显示主窗体
    MainWindow.show()
    # 应用程序退出
    sys.exit(app.exec_())