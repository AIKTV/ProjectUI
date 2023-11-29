import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QDir


class AudioPlayer(QMainWindow):
    def __init__(self, folder_path):
        super(AudioPlayer, self).__init__()
        self.folder_path = folder_path
        self.button = QPushButton("打开文件夹", self)
        self.button.setGeometry(150, 80, 100, 40)
        self.button.clicked.connect(self.open_folder)
    def open_folder(self):
        folder_path = QDir.toNativeSeparators(self.folder_path)  # 转换为本地平台的路径格式
        os.startfile(folder_path)  # 打开指定路径的文件夹

if __name__ == "__main__":
    app = QApplication(sys.argv)
    folder_path = "指定的目录路径"  # 在这里替换为你自己指定的目录路径
    player = AudioPlayer(folder_path)
    player.show()

    sys.exit(app.exec_())