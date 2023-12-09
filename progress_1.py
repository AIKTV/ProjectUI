import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSlider, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QTimer, QUrl

class SoundPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('音频播放器')
        self.setGeometry(300, 300, 500, 200)

        # 播放和暂停录音A的按钮
        self.recordPlayButton = QPushButton('播放录音A', self)
        self.recordPlayButton.setGeometry(20, 20, 120, 30)
        self.recordPlayButton.clicked.connect(self.play_record_a)

        self.recordPauseButton = QPushButton('暂停录音A', self)
        self.recordPauseButton.setGeometry(150, 20, 120, 30)
        self.recordPauseButton.clicked.connect(self.pause_record_a)

        # 播放和暂停录音B的按钮
        self.handledPlayButton = QPushButton('播放录音B', self)
        self.handledPlayButton.setGeometry(20, 60, 120, 30)
        self.handledPlayButton.clicked.connect(self.play_record_b)

        self.handledPauseButton = QPushButton('暂停录音B', self)
        self.handledPauseButton.setGeometry(150, 60, 120, 30)
        self.handledPauseButton.clicked.connect(self.pause_record_b)

        # 音频进度条和时间显示
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(20, 100, 350, 30)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.sliderMoved.connect(self.slider_moved)
        self.slider.sliderReleased.connect(self.slider_released)

        self.current_time_label = QLabel("00:00", self)
        self.current_time_label.setGeometry(380, 100, 60, 30)

        self.total_time_label = QLabel("00:00", self)
        self.total_time_label.setGeometry(440, 100, 60, 30)

        # 创建两个音频播放器
        self.player_a = QMediaPlayer()
        self.player_a.setMedia(QMediaContent(QUrl.fromLocalFile("D:/ai/9.wav")))
        self.player_b = QMediaPlayer()
        self.player_b.setMedia(QMediaContent(QUrl.fromLocalFile("D:/ai/test.wav")))

        # 创建定时器，用于更新进度条位置和时间显示
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_slider_position)
        self.timer.start(100)

        self.paused_position_a = 0
        self.paused_position_b = 0

    def play_record_a(self):
        # 确保只有一个音频在播放
        self.stop_all_players()
        self.player_a.play()

    def pause_record_a(self):
        if self.player_a.state() == QMediaPlayer.PlayingState:
            self.paused_position_a = self.player_a.position()
            self.player_a.pause()
        elif self.player_a.state() == QMediaPlayer.PausedState:
            self.player_a.setPosition(self.paused_position_a)
            self.player_a.play()

    def play_record_b(self):
        self.stop_all_players()
        self.player_b.play()

    def pause_record_b(self):
        if self.player_b.state() == QMediaPlayer.PlayingState:
            self.paused_position_b = self.player_b.position()
            self.player_b.pause()
        elif self.player_b.state() == QMediaPlayer.PausedState:
            self.player_b.setPosition(self.paused_position_b)
            self.player_b.play()

    def update_slider_position(self):
        if self.player_a.state() == QMediaPlayer.PlayingState:
            pos_a = self.player_a.position()
            duration_a = self.player_a.duration()
            self.slider.setValue(pos_a * 100 / duration_a)

            current_time_a = self.milliseconds_to_time(pos_a)
            total_time_a = self.milliseconds_to_time(duration_a)
            self.current_time_label.setText(current_time_a)
            self.total_time_label.setText(total_time_a)

        elif self.player_b.state() == QMediaPlayer.PlayingState:
            pos_b = self.player_b.position()
            duration_b = self.player_b.duration()
            self.slider.setValue(pos_b * 100 / duration_b)

            current_time_b = self.milliseconds_to_time(pos_b)
            total_time_b = self.milliseconds_to_time(duration_b)
            self.current_time_label.setText(current_time_b)
            self.total_time_label.setText(total_time_b)

    def milliseconds_to_time(self, ms):
        seconds = int(ms / 1000)
        minutes = int(seconds / 60)
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    def slider_moved(self):
        value = self.slider.value()
        if self.player_a.state() != QMediaPlayer.StoppedState:
            duration = self.player_a.duration()
            position = int(value / 100 * duration)
            self.player_a.setPosition(position)
        elif self.player_b.state() != QMediaPlayer.StoppedState:
            duration = self.player_b.duration()
            position = int(value / 100 * duration)
            self.player_b.setPosition(position)

    def slider_released(self):
        if self.player_a.state() == QMediaPlayer.PlayingState:
            self.player_a.play()
        elif self.player_b.state() == QMediaPlayer.PlayingState:
            self.player_b.play()

    def stop_all_players(self):
        self.player_a.stop()
        self.player_b.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = SoundPlayer()
    player.show()
    sys.exit(app.exec_())
