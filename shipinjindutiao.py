# coding=gb2312
# ����pyqt5
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
        self.setWindowTitle("���ײ�����")
        self.resize(800, 600)
        # ���Ż���
        self.player = QMediaPlayer()
        self.videoout = QVideoWidget(self)  # ������Ƶ��ʾ��widget
        self.videoout.resize(self.width(), self.height())
        self.player.setVideoOutput(self.videoout)  # ��Ƶ���������widget���������涨���

        # ��ǰ���ŵĽ��ȣ���ʾ������Ƶ������
        self.timeSlider = QSlider(self)
        self.timeSlider.setOrientation(Qt.Horizontal)
        self.timeSlider.setValue(0)
        self.timeSlider.setMinimum(0)
        self.player.positionChanged.connect(self.get_time)
        self.timeSlider.sliderPressed.connect(self.player.pause)
        self.timeSlider.sliderMoved.connect(self.change_time)
        self.timeSlider.sliderReleased.connect(self.player.play)

        # ����Ƶ
        self.open_button = QPushButton('��')
        self.open_button.clicked.connect(self.open_file)
        # ���
        self.right_button = QPushButton('���')
        self.right_button.clicked.connect(self.up_time)
        # play
        self.play_button = QPushButton('����')
        self.play_button.clicked.connect(self.player.play)
        # pause
        self.mid_button = QPushButton('��ͣ')
        self.mid_button.clicked.connect(self.player.pause)
        # ����
        self.left_button = QPushButton('����')
        self.left_button.clicked.connect(self.down_time)
        # ������ť����
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.open_button)
        button_layout.addWidget(self.right_button)
        button_layout.addWidget(self.play_button)
        button_layout.addWidget(self.mid_button)
        button_layout.addWidget(self.left_button)

        # ���岼��
        all_layout = QVBoxLayout(self)
        all_layout.addWidget(self.videoout)
        all_layout.addWidget(self.timeSlider)
        all_layout.addLayout(button_layout)
        self.setLayout(all_layout)

    # ����Ƶ
    def open_file(self):
        self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))  # ѡȡ��Ƶ�ļ�
        msg = QMessageBox.information(self, '��ʾ', "�Ѿ�����Ƶ�ļ�")

    # ���ڲ��Ž���
    def change_time(self, num):
        self.player.setPosition(num)

    # ���
    def up_time(self):
        num = self.player.position() + int(self.player.duration() / 20)
        self.player.setPosition(num)

    # ����
    def down_time(self):
        num = self.player.position() - int(self.player.duration() / 20)
        self.player.setPosition(num)

    # ��ȡ��ý���������
    def get_time(self, num):
        self.timeSlider.setMaximum(self.player.duration())
        self.timeSlider.setValue(num)
        d = QDateTime.fromMSecsSinceEpoch(num).toString("mm:ss")
        all = self.player.duration()
        all_d = QDateTime.fromMSecsSinceEpoch(all).toString("mm:ss")

    def closeEvent(self, event):  # �ر�ǰ��Ҫself.player.pause()���������򱨴�
        self.player.pause()
        reply = QMessageBox.question(self, '��ʾ',
                                     "�Ƿ��˳�",
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


