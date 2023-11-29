import sys
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.player = QMediaPlayer()  # 创建音频播放器对象
        self.audio_file = "path_to_your_audio_file.wav"# 替换为您的音频文件路径

        self.button = QPushButton("A", self)
        self.button.clicked.connect(self.toggle_playback)  # 绑定按钮点击事件

        self.setCentralWidget(self.button)

    def toggle_playback(self):
        if self.button.text() == "A":
            media = QMediaContent(QUrl.fromLocalFile(self.audio_file))
            self.player.setMedia(media)
            self.player.play()
            self.button.setText("C")
        else:
            self.player.pause()
            self.button.setText("A")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

