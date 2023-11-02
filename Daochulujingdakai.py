import sys
from PyQt5.QtWidgets import QApplication, QFileDialog

app = QApplication(sys.argv)

# 打开文件对话框
file_dialog = QFileDialog()
file_path, _ = file_dialog.getOpenFileName(None, "选择文件")

if file_path:
    file_info = QFileInfo(file_path)
    file_name = file_info.fileName()  # 获取文件名
    path = file_info.path()  # 获取文件路径

    print("文件路径:", path)
    print("文件名:", file_name)

sys.exit(app.exec_())
