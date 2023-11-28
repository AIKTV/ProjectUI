#!/user/bin/env python
# -*- coding:utf-8 -*-
# Code created by gongfuture
# Create Time: 2023/11/28 028 
# Create User: gongf
# This file is a part of ProjectUI
#
from PyQt5 import QtWidgets
import os

def __init__(self):
    super(MainForm, self).__init__()
    self.setupUi(self)
    self.actionfileopen.triggered.connect(self.open_file)


def open_file(self):
    fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(
        self, "选取文件", os.getcwd(), 'All Files(*);;Text Files(*.txt)')
    print(fileName)
    print(fileType)