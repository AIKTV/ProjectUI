import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("音频播放器")

        # 创建按钮对象
        self.play_button = QPushButton("播放", self)
        self.play_button.clicked.connect(self.play_audio)

        # 创建媒体播放器对象
        self.player = QMediaPlayer()

    def play_audio(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.play_button.setText("播放")
        else:
            audio_file = "D:\Matlab\5.wav"  # 替换为你的音频文件路径
            audio_url = QUrl.fromLocalFile(audio_file)
            audio_content = QMediaContent(audio_url)

            self.player.setMedia(audio_content)
            self.player.play()
            self.play_button.setText("暂停")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
