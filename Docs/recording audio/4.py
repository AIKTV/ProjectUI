import sys
import os
import time
import threading
import wave
import pyaudio
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)
from PyQt5.QtCore import QTimer

class Recorder(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('录音机')
        self.setGeometry(100, 100, 300, 150)

        self.record_button = QPushButton('开始录音')
        self.record_button.clicked.connect(self.start_recording)
        self.stop_button = QPushButton('停止录音')
        self.stop_button.clicked.connect(self.stop_recording)
        self.recordTimeDisplay = QLabel('00:00')

        self.recent_recording_label = QLabel('最近录音文件：')
        self.recordOutputDisplay = QLabel()

        h_box = QHBoxLayout()
        h_box.addWidget(self.record_button)
        h_box.addWidget(self.stop_button)

        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addWidget(self.recordTimeDisplay)
        v_box.addWidget(self.recent_recording_label)
        v_box.addWidget(self.recordOutputDisplay)

        main_widget = QWidget()
        main_widget.setLayout(v_box)
        self.setCentralWidget(main_widget)

        self.recording = False
        self.record_file_path = ''
        self.counter = 0

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    recorder = Recorder()
    recorder.show()
    sys.exit(app.exec_())

