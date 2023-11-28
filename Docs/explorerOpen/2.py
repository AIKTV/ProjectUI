#按钮点击播放导出文件
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Play Exported File")

        # 创建按钮
        self.play_button = QPushButton("Play", self)
        self.play_button.setGeometry(10, 10, 80, 30)
        self.play_button.clicked.connect(self.play_exported_file)

    def play_exported_file(self):
        # 指定导出文件路径
        exported_file_path = r'"D:\目标文件夹\6.wav"'

        # 播放导出文件
        QDesktopServices.openUrl(QUrl.fromLocalFile(exported_file_path))


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

#在这段代码中，我们创建了一个MainWindow类继承自QMainWindow，并在其中添加了一个小按钮。按钮的位置和大小通过setGeometry方法进行设置。
#按钮的clicked信号与play_exported_file槽连接，当按钮被点击时，会调用play_exported_file方法。在play_exported_file方法中，我们指定了导出文件的路径，并使用QDesktopServices.openUrl方法来播放导出文件。
#请将exported_file_path变量替换为实际的导出文件路径。确保已经安装了PyQt库。运行代码后，将会显示一个包含小按钮的主窗口，点击按钮即可播放导出文件。