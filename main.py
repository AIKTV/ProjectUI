import warnings
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import QProcess
from AIKTVUI import Ui_MainWindow
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
from pydub import AudioSegment
from pydub.playback import play
import os
import time
import threading
import wave
import pyaudio
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)
from PyQt5.QtCore import QTimer
from PyQt5.QtMultimedia import QSound  # 导入PyQt5库中的QSound类


warnings.filterwarnings("ignore", category=DeprecationWarning)

recordFileAddress = r""  # 录音/原始文件地址
handledFileAddress = r""  # 处理后文件地址
record_file_path = recordFileAddress  #录音文件地址record_file_path，用于录音子模块中

if_enhance = 'n'


class MainForm(QMainWindow, Ui_MainWindow):
    """正式文件 MainForm class"""

    def __init__(self):
        """使用的控件相关触发器全放这里"""

        super(MainForm, self).__init__()
        self.setupUi(self)
        self.chooseRecord.clicked.connect(
            lambda: self.openfiledialog('record', 'WAV波形文件(*.wav)'))
        self.chooseHandled.clicked.connect(
            lambda: self.openfiledialog('handled', 'WAV无损音频文件(*.wav)'))
        self.configButton.clicked.connect(self.openConfigDialog)
        self.dialog = None  # 对话框对象
        self.recordButton.clicked.connect(self.start_recording)
        self.pauseRecordButton.clicked.connect(self.stop_recording)
        self.recording = False
        self.record_file_path = ''
        self.counter = 0

        self.player_a = QMediaPlayer()
        self.player_b = QMediaPlayer()

        self.recordPlayButton.clicked.connect(self.play_record_a)
        self.recordStopButton.clicked.connect(self.pause_record_a)
        self.handledPlayButton.clicked.connect(self.play_record_b)
        self.handledStopButton.clicked.connect(self.pause_record_b)

        self.time_slider.setMinimum(0)
        self.time_slider.setMaximum(100)
        self.time_slider.sliderMoved.connect(self.time_slider_moved)
        self.time_slider.sliderReleased.connect(self.time_slider_released)

        self.current_time_label = QLabel("00:00", self)
        self.current_time_label.setGeometry(420, 100, 100, 920)

        self.total_time_label = QLabel("00:00", self)
        self.total_time_label.setGeometry(480, 100, 60, 920)

        # 创建定时器，用于更新进度条位置和时间显示
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time_slider_position)
        self.timer.start(100)

        self.paused_position_a = 0
        self.paused_position_b = 0

    def play_record_a(self):
        # 确保只有一个音频在播放
        global recordFileAddress
        self.player_a.setMedia(QMediaContent(QUrl.fromLocalFile(recordFileAddress)))
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
        global handledFileAddress
        self.player_b.setMedia(QMediaContent(QUrl.fromLocalFile(handledFileAddress)))
        self.stop_all_players()
        self.player_b.play()

    def pause_record_b(self):
        if self.player_b.state() == QMediaPlayer.PlayingState:
            self.paused_position_b = self.player_b.position()
            self.player_b.pause()
        elif self.player_b.state() == QMediaPlayer.PausedState:
            self.player_b.setPosition(self.paused_position_b)
            self.player_b.play()

    def update_time_slider_position(self):
        global recordFileAddress
        global handledFileAddress
        if self.player_a.state() == QMediaPlayer.PlayingState:
            pos_a = self.player_a.position()
            duration_a = self.player_a.duration()
            if duration_a != 0:
                self.time_slider.setValue(pos_a * 100 / duration_a)
                current_time_a = self.milliseconds_to_time(pos_a)
                total_time_a = self.milliseconds_to_time(duration_a)
                self.current_time_label.setText(current_time_a)
                self.total_time_label.setText(total_time_a)

        elif self.player_b.state() == QMediaPlayer.PlayingState:
            pos_b = self.player_b.position()
            duration_b = self.player_b.duration()
            if duration_b != 0:
                self.time_slider.setValue(pos_b * 100 / duration_b)
                current_time_b = self.milliseconds_to_time(pos_b)
                total_time_b = self.milliseconds_to_time(duration_b)
                self.current_time_label.setText(current_time_b)
                self.total_time_label.setText(total_time_b)


    def milliseconds_to_time(self, ms):
        seconds = int(ms / 1000)
        minutes = int(seconds / 60)
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    def time_slider_moved(self):
        value = self.time_slider.value()
        if self.player_a.state() != QMediaPlayer.StoppedState:
            duration = self.player_a.duration()
            position = int(value / 100 * duration)
            self.player_a.setPosition(position)
        elif self.player_b.state() != QMediaPlayer.StoppedState:
            duration = self.player_b.duration()
            position = int(value / 100 * duration)
            self.player_b.setPosition(position)

    def time_slider_released(self):
        if self.player_a.state() == QMediaPlayer.PlayingState:
            self.player_a.play()
        elif self.player_b.state() == QMediaPlayer.PlayingState:
            self.player_b.play()

    def stop_all_players(self):
        self.player_a.stop()
        self.player_b.stop()



    def start_recording(self):
        #开始模块
        self.recording = True
        #设置recording为True，表示正在录音
        self.counter += 1
        # counter加1，用于生成唯一的文件名。
        current_time = time.strftime("%m%d-%H%M")
        # 修改文件存放路径为新的位置，包括当前时间、计数器和文件扩展名。
        self.record_file_path = f"E:/Projects/Python/ProjectUI/AI-barbara-4.1-Stable-fcpe/raw/record-{current_time}-{self.counter}.wav"
        threading.Thread(target=self._record).start()  #启动一个新的线程，调用_record方法开始录音。

    def stop_recording(self):            #停止录音模块
        self.recording = False      #设置recording为False，表示停止录音
        self.display_recent_recording_box()

    def display_recent_recording_box(self):         #录音文件保存路径显示5秒
        recent_file = self.record_file_path
        max_line_length = 20
        #      使显示路径分成两行，可以根据需要调整每行的最大字符数
        split_index = max_line_length
        while split_index < len(recent_file) and recent_file[split_index] != "/":
            split_index += 1

        if split_index < len(recent_file):
            display_path = recent_file[:split_index] + "\n" + recent_file[split_index:]
        else:
            display_path = recent_file
        self.recordOutputDisplay.setText(display_path)            #显示
        self.recordOutputDisplay.show()
        QTimer.singleShot(5000, self.recordOutputDisplay.hide)       #更改秒数，例如5000表示5秒，依次类推

    def _update_time(self):
        seconds = 0
        while self.recording:
            self.recordTimeDisplay.setText(time.strftime('%M:%S', time.gmtime(seconds)))
            time.sleep(1)
            seconds += 1
    #这段代码是一个用于更新录音时间显示的方法。它包括以下步骤：
    # 首先将秒数设置为0。
    # 在录音状态下，循环执行以下操作：
    # 使用time.strftime函数将秒数格式化为"分:秒"的字符串，并将其显示在录音时间的UI元素上。
    # 休眠1秒钟，以便时间能够递增。秒数加1，用于计算录音的总时长。
    # 这个方法的作用是在录音过程中实时更新录音时间的显示，让用户能够清楚地看到录音的时长

    def _record(self):
        CHUNK = 1024  # 每次读取的数据块大小
        FORMAT = pyaudio.paInt16  # 音频格式为16位整型
        CHANNELS = 2  # 声道数为2
        RATE = 44100  # 采样率为44100Hz
        RECORD_SECONDS = 10  # 录音时长为10秒

        audio = pyaudio.PyAudio()  # 创建PyAudio对象，用于音频输入和输出

        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)  # 打开音频输入流，设置格式、声道数、采样率等参数

        frames = []  # 用于存储录音数据的列表

        t = threading.Thread(target=self._update_time)  # 创建一个新线程，调用self._update_time方法实时更新录音时间的显示
        t.start()  # 启动线程

        while self.recording:  # 在录音状态下，循环执行以下操作
            data = stream.read(CHUNK)  # 从音频输入流中读取一块数据
            frames.append(data)  # 将数据添加到frames列表中

        stream.stop_stream()  # 停止音频输入流
        stream.close()  # 关闭音频输入流
        audio.terminate()  # 终止PyAudio对象

        t.join()  # 等待线程t结束

        wf = wave.open(self.record_file_path, 'wb')  # 创建并打开录音文件
        wf.setnchannels(CHANNELS)  # 设置文件的通道数
        wf.setsampwidth(audio.get_sample_size(FORMAT))  # 设置文件的采样宽度
        wf.setframerate(RATE)  # 设置文件的采样率
        wf.writeframes(b''.join(frames))  # 将frames列表中的音频数据写入录音文件
        wf.close()  # 关闭录音文件




    def getTotalTime(self, d):
        # .设置时间进度条的进度值和正在播放的音频总时长一致
        self.time_slider.setRange(0, d)

        seconds = int(d / 1000)
        # 获取时长的分钟
        minutes = int(seconds / 60)
        seconds = seconds - -minutes * 60
        str_time1 = ""
        if minutes < 10:
            str_time1 = str_time1 + "0" + str(minutes)
        else:
            str_time1 = str_time1 + str(minutes)
        str_time1 = str_time1 + ":"
        if seconds < 10:
            str_time1 = str_time1 + "0" + str(seconds)
        else:
            str_time1 = str_time1 + str(seconds)

        # 把分钟和秒设置在时间标签中显示
        b = str_time1
        self.time_lbl_2.setText(f"{b}")





    # 自定义函数，获取播放音频的当前时长，参数p保存的是音频当前时长（毫秒）
    def getCurrentTime(self, p):
        # 设置时长进度条的当前进度
        self.time_slider.setValue(p)
        # 获取时长的秒
        seconds = int(p / 1000)
        # 获取时长的分钟
        minutes = int(seconds / 60)
        seconds = seconds - -minutes * 60
        str_time = ""
        if minutes < 10:
            str_time = str_time + "0" + str(minutes)
        else:
            str_time = str_time + str(minutes)
        str_time = str_time + ":"
        if seconds < 10:
            str_time = str_time + "0" + str(seconds)
        else:
            str_time = str_time + str(seconds)

        # 把分钟和秒设置在时间标签中显示
        a = str_time + "   /"
        self.time_lbl.setText(f"{a}")




    def openfiledialog(self, button, type):
        global recordFileAddress
        global handledFileAddress  # 声明全局变量
        if button == 'record':
            typetext = '录音/原始'
        else:
            typetext = '要播放的'
        fileaddress, filetype = QtWidgets.QFileDialog.getOpenFileName(
            self, "选择" + typetext + "文件", os.getcwd(), type)
        if fileaddress:  # 如果文件名非空
            if button == 'record':  # 传递的类型为record 录音/原始文件
                self.recordAddress.setText(
                    os.path.basename(fileaddress))  # 设置文本框内容
                recordFileAddress = fileaddress  # 更新全局变量的值
            # if button == 'handled':  # 传递的类型为handled 处理后文件
            else:
                self.handledAddress.setText(os.path.basename(fileaddress))
                handledFileAddress = fileaddress

    def openConfigDialog(self):
        global dialog
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("AI模型配置")
        layout = QtWidgets.QVBoxLayout(dialog)

        self.model_name_label = QLabel("请选择使用的模型:")
        self.model_name_combobox = QComboBox()
        self.model_name_combobox.addItem("Furina")
        self.model_name_combobox.addItem("Neuvillette")
        layout.addWidget(self.model_name_label)
        layout.addWidget(self.model_name_combobox)

        self.key_num_label = QLabel("请输入音高（例：维持原调为0，支持正负，数字为半音）")
        self.key_num_edit = QLineEdit()
        layout.addWidget(self.key_num_label)
        layout.addWidget(self.key_num_edit)

        self.f0_predictor_label = QLabel("请选择使用的F0预测器，0为crepe，1为pm，2为dio，3为harvest，4为rmvpe，5为fcpe")
        self.f0_predictor_combobox = QComboBox()
        self.f0_predictor_combobox.addItem('crepe')
        self.f0_predictor_combobox.addItem('pm')
        self.f0_predictor_combobox.addItem('dio')
        self.f0_predictor_combobox.addItem('harvest')
        self.f0_predictor_combobox.addItem('rmvpe')
        self.f0_predictor_combobox.addItem('fcpe')
        layout.addWidget(self.f0_predictor_label)
        layout.addWidget(self.f0_predictor_combobox)

        self.if_diffusion_label = QLabel("是否使用浅层扩散模型？使用后可解决一部分电音问题（推荐）\n请注意该模型需先单独训练好（y/n）")
        self.if_diffusion_switch = QComboBox()
        self.if_diffusion_switch.addItems(['y', 'n'])
        layout.addWidget(self.if_diffusion_label)
        layout.addWidget(self.if_diffusion_switch)

        self.if_feature_retrieval_label = QLabel("是否使用特征检索？特征检索可以减小音色泄露，并且不是非常影响咬字\n请注意该模型需先单独训练好（y/n）")
        self.if_feature_retrieval_switch = QComboBox()
        self.if_feature_retrieval_switch.addItems(['y', 'n'])
        layout.addWidget(self.if_feature_retrieval_label)
        layout.addWidget(self.if_feature_retrieval_switch)

        self.cluster_ratio_label = QLabel("请输入特征检索占比，范围 0-1（例：0为不使用）")
        self.cluster_ratio_slider = QSlider()
        self.cluster_ratio_slider.setOrientation(Qt.Horizontal)
        self.cluster_ratio_slider.setMinimum(0)
        self.cluster_ratio_slider.setMaximum(10)
        self.cluster_ratio_slider.setValue(5)  # 设置默认值，可以根据需要调整
        layout.addWidget(self.cluster_ratio_label)
        layout.addWidget(self.cluster_ratio_slider)

        self.if_auto_predict_f0_label = QLabel("是否使用自动音高预测？推荐语音转换开启，歌声转换开启会严重跑调（y/n）")
        self.if_auto_predict_f0_switch = QComboBox()
        self.if_auto_predict_f0_switch.addItems(['n', 'y'])
        layout.addWidget(self.if_auto_predict_f0_label)
        layout.addWidget(self.if_auto_predict_f0_switch)

        self.if_clip_label = QLabel("是否使用音频强制切片？单位为秒（例：0为自动切片，10为强制10秒切一段）")
        self.if_clip_edit = QLineEdit()
        layout.addWidget(self.if_clip_label)
        layout.addWidget(self.if_clip_edit)

        self.if_linear_gradient_label = QLabel("请输入两段音频切片的交叉淡入长度，单位为秒")
        self.if_linear_gradient_edit = QLineEdit()
        layout.addWidget(self.if_linear_gradient_label)
        layout.addWidget(self.if_linear_gradient_edit)

        start_button = QtWidgets.QPushButton("开始转换")
        start_button.clicked.connect(self.start_conversion)
        layout.addWidget(start_button)
        dialog.exec_()  # 显示对话框


    def start_conversion(self):
        global recordFileAddress
        model_name = self.model_name_combobox.currentText()
        if recordFileAddress:                                         # 将地址传递给 self.wav_name_edit
            wav_name = recordFileAddress.split('/')[-1].split('.')[0]
        key_num = self.key_num_edit.text()
        f0_predictor = self.f0_predictor_combobox.currentText()
        if_diffusion = self.if_diffusion_switch.currentText()
        diffusion_name = '10000'
        if model_name == 'Furina':
            diffusion_k_step = '20'
        else:
            diffusion_k_step = '100'
        if_feature_retrieval = self.if_feature_retrieval_switch.currentText()
        cluster_ratio = self.cluster_ratio_slider.value() / 10.0
        if_auto_predict_f0 = self.if_auto_predict_f0_switch.currentText()
        if_clip = self.if_clip_edit.text()
        if_linear_gradient = self.if_linear_gradient_edit.text()

        inference_case = r'.\env\python.exe inference_main.py'
        inference_case = inference_case + f' -m "logs/44k/{model_name}.pth" -c "configs/config.json" -n "{wav_name}" -t {key_num} -s "barbara" -f0p {f0_predictor}'

        if if_diffusion == 'y':
            inference_case = inference_case + f' -shd -dm "logs/44k/diffusion/model_{diffusion_name}.pt" -ks {diffusion_k_step}'
        if if_feature_retrieval == 'y':
            inference_case = inference_case + f' --feature_retrieval -cr {cluster_ratio}'
        if if_auto_predict_f0 == 'y':
            inference_case = inference_case + f' -a'

        inference_case = inference_case + f' -cl {if_clip} -lg {if_linear_gradient}'

        process = QProcess()
        process.start(inference_case)
        process.waitForFinished()
        process.close()
        process.deleteLater()
        QtWidgets.QMessageBox.information(self,"转换完成","转换已完成！")
        if dialog:  # 检查对话框对象是否存在
            dialog.close()  # 关闭对话框

    def play_sound_a(self):
        if self.recordPlayButton.text() == '播放':
            if self.handledPlayButton.text() == '暂停':
                self.player_b.stop()
                self.handledPlayButton.setText('播放')
            self.player_a.play()
            self.recordPlayButton.setText('暂停')
        else:
            self.player_a.pause()
            self.recordPlayButton.setText('播放')

    def play_sound_b(self):
        if self.handledPlayButton.text() == '播放':
            if self.recordPlayButton.text() == '暂停':
                self.player_a.pause()
                self.recordPlayButton.setText('播放')
            self.player_b.play()
            self.handledPlayButton.setText('暂停')
        else:
            self.player_b.pause()
            self.handledPlayButton.setText('播放')

    def update_slider_position(self):
        if self.recordPlayButton.text() == '暂停':
            pos_a = self.player_a.position() * 100 / self.player_a.duration()
            self.slider.setValue(pos_a)
        elif self.handledPlayButton.text() == '暂停':
            pos_b = self.player_b.position() * 100 / self.player_b.duration()
            self.slider.setValue(pos_b)

    def slider_moved(self):
        value = self.slider.value()
        if self.recordPlayButton.text() == '暂停':
            duration = self.player_a.duration()
            position = int(value / 100 * duration)
            self.player_a.setPosition(position)
        elif self.handledPlayButton.text() == '暂停':
            duration = self.player_b.duration()
            position = int(value / 100 * duration)
            self.player_b.setPosition(position)

    def slider_released(self):
        if self.recordPlayButton.text() == '暂停':
            self.player_a.play()
        elif self.handledPlayButton.text() == '暂停':
            self.player_b.play()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
