# DATE : 20240206
# FILE : test_41_exam.py
# DESC : 가상환경 테스트


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent, QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class qtwin_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        btn01 = QPushButton('Click', self)
        btn01.setGeometry(50, 100, 100, 40)
        btn01.clicked.connect(self.btn01_clicked) # 버튼을 클릭하면(Signal) btn01_clicked 함수를 실행

        self.setGeometry(300, 200, 400, 200)
        self.setWindowTitle('Button Event')
        # self.show()

    def btn01_clicked(self):
        QMessageBox.about(self,'Clicked', '버튼을 클릭했습니다!')

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self,'종료 확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No) # Shift \ == | (or)
        if re == QMessageBox.Yes: # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__ == '__main__': # Main entry 확인 조건 추가
    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show()
    loop.exec_()
