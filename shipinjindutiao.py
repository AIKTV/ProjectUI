# coding=gb2312
# 基于pyqt5
import os
import sys

# from PyQt5.QtCore import QDateTime, QUrl
from PyQt5.QtMultimedia import QAudioOutput, QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QSlider
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# from mediawin_qt5 import Ui_MainWindow


class Video_win(QWidget):
    def __init__(self):
        super(Video_win, self).__init__()
        self.setWindowTitle("简易播放器")
        self.resize(800, 600)
        # 播放画面
        self.player = QMediaPlayer()
        self.videoout = QVideoWidget(self)  # 定义视频显示的widget
        self.videoout.resize(self.width(), self.height())
        self.player.setVideoOutput(self.videoout)  # 视频播放输出的widget，就是上面定义的

        # 当前播放的进度，显示调整视频进度条
        self.timeSlider = QSlider(self)
        self.timeSlider.setOrientation(Qt.Horizontal)
        self.timeSlider.setValue(0)
        self.timeSlider.setMinimum(0)
        self.player.positionChanged.connect(self.get_time)
        self.timeSlider.sliderPressed.connect(self.player.pause)
        self.timeSlider.sliderMoved.connect(self.change_time)
        self.timeSlider.sliderReleased.connect(self.player.play)

        # 打开视频
        self.open_button = QPushButton('打开')
        self.open_button.clicked.connect(self.open_file)
        # 快进
        self.right_button = QPushButton('快进')
        self.right_button.clicked.connect(self.up_time)
        # play
        self.play_button = QPushButton('播放')
        self.play_button.clicked.connect(self.player.play)
        # pause
        self.mid_button = QPushButton('暂停')
        self.mid_button.clicked.connect(self.player.pause)
        # 快退
        self.left_button = QPushButton('快退')
        self.left_button.clicked.connect(self.down_time)
        # 上述按钮布局
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.open_button)
        button_layout.addWidget(self.right_button)
        button_layout.addWidget(self.play_button)
        button_layout.addWidget(self.mid_button)
        button_layout.addWidget(self.left_button)

        # 总体布局
        all_layout = QVBoxLayout(self)
        all_layout.addWidget(self.videoout)
        all_layout.addWidget(self.timeSlider)
        all_layout.addLayout(button_layout)
        self.setLayout(all_layout)

    # 打开视频
    def open_file(self):
        self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))  # 选取视频文件
        msg = QMessageBox.information(self, '提示', "已经打开视频文件")

    # 调节播放进度
    def change_time(self, num):
        self.player.setPosition(num)

    # 快进
    def up_time(self):
        num = self.player.position() + int(self.player.duration() / 20)
        self.player.setPosition(num)

    # 快退
    def down_time(self):
        num = self.player.position() - int(self.player.duration() / 20)
        self.player.setPosition(num)

    # 获取获得进度条进度
    def get_time(self, num):
        self.timeSlider.setMaximum(self.player.duration())
        self.timeSlider.setValue(num)
        d = QDateTime.fromMSecsSinceEpoch(num).toString("mm:ss")
        all = self.player.duration()
        all_d = QDateTime.fromMSecsSinceEpoch(all).toString("mm:ss")

    def closeEvent(self, event):  # 关闭前需要self.player.pause()操作，否则报错
        self.player.pause()
        reply = QMessageBox.question(self, '提示',
                                     "是否退出",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    win = Video_win()
    win.show()
    sys.exit(app.exec())


