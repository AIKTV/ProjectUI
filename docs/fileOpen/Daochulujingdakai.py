from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton('打开文件', self)
        self.button.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, '选择文件', '', 'All Files (*);;Text Files (*.txt)',
                                                   options=options)

        if file_name:
            print("文件路径:", file_name)
            print("文件名:", file_name.split('/')[-1])


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
