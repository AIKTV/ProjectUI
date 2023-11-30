import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtMultimedia import QSound


class SoundPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('音频播放器')
        self.setGeometry(300, 300, 300, 150)

        self.recordPlayButton = QPushButton('播放', self)
        self.recordPlayButton.clicked.connect(self.play_sound_a)
        self.recordPlayButton.setGeometry(50, 50, 100, 50)
        self.recordPlayButton_status = '播放'

        self.handledPlayButton = QPushButton('播放', self)
        self.handledPlayButton.clicked.connect(self.play_sound_b)
        self.handledPlayButton.setGeometry(150, 50, 100, 50)
        self.handledPlayButton_status = '播放'

        self.audio_a = QSound('audio_a.wav')
        self.audio_b = QSound('audio_b.wav')

    def play_sound_a(self):
        if self.recordPlayButton_status == '播放':
            if self.handledPlayButton_status == '暂停':
                self.audio_b.stop()
                self.handledPlayButton.setText('播放')
                self.handledPlayButton_status = '播放'

            self.audio_a.play()
            self.recordPlayButton.setText('暂停')
            self.recordPlayButton_status = '暂停'
        else:
            self.audio_a.stop()
            self.recordPlayButton.setText('播放')
            self.recordPlayButton_status = '播放'

    def play_sound_b(self):
        if self.handledPlayButton_status == '播放':
            if self.recordPlayButton_status == '暂停':
                self.audio_a.stop()
                self.recordPlayButton.setText('播放')
                self.recordPlayButton_status = '播放'

            self.audio_b.play()
            self.handledPlayButton.setText('暂停')
            self.handledPlayButton_status = '暂停'
        else:
            self.audio_b.stop()
            self.handledPlayButton.setText('播放')
            self.handledPlayButton_status = '播放'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = SoundPlayer()
    player.show()
    sys.exit(app.exec_())
