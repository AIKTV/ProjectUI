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
            lambda: self.openfiledialog('record', 'WAV波形文件(*.wav)'))
        self.chooseHandled.clicked.connect(
            lambda: self.openfiledialog('handled', 'FLAC无损音频文件(*.flac)'))

    def openfiledialog(self, button, type):
        global recordFileAddress
        global handledFileAddress  # 声明全局变量
        if button == 'record':
            typetext = '录音/原始'
        else:
            typetext = '要播放的'
        fileaddress, filetype = QtWidgets.QFileDialog.getOpenFileName(
            self, "选择" + typetext + "文件", os.getcwd(), type)
        if fileaddress:  # 如果文件名非空
            if button == 'record':  # 传递的类型为record 录音/原始文件
                self.recordAddress.setText(
                    os.path.basename(fileaddress))  # 设置文本框内容
                recordFileAddress = fileaddress  # 更新全局变量的值
            # if button == 'handled':  # 传递的类型为handled 处理后文件
            else:
                self.handledAddress.setText(os.path.basename(fileaddress))
                handledFileAddress = fileaddress


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
