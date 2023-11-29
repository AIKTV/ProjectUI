import warnings
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from AIKTVUI import Ui_MainWindow
import sys
import os

class MainForm(QMainWindow, Ui_MainWindow):
    class MainForm(QMainWindow, Ui_MainWindow):




        if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())