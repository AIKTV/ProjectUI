#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/10/30 
# Create User: gongf
# This file is a part of ProjectUI
#
import os
import sys
import warnings

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from AIKTVUI import Ui_MainWindow

warnings.filterwarnings("ignore", category=DeprecationWarning)

class testform(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(testform, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_file)

    def open_file(self):
        fileName,fileType=QtWidgets.QFileDialog.getOpenFileName(
            self,"Open File",os.getcwd(),'随便啥文件(*)')
        print(fileName)
        print(fileType)

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = testform()
    win.show()
    sys.exit(app.exec_())
