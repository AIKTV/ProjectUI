from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
import os

app = QApplication([])
dir_path = "D:\目标文件夹"  # 指定目录路径
if os.path.isdir(dir_path):  # 判断目录是否存在
    url = QUrl.fromLocalFile(dir_path)
    QDesktopServices.openUrl(url)  # 打开目录
else:
    print("目录不存在")
