import sys
import warnings

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtMultimedia import QSound

warnings.filterwarnings("ignore", category=DeprecationWarning)

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

        self.audio_a = QSound(r"D:\Matlab\3.wav")
        self.audio_b = QSound(r"D:\Matlab\4.wav")

        self.audio_a_playing = False
        self.audio_b_playing = False

    def play_sound_a(self):
        if not self.audio_a_playing:
            if self.audio_b_playing:
                self.audio_b.stop()
                self.handledPlayButton.setText('播放')
                self.audio_b_playing = False

            self.audio_a.play()
            self.recordPlayButton.setText('暂停')
            self.audio_a_playing = True
        else:
            self.audio_a.stop()
            self.recordPlayButton.setText('播放')
            self.audio_a_playing = False

    def play_sound_b(self):
        if not self.audio_b_playing:
            if self.audio_a_playing:
                self.audio_a.stop()
                self.recordPlayButton.setText('播放')
                self.audio_a_playing = False

            self.audio_b.play()
            self.handledPlayButton.setText('暂停')
            self.audio_b_playing = True
        else:
            self.audio_b.stop()
            self.handledPlayButton.setText('播放')
            self.audio_b_playing = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = SoundPlayer()
    player.show()
    sys.exit(app.exec_())
