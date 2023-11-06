#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/11/4 
# Create User: gongf
# This file is a part of ProjectUI
#

import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from AIKTVUI import Ui_MainWindow
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


class FileOperate(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(FileOperate, self).__init__()
        # testform记得改
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_file)
        # pushButton是你使用的控件id，clicked()为button特有，其他的可能是triggered()或者toggle()
        # open_file是下面定义的方法名

    def open_file(self):
        # open_file随便，上面要用
        file_name_open, file_type_open = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File", os.getcwd(), '随便啥文件(*)')
        # fileName和fileType是自定义变量名，用于储存文件地址和文件类型（后缀）
        print(file_name_open)
        print(file_type_open)
        # 上两行是测试用的，正式用不用写
