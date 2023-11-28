#将导出文件放入指定目录然后调用Windows下的资源管理器打开指定目录并播放导出文件
import shutil
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

if __name__ == '__main__':
    app = QApplication([])

    # 指定目录和导出文件路径
    directory_path = r'D:\目标文件夹'
    export_file_path = r'C:\path\to\export_file.mp3'

    # 移动导出文件到指定目录
    shutil.move(export_file_path, directory_path)

    # 打开目录
    QDesktopServices.openUrl(QUrl.fromLocalFile(directory_path))

    app.exec()

#在这段代码中，我们首先使用shutil.move函数将导出文件移动到指定目录。
# 然后，使用QDesktopServices.openUrl方法打开资源管理器并显示指定目录。
