import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtMultimedia import QSound


class SoundPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('音频播放器')
        self.setGeometry(300, 300, 300, 150)

        self.button_a = QPushButton('播放', self)
        self.button_a.clicked.connect(self.play_sound_a)
        self.button_a.setGeometry(50, 50, 100, 50)
        self.button_a_status = '播放'

        self.button_b = QPushButton('播放', self)
        self.button_b.clicked.connect(self.play_sound_b)
        self.button_b.setGeometry(150, 50, 100, 50)
        self.button_b_status = '播放'

        self.audio_a = QSound('audio_a.wav')
        self.audio_b = QSound('audio_b.wav')

    def play_sound_a(self):
        if self.button_a_status == '播放':
            if self.button_b_status == '暂停':
                self.audio_b.stop()
                self.button_b.setText('播放')
                self.button_b_status = '播放'

            self.audio_a.play()
            self.button_a.setText('暂停')
            self.button_a_status = '暂停'
        else:
            self.audio_a.stop()
            self.button_a.setText('播放')
            self.button_a_status = '播放'

    def play_sound_b(self):
        if self.button_b_status == '播放':
            if self.button_a_status == '暂停':
                self.audio_a.stop()
                self.button_a.setText('播放')
                self.button_a_status = '播放'

            self.audio_b.play()
            self.button_b.setText('暂停')
            self.button_b_status = '暂停'
        else:
            self.audio_b.stop()
            self.button_b.setText('播放')
            self.button_b_status = '播放'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = SoundPlayer()
    player.show()
    sys.exit(app.exec_())
