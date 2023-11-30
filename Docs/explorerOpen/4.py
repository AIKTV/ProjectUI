import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtMultimedia import QSound


class SoundPlayer(QWidget):
    def __init__(self):
        super().__init__()  # 调用 QWidget 的初始化函数

        self.setWindowTitle('音频播放器')  # 设置窗口标题
        self.setGeometry(300, 300, 300, 150)  # 设置窗口大小和位置

        # 创建按钮 A，并连接点击事件到播放函数 play_sound_a
        self.button_a = QPushButton('播放', self)
        self.button_a.clicked.connect(self.play_sound_a)
        self.button_a.setGeometry(50, 50, 100, 50)  # 设置按钮 A 的位置和大小
        self.button_a_status = '播放'  # 初始化按钮 A 的状态为"播放"

        # 创建按钮 B，并连接点击事件到播放函数 play_sound_b
        self.button_b = QPushButton('播放', self)
        self.button_b.clicked.connect(self.play_sound_b)
        self.button_b.setGeometry(150, 50, 100, 50)  # 设置按钮 B 的位置和大小
        self.button_b_status = '播放'  # 初始化按钮 B 的状态为"播放"

        # 创建音频 A 和音频 B 对应的 QSound 对象
        self.audio_a = QSound('audio_a.wav')
        self.audio_b = QSound('audio_b.wav')

    # 播放音频 A 的函数
    def play_sound_a(self):
        if self.button_a_status == '播放':  # 如果按钮 A 的状态为"播放"
            if self.button_b_status == '暂停':  # 如果按钮 B 的状态为"暂停"
                self.audio_b.stop()  # 停止音频 B 的播放
                self.button_b.setText('播放')  # 修改按钮 B 的文本为"播放"
                self.button_b_status = '播放'  # 更新按钮 B 的状态为"播放"

            self.audio_a.play()  # 播放音频 A
            self.button_a.setText('暂停')  # 修改按钮 A 的文本为"暂停"
            self.button_a_status = '暂停'  # 更新按钮 A 的状态为"暂停"
        else:  # 如果按钮 A 的状态为"暂停"
            self.audio_a.stop()  # 停止音频 A 的播放
            self.button_a.setText('播放')  # 修改按钮 A 的文本为"播放"
            self.button_a_status = '播放'  # 更新按钮 A 的状态为"播放"

    # 播放音频 B 的函数
    def play_sound_b(self):
        if self.button_b_status == '播放':  # 如果按钮 B 的状态为"播放"
            if self.button_a_status == '暂停':  # 如果按钮 A 的状态为"暂停"
                self.audio_a.stop()  # 停止音频 A 的播放
                self.button_a.setText('播放')  # 修改按钮 A 的文本为"播放"
                self.button_a_status = '播放'  # 更新按钮 A 的状态为"播放"

            self.audio_b.play()  # 播放音频 B
            self.button_b.setText('暂停')  # 修改按钮 B 的文本为"暂停"
            self.button_b_status = '暂停'  # 更新按钮 B 的状态为"暂停"
        else:  # 如果按钮 B 的状态为"暂停"
            self.audio_b.stop()  # 停止音频 B 的播放
            self.button_b.setText('播放')  # 修改按钮 B 的文本为"播放"
            self.button_b_status = '播放'  # 更新按钮 B 的状态为"播放"


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建 QApplication 对象
    player = SoundPlayer()  # 创建音频播放器对象
    player.show()  # 显示音频播放器窗口
    sys.exit(app.exec_())  # 进入主循环，等待用户的操作，并在退出时释放资源
