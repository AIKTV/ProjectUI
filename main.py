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

        self.recordPlayButton.clicked.connect(
            self.play_sound_a)
        self.handledPlayButton.clicked.connect(
            self.play_sound_b)
        self.recordPlayButton_status = '暂停'  # 记录recordPlayButton的状态
        self.handledPlayButton_status = '暂停'  # 记录handledPlayButton的状态

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

    def myWindowInit(self):
        # 创建播放列表对象（窗体属性）
        self.playList = QMediaPlaylist()
        # 初始化播放列表对象的播放模式Loop(顺序播放）
        self.playList.setPlaybackMode(QMediaPlaylist.Loop)
        # 创建播放器对象（窗体属性）
        self.player = QMediaPlayer()
        # 初始化播放器的播放音量最大
        self.player.setVolume(100)
        # 设置播放器的播放列表
        self.player.setPlaylist(self.playList)
        # 创建列表对像（窗体属性）
        self.musicNames = []
        # 设置按钮的提示信息
        self.play_btn.setToolTip("播放")
        self.mode_btn.setToolTip("顺序播放")
        # 给播放按钮的单击信号（clicke)调用函数musicPlay
        self.play_btn.clicked.connect(self.musicPlay)
        # 给播放器的播放音频持续时长改变信号（durationChang)调用getTotalTime
        self.player.durationChanged.connect(self.getTotalTime)
        # 给播放器的当前播放位置更改信号（positionChanged)调用getCurrentTime
        self.player.positionChanged.connect(self.getCurrentTime)
        # 给时间进度条的拖拽移动（sliderMoved)调用自主定义函数timeChanfed
        self.time_slider.sliderMoved.connect(self.timeChanged)
        # 给模式按钮点击（clicked信号）调用自定义函数modeChanged
        self.mode_btn.clicked.connect(self.modeChanged)


    def modeChanged(self):
        # 判断播放列表的播放模式是否是顺序播放
        if self.playList.playbackMode() == QMediaPlaylist.Loop:
            # 1)更改播放列表当前播放模式为单曲循环
            self.playList.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
            # 2)更改模式按钮的图片为单曲循环图片
            self.mode_btn.setIcon(QIcon("images/3.ico"))
            # 3)更改模式按钮提示信息
            self.mode_btn.setToolTip("单曲循环")
            # 否则单曲循环
        else:
            # 1)更改播放列表当前播放模式为顺序播放
            self.playList.setPlaybackMode(QMediaPlaylist.Loop)
            # 2)更改模式按钮的图片为顺序图片
            self.mode_btn.setIcon(QIcon("images/4.ico"))
            # 3)更改模式按钮提示信息
            self.mode_btn.setToolTip("顺序播放")

    # 自定义函数，获取播放音频的总时长,参数d保存的音频的总时长 （毫秒）
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

        # 获取当前播放列表
        index = self.playList.currentIndex()



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

    # 自定义函数，更改当前播放位置
    def timeChanged(self, t):
        # 设置播放器的当前位置为进度条的当前进度
        self.player.setPosition(t)

    # 自定义播放函数
    def musicPlay(self):
        # 判断播放器是否是播放状态
        if self.player.state() == QMediaPlayer.State.PlayingState:
            # 更改播放器为暂停状态
            self.player.pause()
            # 更改播放按钮的图片为暂停图片
            self.play_btn.setIcon(QIcon("images/1.ico"))
            # 更改播放按钮的提示信息为“播放”
            self.play_btn.setToolTip("播放")

        # 判断播放器是否是暂停状态
        elif self.player.state() == QMediaPlayer.State.PausedState:
            # 更改播放器为播放状态
            self.player.play()
            # 更改播放按钮的图片为播放图片
            self.play_btn.setIcon(QIcon("images/2.ico"))
            # 更改播放按钮的提示信息为“暂停”
            self.play_btn.setToolTip("暂停")
        # 否则（停止状态）
        else:
            # 获取本地音频文件
            fileNames,_ = QFileDialog.getOpenFileNames(None,"选择音乐",'E:/Projects/Python/ProjectUI/AI-barbara-4.1-Stable-fcpe/results',"FLAC无损音频文件(*.flac);;所有文件(*.*)")
            for i in fileNames:
                if i.endswith('.flac'):  # 判断文件类型是否为FLAC
                    # 生成相同前缀的WAV文件名
                    output_wav = os.path.splitext(i)[0] + ".wav"
                    audio = AudioSegment.from_file(i,"flac")
                    audio.export(output_wav,format="wav")
                    break
                    play(audio)  # 使用pydub库播放FLAC文件
                else:
                    # 把音频文件加载到播放列表对象中
                    self.playList.addMedia(QMediaContent(QUrl.fromLocalFile(i)))
                    # 获取音频文件路径最后一个“/"字符的位置
                    start = i.rfind('/')
                    end = i.rfind('.')
                    # 获取音频文件中文件名称，追加到列表对象中
                    self.musicNames.append(i[start + 1:end])
            # 设置当前播放列表的播放音频索引
            self.playList.setCurrentIndex(0)
            # 开始播放
            self.player.play()
            # 更改播放按钮的图片为暂停图片
            self.play_btn.setIcon(QIcon("images/2.ico"))
            # 更改播放按钮的提示信息为“暂停”
            self.play_btn.setToolTip("暂停")


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

    def play_sound_a(self):  # 播放audio_a.wav音频文件的方法
        global audio_a
        global audio_b # 声明全局变量
        self.audio_a = QSound(recordFileAddress)  # 创建一个名为audio_a的QSound对象，用于播放audio_a.wav音频文件
        self.audio_b = QSound(handledFileAddress)  # 创建一个名为audio_b的QSound对象，用于播放audio_b.wav音频文件
        if self.recordPlayButton_status == '播放':  # 如果recordPlayButton处于"播放"状态
            if self.handledPlayButton_status == '暂停':  # 如果handledPlayButton处于"暂停"状态
                self.audio_b.stop()  # 停止播放audio_b.wav音频文件
                self.handledPlayButton.setText('播放')  # 修改handledPlayButton的文本为"播放"
                self.handledPlayButton_status = '播放'  # 修改handledPlayButton的状态为"播放"


            self.audio_a.play()
            self.recordPlayButton.setText('暂停')  # 修改recordPlayButton的文本为"暂停"
            self.recordPlayButton_status = '暂停'  # 修改recordPlayButton的状态为"暂停"
        else:  # 如果recordPlayButton处于"暂停"状态
            self.audio_a.stop()  # 停止播放audio_a.wav音频文件
            self.recordPlayButton.setText('播放')  # 修改recordPlayButton的文本为"播放"
            self.recordPlayButton_status = '播放'  # 修改recordPlayButton的状态为"播放"

    def play_sound_b(self):  # 播放audio_b.wav音频文件的方法
        global record_state
        global handle_state
        if self.handledPlayButton_status == '播放':  # 如果handledPlayButton处于"播放"状态
            if self.recordPlayButton_status == '暂停':  # 如果recordPlayButton处于"暂停"状态
                self.audio_a.stop()  # 停止播放audio_a.wav音频文件
                self.recordPlayButton.setText('播放')  # 修改recordPlayButton的文本为"播放"
                self.recordPlayButton_status = '播放'  # 修改recordPlayButton的状态为"播放"

            self.audio_b.play()  # 播放audio_b.flac音频文件
            self.handledPlayButton.setText('暂停')  # 修改handledPlayButton的文本为"暂停"
            self.handledPlayButton_status = '暂停'  # 修改handledPlayButton的状态为"暂停"
        else:  # 如果handledPlayButton处于"暂停"状态
            self.audio_b.stop()  # 停止播放audio_b.wav音频文件
            self.handledPlayButton.setText('播放')  # 修改handledPlayButton的文本为"播放"
            self.handledPlayButton_status = '播放'  # 修改handledPlayButton的状态为"播放"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
