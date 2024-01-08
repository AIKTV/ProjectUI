class MainForm(QMainWindow, Ui_MainWindow):
    """正式文件 MainForm class"""

    def __init__(self):
        """使用的控件相关触发器全放这里"""
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.chooseRecord.clicked.connect(
            lambda: self.openfiledialog('record'))
        self.chooseHandled.clicked.connect(
            lambda: self.openfiledialog('handled'))
        self.recordPlayButton.clicked.connect(
            self.play_sound_a)
        self.handledPlayButton.clicked.connect(
            self.play_sound_b)
        self.a = '暂停'  # 记录recordPlayButton的状态
        self.b = '暂停'  # 记录handledPlayButton的状态
        self.audio_a = QSound(r"D:\Matlab\3.wav")  # 创建一个名为audio_a的QSound对象，用于播放audio_a.wav音频文件
        self.audio_b = QSound(r"D:\Matlab\4.wav")  # 创建一个名为audio_b的QSound对象，用于播放audio_b.wav音频文件
    def play_sound_a(self):
        if self.a == '暂停':  #
            if self.b == '播放':
                self.audio_b.stop()
                self.handledPlayButton.setText('播放')  # 修改handledPlayButton的文本为"播放"
                self.b = '播放'  # 修改handledPlayButton的状态为"播放"

            self.audio_a.play()  # 播放audio_a.wav音频文件
            self.recordPlayButton.setText('暂停')  # 修改recordPlayButton的文本为"暂停"
            self.a = '暂停'  # 修改recordPlayButton的状态为"暂停"
        else:  # 如果recordPlayButton处于"暂停"状态
            self.audio_a.stop()  # 停止播放audio_a.wav音频文件
            self.recordPlayButton.setText('播放')  # 修改recordPlayButton的文本为"播放"
            self.a = '播放'  # 修改recordPlayButton的状态为"播放"