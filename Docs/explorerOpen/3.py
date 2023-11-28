#将导出文件（音频）放入已经指定了的目录（在代码中指定）然后在UI界面设计一个小按钮 点击就立即播放指定文件夹中的导出文件（音频）
ifrom PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer
from generated_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 加载UI界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 连接按钮的信号槽
        self.ui.playButton.clicked.connect(self.playAudio)

    def playAudio(self):
        # 指定导出文件夹路径
        export_folder = "指定的文件夹路径"

        # 创建MediaPlayer对象
        player = QMediaPlayer()

        # 设置音频文件路径
        audio_file = f"{export_folder}/导出文件名.wav"  # 根据实际情况修改文件名和格式
        player.setMedia(QMediaContent.fromUrl(QUrl.fromLocalFile(audio_file)))

        # 播放音频
        player.play()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
