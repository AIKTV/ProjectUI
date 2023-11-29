import warnings
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from AIKTVUI import Ui_MainWindow
import sys
import os

warnings.filterwarnings("ignore", category=DeprecationWarning)

class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())