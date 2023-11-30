import warnings
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from AIKTVUI import Ui_MainWindow
import sys
import os

warnings.filterwarnings("ignore", category=DeprecationWarning)

recordFileAddress = ""  # 录音/原始文件地址
handledFileAddress = ""  # 处理后文件地址


class MainForm(QMainWindow, Ui_MainWindow):
    """正式文件 MainForm class"""

    def __init__(self):
        """使用的控件相关触发器全放这里"""
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.chooseRecord.clicked.connect(
            lambda: self.openfiledialog('record'))
        self.chooseHandled.clicked.connect(
            lambda: self.openfiledialog('handled'))
        self.recordPlayButton.clicked.connect(
            self.play_sound_a)
        self.handledPlayButton.clicked.connect(
            self.play_sound_b)
        self.recordPlayButton = '播放'  # 记录recordPlayButton的状态
        self.handledPlayButton = '播放'  # 记录handledPlayButton的状态

    def play_sound_a(self):
        if self.recordPlayButton == '播放':  #
            if self.handledPlayButton == '暂停':
                self.audio_a.stop()
                self.handledPlayButton.setText('播放')  # 修改handledPlayButton的文本为"播放"
                self.handledPlayButton = '播放'  # 修改handledPlayButton的状态为"播放"

            self.audio_a.play()  # 播放audio_a.wav音频文件
            self.recordPlayButton.setText('暂停')  # 修改recordPlayButton的文本为"暂停"
            self.recordPlayButton = '暂停'  # 修改recordPlayButton的状态为"暂停"
        else:  # 如果recordPlayButton处于"暂停"状态
            self.audio_a.stop()  # 停止播放audio_a.wav音频文件
            self.recordPlayButton.setText('播放')  # 修改recordPlayButton的文本为"播放"
            self.recordPlayButton = '播放'  # 修改recordPlayButton的状态为"播放"

    def openfiledialog(self, type):
        global recordFileAddress
        global handledFileAddress  # 声明全局变量
        if type == 'record':
            typetext = '录音/原始'
        else:
            typetext = '要播放的'
        fileaddress, filetype = QtWidgets.QFileDialog.getOpenFileName(
            self, "选择" + typetext + "文件", os.getcwd(), '波形文件(*.wav)')
        if fileaddress:  # 如果文件名非空
            if type == 'record':  # 传递的类型为record 录音/原始文件
                self.recordAddress.setText(
                    os.path.basename(fileaddress))  # 设置文本框内容
                recordFileAddress = fileaddress  # 更新全局变量的值
            # if type == 'handled':  # 传递的类型为handled 处理后文件
            else:
                self.handledAddress.setText(os.path.basename(fileaddress))
                handledFileAddress = fileaddress


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
