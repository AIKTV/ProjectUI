import sys
import wave
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("音频处理")
        self.setGeometry(100, 100, 300, 200)

        self.btn_select_file = QPushButton("选择文件", self)
        self.btn_select_file.setGeometry(50, 50, 200, 30)
        self.btn_select_file.clicked.connect(self.select_file)

        self.lbl_duration = QLabel("文件持续时间: 0秒", self)
        self.lbl_duration.setGeometry(50, 100, 200, 30)

    def select_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "选择文件")
        if file_path:
            duration = self.get_audio_duration(file_path)
            self.lbl_duration.setText(f"文件持续时间: {duration}秒")

    def get_audio_duration(self, file_path):
        try:
            with wave.open(file_path, 'r') as audio_file:
                frames = audio_file.getnframes()
                rate = audio_file.getframerate()
                duration = frames / float(rate)
                return round(duration, 2)
        except Exception as e:
            print(f"获取音频持续时间失败: {e}")
            return 0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
