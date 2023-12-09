import sys  # 导入sys模块
import warnings

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton  # 导入PyQt5库中的QApplication、QWidget、QPushButton类
from PyQt5.QtMultimedia import QSound  # 导入PyQt5库中的QSound类

warnings.filterwarnings("ignore", category=DeprecationWarning)

class SoundPlayer(QWidget):  # 定义一个名为SoundPlayer的继承自QWidget的类
    def __init__(self):  # 类的构造函数
        super().__init__()  # 调用父类QWidget的构造函数

        self.setWindowTitle('音频播放器')  # 设置窗口标题
        self.setGeometry(300, 300, 300, 150)  # 设置窗口大小和位置

        self.recordPlayButton = QPushButton('播放', self)  # 创建一个名为recordPlayButton的按钮，并连接到self对象上
        self.recordPlayButton.clicked.connect(self.play_sound_a)  # 将recordPlayButton的clicked信号连接到play_sound_a方法上
        self.recordPlayButton.setGeometry(50, 50, 100, 50)  # 设置recordPlayButton在窗口中的位置和大小
        self.recordPlayButton_status = '播放'  # 记录recordPlayButton的状态

        self.handledPlayButton = QPushButton('播放', self)  # 创建一个名为handledPlayButton的按钮，并连接到self对象上
        self.handledPlayButton.clicked.connect(self.play_sound_b)  # 将handledPlayButton的clicked信号连接到play_sound_b方法上
        self.handledPlayButton.setGeometry(150, 50, 100, 50)  # 设置handledPlayButton在窗口中的位置和大小
        self.handledPlayButton_status = '播放'  # 记录handledPlayButton的状态

        self.audio_a = QSound(r"D:\Matlab\3.wav")  # 创建一个名为audio_a的QSound对象，用于播放audio_a.wav音频文件
        self.audio_b = QSound(r"D:\Matlab\4.wav")  # 创建一个名为audio_b的QSound对象，用于播放audio_b.wav音频文件

    def play_sound_a(self):  # 播放audio_a.wav音频文件的方法
        if self.recordPlayButton_status == '播放':  # 如果recordPlayButton处于"播放"状态
            if self.handledPlayButton_status == '暂停':  # 如果handledPlayButton处于"暂停"状态
                self.audio_b.stop()  # 停止播放audio_b.wav音频文件
                self.handledPlayButton.setText('播放')  # 修改handledPlayButton的文本为"播放"
                self.handledPlayButton_status = '播放'  # 修改handledPlayButton的状态为"播放"

            self.audio_a.play()  # 播放audio_a.wav音频文件
            self.recordPlayButton.setText('暂停')  # 修改recordPlayButton的文本为"暂停"
            self.recordPlayButton_status = '暂停'  # 修改recordPlayButton的状态为"暂停"
        else:  # 如果recordPlayButton处于"暂停"状态
            self.audio_a.stop()  # 停止播放audio_a.wav音频文件
            self.recordPlayButton.setText('播放')  # 修改recordPlayButton的文本为"播放"
            self.recordPlayButton_status = '播放'  # 修改recordPlayButton的状态为"播放"

    def play_sound_b(self):  # 播放audio_b.wav音频文件的方法
        if self.handledPlayButton_status == '播放':  # 如果handledPlayButton处于"播放"状态
            if self.recordPlayButton_status == '暂停':  # 如果recordPlayButton处于"暂停"状态
                self.audio_a.stop()  # 停止播放audio_a.wav音频文件
                self.recordPlayButton.setText('播放')  # 修改recordPlayButton的文本为"播放"
                self.recordPlayButton_status = '播放'  # 修改recordPlayButton的状态为"播放"

            self.audio_b.play()  # 播放audio_b.wav音频文件
            self.handledPlayButton.setText('暂停')  # 修改handledPlayButton的文本为"暂停"
            self.handledPlayButton_status = '暂停'  # 修改handledPlayButton的状态为"暂停"
        else:  # 如果handledPlayButton处于"暂停"状态
            self.audio_b.stop()  # 停止播放audio_b.wav音频文件
            self.handledPlayButton.setText('播放')  # 修改handledPlayButton的文本为"播放"
            self.handledPlayButton_status = '播放'  # 修改handledPlayButton的状态为"播放"


if __name__ == '__main__':  # 如果当前运行的文件是主程序
    app = QApplication(sys.argv)  # 创建一个QApplication对象
    player = SoundPlayer()  # 创建一个名为player的SoundPlayer对象
    player.show()  # 显示player窗口
    sys.exit(app.exec_())  # 进入主循环，等待用户操作，并在退出时释放资源
