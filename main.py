import sys
import typing
from PyQt5 import QtCore
from getpass import getpass
# from viewinternshipdetailsfinal import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        # self.setFixedWidth(1920)
        # self.setFixedHeight(1080)
        self.ui.setupUi(self)
        self.w = 2000
        self.h = 1000
        self.resize(self.w,self.h)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    # window.setGeometry(100,100,100,100)
    # window.setFixedWidth(1920)
    # window.setFixedHeight(1080)
    window.showMaximized()
    window.show()
    sys.exit(app.exec_())



