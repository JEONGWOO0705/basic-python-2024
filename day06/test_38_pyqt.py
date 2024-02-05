# DATE : 2024025
# FILE : test_38_pyqt.py
# DESC : Qt designer 로 만든 ui와 연동


import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtwin_exam(QWidget): 
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/TestApp.ui',self)  # QtDesigner에서 만든 ui를 로드
        

if __name__ == '__main__':
    loop = QApplication(sys.argv) 
    instance = qtwin_exam() 
    instance.show()
    loop.exec_()