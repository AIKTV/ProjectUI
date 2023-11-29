import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDir

from mainwindow import Ui_MainWindow  # 导入从UI文件生成的Python类


class AudioPlayer(QMainWindow):
    def __init__(self, folder_path):
        super(AudioPlayer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 初始化UI界面
        self.ui.pushButton.clicked.connect(self.open_folder)  # 点击按钮连接到open_folder函数
        self.folder_path = folder_path

    def open_folder(self):
        folder_path = QDir.toNativeSeparators(self.folder_path)  # 转换为本地平台的路径格式
        os.startfile(folder_path)  # 打开指定路径的文件夹

    def run(self):
        app = QApplication(sys.argv)  # 创建Qt应用程序
        self.show()  # 显示主窗口
        sys.exit(app.exec_())  # 运行应用程序，并进入事件循环


if __name__ == "__main__":
    folder_path = "指定的目录路径"  # 在这里替换为你自己指定的目录路径
    player = AudioPlayer(folder_path)
    player.run()

