# 파이썬 기초 2024
부경대 2024 IoT 개발자 과정 기초 프로그래밍 언어 - 파이썬

## 1일차
- 개발 환경 구축
    - 코딩 폰트 - 나눔고딕코딩
    - Notepad++ 설치
    - Python 설치
    - Visual Studio Code 설치
    - Git 설치
        - TortoiseGit 설치
        - Github 가입
        - Github Desktop 설치
    
- 파이썬 기초
    - 콘솔 출력
    - 주석  
    - 변수
    - 자료형
    - 연산자

    ```python
    # 이부분은 주석입니다.
    var01 = 10 # 정수, 실수, 불, 문자열 모두 가능
    print(var01)
    print(type(var01))

    print(5 + 4 / 2) # 7.0
    print(5 == 4) # False
    ```

## 2일차
- 파이썬 기초
    - 흐름제어
        - if
            - if 문 문법 # 참과 거짓으로 조건을 나눔 (다른 언어 switch)
            - int(input()) # 입력 방법
            - import datetime 을 사용한 현재 시간 을 처리하는 if문
        - for : 반복문 기본 (다른 언어 foreach)
        - while : 반복문 변형 (다른언어 do~while)
    - 복합 자료형 + 연산자
        - list
        - tuple
        - dictionary
        - range()
    - 출력 포맷, 입력 방법
    - 구구단 + 디버깅
    ```python
    # debugging
    # F5(디버그 시작), F10(한줄씩 실행), F11(함수 안으로 진입), F9(중단점 토글)
    print('구구단 시작!!')
    for x in range(2,9+1): # 2부터 9까지 반복
        print(f'{x}단 -------------------------------------------------------------------------------------------------------------------')
        for y in range(1,9+1): # 1부터 9까지 반복
            print(f'{x} x {y} = {x*y :2d}', end ='   ') # end = 는 엔터대신 공백으로 대체
        print() # 안쪽 for문이 끝나면 마지막 enter를 추가

    ```

## 3일차
- 파이썬 기초
    - 입력 방법
        - input(), map() 함수의 활용
    - 별찍기
    - 함수, (람다함수는 나중에..)
    - 객체지향 OOP
        - 객체는 명사와 동사의 집합
        - 명사는 변수, 동사는 함수
        - 변수와 함수를 모두 모아둔 곳 : 클래스 (class) ==> class 는 객체가 아니다. class에서 나온 것이 객체이다!!
        - class에서 하나씩 생성 : 객체 (object)
        - 캡슐화(__plateNumber)
    - 패키지, 모듈

## 4일차
- 파이썬 기초
    - 패키지, 모듈 계속
        - pip 사용

        ```shell
        > pip --version # 버전 확인
        > pip list # 현재 설치된 라이브러리 목록 확인
        > pip install 패키지명 # 패키지를 내 컴퓨터에 설치
        > pip uninstall 패키지명 # 패키지를 삭제
        ```
    - 예외 처리 : 비정상적인 프로그램 종료 방지

    ```python
    def divide(x, y):
        try:
            return x / y  # ZeroDivision Error 발생
        except ZeroDivisionError as e:
            print('제수는 0이 될 수 없습니다.')
            return '∞' 
    ```
    - 텍스트 파일 입출력

    ```python
    f = open('파일명', mode = 'r or w or a', encoding = 'cp949 or utf-8')
    f.read()    
    f.readline()    # 읽기  
    f.write('text') # 쓰기
    f.close()       # 파일은 반드시 닫는다
    ```
    
- 파이썬 응용
    - 주피터 노트북
        - Ctrl + Shift + P (보기 => 명령 팔레트) 로 시작
        - 사용방법 (text31_jupyternb.ipybn 참조)
    - folium 기본 사용
    ![folium 사용법](https://raw.githubusercontent.com/JEONGWOO0705/basic-python-2024/main/images/python_001.png)



## 5일차
- 파이썬 응용
    - 주피터 노트북 활용 - 구글 코랩(Colab)
    - folium 계속
    - json (Java Script Object Notation) 사용법, 입출력
    - 응용 예제 연습 (10개)
        - IP 주소 확인 예제
        - QR Code (Naver)

    ![QR Code](https://raw.githubusercontent.com/JEONGWOO0705/basic-python-2024/main/day05/qrcode_01.png)


## 6일차
- Python 라이브러리 경로 : C:\DEV\Langs\Python311\Lib\site-packages

- 파이썬 응용
    - Window App(PyQt) 만들기

    ```shell
    > pip install PyQt5
    > pip install PyQt5Designer
    ```
    - PyQt5 기본 실행
    - QtDesigner 사용법
    - ☆☆☆ Thread 학습 : UI 쓰레드와 Background 쓰레드 분리
        - UI Thread 하나로 모든 일을 못함
        - 다른 Thread를 만들어 일을 병렬로 수행하게함 !!
        - [ ] GIL, 병렬 프로세싱 더 학습할 것

    ![쓰레드 예제](https://raw.githubusercontent.com/JEONGWOO0705/basic-python-2024/main/images/python_002.gif)

    ```python
        # 쓰레드 클래스에서 시그널 선언
        class BackWorker(QThread): # PyQt에서 스레드 클래스 상속
            initSignal = pyqtSignal(int) # 시그널을 UI스레드로 전달하기위한 변수객체
            setSignal = pyqtSignal(int)
            # ...

            def run(self) -> None: # 스레드 실행
                # 스레드로 동작할 내용
                maxVal = 1000001
                self.initSignal.emit(maxVal) # UI쓰레드로 보내기...
                # ...

        class qtwin_exam(QWidget):  # UI 스레드
            # ...
            def btnStartClicked(self):
                th = BackWorker(self)
                th.start() # BackWorker 내의 self.run() 실행
                th.initSignal.connect(self.initPgbTask) # 스레드에서 초기화 시그널이 오면 initPgbTask 슬롯함수가 대신 처리
                # ...    

            # 스레드에서 시그널이 넘어오면 UI처리를 대신 해주는 부분 -> 슬롯 함수
            @pyqtSlot(int) # BackWorker 스레드에서 self.initSignal.emit() 동작해서 실행
            def initPgbTask(self, maxVal):
                self.pgbTask.setValue(0)
                self.pgbTask.setRange(0,maxVal-1)
        ```


## 7일차
- 파이썬 응용
    - 객체지향 정리
        - 상속
        - 오버라이딩(재정의) 
        - 오버로드(같은 이름의 함수를 매개변수 다르게 사용 -> 같은 이름의 함수를 다른 역할로써 활용)
    - 가상환경 Virtualenv
        - 다른 버전의 파이썬도 설치해야 사용 가능

    ![가상 환경](https://raw.githubusercontent.com/JEONGWOO0705/basic-python-2024/main/images/python_003.png)


    - PyQt5와 응용예제 연습
        - 이미지 뷰어
        - 이미지 에디터(그림판)

    ![PyQt 예제](https://raw.githubusercontent.com/JEONGWOO0705/basic-python-2024/main/images/python_006.png)


## 8일차
- 파이썬 기본 코딩 테스트!!
    - 주피터 노트북 활용

## 추가
- 파이썬 실행 파일 만들기
    - PyQt ui 파일이나 이미지 파일의 경로가 절대 경로가 지정
    - pip install pyinstaller 패키지 설치
    - pyinstaller -w -F 파이썬.py   (-w :콘솔창 없애기, -F: 실행파일 하나로 만들기)



      