# DATE : 20240206
# FILE : test_42_pypaint.py
# DESC : 그림판 만들기

import sys
from PyQt5 import uic # QtDesigner 호출시 필요
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *

class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self): # 화면 초기화
        # uic.loadUi('./day07/pyPaint.ui',self)
        uic.loadUi('C:/Sources/basic-python-2024/day07/pyPaint.ui',self)   # 실행 파일 생성시는 경로에 상대 경로가 없어져야함
        # self.setWindowIcon(QIcon('./images/iot.png'))
        self.setWindowIcon(QIcon('C:/Sources/basic-python-2024/day07/iot.png')) # 실행 파일 생성시는 경로에 상대 경로가 없어져야함
        self.setWindowTitle('Py그림판') 
        # 캔버스 초기화
        self.brushColor = Qt.black
        self.canvas = QPixmap(self.lb_canvas.width(),self.lb_canvas.height())   
        self.canvas.fill(QColor('white'))
        self.lb_canvas.setPixmap(self.canvas)

        self.btn_black.setStyleSheet('background : black')
        self.btn_red.setStyleSheet('background : red')
        self.btn_blue.setStyleSheet('background : blue')


        self.setCenter()
        self.show()

    def initSignal(self): # 동작 초기화
        self.btn_black.clicked.connect(self.buttonClicked)
        self.btn_red.clicked.connect(self.buttonClicked)
        self.btn_blue.clicked.connect(self.buttonClicked)
        self.btn_clear.clicked.connect(self.buttonClicked)
        #2024-02-06 이미지 로드 및 저장 버튼 추가
        self.btn_load.clicked.connect(self.btnLoadClicked)
        self.btn_save.clicked.connect(self.btnSaveClicked)

    def btnSaveClicked(self):
        filePath, _ = QFileDialog.getSaveFileName(self,'이미지 저장','','Image file(*.jpg; *.png)' )
        if filePath =='': return
        pixmap = self.lb_canvas.pixmap()
        pixmap.save(filePath)

    def btnLoadClicked(self):
        image = QFileDialog.getOpenFileName(None,'이미지 로드','','Image file(*.jpg; *.png)')
        imagePath = image[0]
        pixmap = QPixmap(imagePath).scaledToHeight(381) # 파일 겨올에 있는 이미지를 읽어서 pixmap 객체에 담기
        self.lb_canvas.setPixmap(pixmap)
        self.lb_canvas.adjustSize() # 이미지를 라벨 크기에 맞추기

    def buttonClicked(self):
        btn_val = self.sender().objectName() # self.sender() == btn_blue
        print(btn_val)
        if btn_val == 'btn_black':
            self.brushColor = Qt.black
        elif btn_val == 'btn_red':
            self.brushColor = Qt.red
        elif btn_val == 'btn_blue':
            self.brushColor = Qt.blue
        elif btn_val == 'btn_clear':
            self.canvas.fill(QColor('white'))
            self.lb_canvas.setPixmap(self.canvas)   
   

    def mouseMoveEvent(self, e) -> None:
        print(e.x(), e.y())
        brush = QPainter(self.lb_canvas.pixmap())
        brush.setPen(QPen(self.brushColor, 5, Qt.SolidLine, Qt.RoundCap))
        brush.drawPoint(e.x(), e.y())
        brush.end()
        self.update() # 화면 업데이트

         

    def setCenter(self): ## 윈앱을 화면 정중앙에 위치
            gm = self.frameGeometry() # 윈앱 자신의 위치값
            cp = QDesktopWidget().availableGeometry().center()  # 현재 모니터의 정중앙 값을 가져옴
            gm.moveCenter(cp)
            self.move(gm.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())