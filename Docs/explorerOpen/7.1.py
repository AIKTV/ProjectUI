import warnings
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import QProcess
from AIKTVUI import Ui_MainWindow
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
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
            lambda: self.openfiledialog('handled', 'FLAC无损音频文件(*.flac)'))
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
        self.recording = True
        self.counter += 1
        current_time = time.strftime("%m%d-%H%M")
        # 修改文件存放路径为新的位置
        self.record_file_path = f"D:/GitHub/ProjectUI/Docs/recording audio/recordings/record-{current_time}-{self.counter}.wav"
        threading.Thread(target=self._record).start()

    def stop_recording(self):
        self.recording = False
        self.display_recent_recording_box()

    def display_recent_recording_box(self):
        recent_file = self.record_file_path
        self.recordOutputDisplay.setText(recent_file)
        self.recordOutputDisplay.show()
        QTimer.singleShot(5000, self.recordOutputDisplay.hide)

    def _update_time(self):
        seconds = 0
        while self.recording:
            self.recordTimeDisplay.setText(time.strftime('%M:%S', time.gmtime(seconds)))
            time.sleep(1)
            seconds += 1

    def _record(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 10

        audio = pyaudio.PyAudio()

        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)

        frames = []

        t = threading.Thread(target=self._update_time)
        t.start()

        while self.recording:
            data = stream.read(CHUNK)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        audio.terminate()

        t.join()

        wf = wave.open(self.record_file_path, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
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
            fileNames, typeName = QFileDialog.getOpenFileNames(None, "选择音乐", 'D:/ai', "*")
            # 循环音频文件的列表
            for i in fileNames:
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

        self.model_name_label = QLabel("请输入使用的模型步数（例：模型为G_800.pth就输入800）")
        self.model_name_edit = QLineEdit()
        layout.addWidget(self.model_name_label)
        layout.addWidget(self.model_name_edit)

        self.key_num_label = QLabel("请输入音高（例：维持原调为0，支持正负，数字为半音）")
        self.key_num_edit = QLineEdit()
        layout.addWidget(self.key_num_label)
        layout.addWidget(self.key_num_edit)

        self.f0_predictor_label = QLabel("请选择使用的F0预测器，0为crepe，1为pm，2为dio，3为harvest")
        self.f0_predictor_edit = QLineEdit()
        layout.addWidget(self.f0_predictor_label)
        layout.addWidget(self.f0_predictor_edit)

        self.if_diffusion_label = QLabel("是否使用浅层扩散模型？使用后可解决一部分电音问题（推荐）\n请注意该模型需先单独训练好（y/n）")
        self.if_diffusion_edit = QLineEdit()
        layout.addWidget(self.if_diffusion_label)
        layout.addWidget(self.if_diffusion_edit)

        self.diffusion_name_label = QLabel("请输入使用的扩散模型步数（例：模型为model_2000.pt就输入2000）")
        self.diffusion_name_edit = QLineEdit()
        layout.addWidget(self.diffusion_name_label)
        layout.addWidget(self.diffusion_name_edit)

        self.diffusion_k_step_label = QLabel("请输入扩散步数，越大越接近扩散模型的结果，默认100（例：100）")
        self.diffusion_k_step_edit = QLineEdit()
        layout.addWidget(self.diffusion_k_step_label)
        layout.addWidget(self.diffusion_k_step_edit)

        self.if_cluster_label = QLabel("是否使用聚类模型？聚类模型可以减小音色泄漏，但会降低模型的咬字\n请注意该模型需先单独训练好（y/n）")
        self.if_cluster_edit = QLineEdit()
        layout.addWidget(self.if_cluster_label)
        layout.addWidget(self.if_cluster_edit)

        self.cluster_ratio_label = QLabel("请输入聚类方案占比，范围 0-1（例：0为不使用）")
        self.cluster_ratio_edit = QLineEdit()
        layout.addWidget(self.cluster_ratio_label)
        layout.addWidget(self.cluster_ratio_edit)

        self.if_auto_predict_f0_label = QLabel("是否使用自动音高预测？推荐语音转换开启，歌声转换开启会严重跑调（y/n）")
        self.if_auto_predict_f0_edit = QLineEdit()
        layout.addWidget(self.if_auto_predict_f0_label)
        layout.addWidget(self.if_auto_predict_f0_edit)

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
        model_name = self.model_name_edit.text()
        if recordFileAddress:                                         # 将地址传递给 self.wav_name_edit
            wav_name = recordFileAddress.split('/')[-1].split('.')[0]
        key_num = self.key_num_edit.text()
        f0_predictor = self.f0_predictor_edit.text()
        if f0_predictor == '0':
            f0_predictor = 'crepe'
        if f0_predictor == '1':
            f0_predictor = 'pm'
        if f0_predictor == '2':
            f0_predictor = 'dio'
        if f0_predictor == '3':
            f0_predictor = 'harvest'
        if_diffusion = self.if_diffusion_edit.text()
        diffusion_name = self.diffusion_name_edit.text()
        diffusion_k_step = self.diffusion_k_step_edit.text()

        if_cluster = self.if_cluster_edit.text()
        cluster_ratio = self.cluster_ratio_edit.text()

        if_auto_predict_f0 = self.if_auto_predict_f0_edit.text()

        if_clip = self.if_clip_edit.text()
        if_linear_gradient = self.if_linear_gradient_edit.text()

        inference_case = r'.\env\python.exe inference_main.py'
        inference_case = inference_case + f' -m "logs/44k/G_{model_name}.pth" -c "configs/config.json" -n "{wav_name}" -t {key_num} -s "barbara" -f0p {f0_predictor}'

        if if_diffusion == 'y':
            inference_case = inference_case + f' -shd -dm "logs/44k/diffusion/model_{diffusion_name}.pt" -ks {diffusion_k_step}'
        if if_cluster == 'y':
            inference_case = inference_case + f' -cm "logs/44k/kmeans_10000.pt" -cr {cluster_ratio}'
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

            self.audio_a.play()  # 播放audio_a.wav音频文件
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

            self.audio_b.play()  # 播放audio_b.wav音频文件
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