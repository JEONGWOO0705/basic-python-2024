# DATE : 2024025
# FILE : test_38_pyqt.py
# DESC : Qt designer 로 만든 ui와 연동


import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtwin_exam(QWidget): # 상속
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/TestApp.ui',self)  # QtDesigner에서 만든 ui를 로드
        # 버튼에 대한 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked) # ui파일내에 있는 위젯 접근은 VSCODE상에서 색상으로 표현이 안됨
        self.btnStop.clicked.connect(self.btnStopClicked)

    def btnStartClicked(self):
        print('Click the Start Button')
        self.lblStatus.setText('Status : Start')
        QMessageBox.about(self,'run','system is started.')

    def btnStopClicked(self):
        print('Click the Stop Button')
        self.lblStatus.setText('Status : Stop')

    # QWidget(부모 클래스)에 있는 close Event를 그대로 쓰면 그냥 닫힘
    # 닫을지 말지를 한번더 물어보는 형태로 다시 구현하고 싶음(재정의 : Override)
    def closeEvent(self, QCloseEvent) -> None: # x버튼 종료 확인 코드 (재정의 : 오버라이딩)
        re = QMessageBox.question(self,'종료 확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No) # Shift \ == | (or)
        if re == QMessageBox.Yes: # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
        

if __name__ == '__main__':
    loop = QApplication(sys.argv) 
    instance = qtwin_exam() 
    instance.show()
    loop.exec_()