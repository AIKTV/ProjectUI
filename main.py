import warnings
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from AIKTVUI import Ui_MainWindow
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import os

warnings.filterwarnings("ignore", category=DeprecationWarning)

recordFileAddress = ""  # 录音/原始文件地址
handledFileAddress = ""  # 处理后文件地址


class MainForm(QMainWindow, Ui_MainWindow):
    """正式文件 MainForm class"""
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.chooseRecord.clicked.connect(lambda:self.openfiledialog('record'))
        self.chooseHandled.clicked.connect(lambda:self.openfiledialog('handled'))

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

        seconds = int(d / 1000)
        # 获取时长的分钟
        minutes = int(seconds / 60)
        seconds = seconds - -minutes * 60
        str_time1 = ""
        if minutes < 10:
            str_time1 = str_time1 + "0" + str(minutes)
        else:
            str_time1 = str_time1 + str(minutes)
        str_time1 = str_time1 + ":"
        if seconds < 10:
            str_time1 = str_time1 + "0" + str(seconds)
        else:
            str_time1 = str_time1 + str(seconds)

        # 把分钟和秒设置在时间标签中显示
        b = str_time1
        self.time_lbl_2.setText(f"{b}")

        # 获取当前播放列表
        index = self.playList.currentIndex()



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
        a = str_time + "    /"
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





    def openfiledialog(self, type):
        global recordFileAddress
        global handledFileAddress  # 声明全局变量
        filename, filetype = QtWidgets.QFileDialog.getOpenFileName(
            self, "选取文件", os.getcwd(), '波形文件(*.wav)')
        if filename:  # 如果文件名非空
            if type == 'record':  # 传递的类型为record 录音/原始文件
                self.recordAddress.setText(filename)  # 设置文本框内容
                recordFileAddress = filename  # 更新全局变量的值
            if type == 'handled':  # 传递的类型为handled 处理后文件
                self.handledAddress.setText(filename)
                handledFileAddress = filename


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
