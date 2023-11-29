class AudioPlayer(QMainWindow):
    def __init__(self, folder_path):
        super(AudioPlayer, self).__init__()
        self.folder_path = folder_path
        self.button = QPushButton("打开文件夹", self)
        self.button.setGeometry(150, 80, 100, 40)
        self.button.clicked.connect(self.open_folder)

        self.progress_bar = QProgressBar(self)  # 创建一个进度条实例
        self.progress_bar.setGeometry(50, 150, 300, 20)  # 设置进度条在窗口中的位置和大小

        self.timer = QBasicTimer()  # 创建一个基本定时器实例
        self.step = 0  # 初始化进度条值

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()  # 如果进度条已经满，则停止计时器
            return

        self.step += 1  # 增加进度条值
        self.progress_bar.setValue(self.step)  # 更新进度条的显示值

    def open_folder(self):
        folder_path = QDir.toNativeSeparators(self.folder_path)  # 转换为本地平台的路径格式
        os.startfile(folder_path)  # 打开指定路径的文件夹

        self.step = 0  # 重置进度条值
        self.timer.start(100, self)  # 启动定时器，每100ms更新一次进度条


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建应用程序实例
    folder_path = "D:\新建文件夹"  # 在这里替换为你自己指定的目录路径
    player = AudioPlayer(folder_path)  # 创建音频播放器实例，传入文件夹路径
    player.show()  # 显示音频播放器窗口

    sys.exit(app.exec_())  # 运行应用程序的事件循环，直到程序退出

