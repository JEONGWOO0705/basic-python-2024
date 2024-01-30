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
            - if 문 문법 # 참과 거짓으로 조건을 나눔
            - int(input()) # 입력 방법
            - import datetime 을 사용한 현재 시간 을 처리하는 if문
        - for : 반복문 기본
        - while
    - 복합 자료형 + 연산자
        - list 연산 => list[x:y] 
            - x 값에는 자기가 출력하고 싶은 인덱스 값, y값에는 자기가 출력하고 싶은 인덱스 +1 값
        - 이중 리스트
        - 리스트 연산 +,*
        - 리스트 길이 함수 len()
        - append() => 리스트 마지막에 추가시켜주는 함수  ## list_1.append('hello')
        - insert(index, val) 리스트의 index 이후에 val추가 ## list_1.index(2,'hello')
        - extend() 기존 리스트 확장 ## list_4.extend(list_5)
        - del 리스트 삭제 ## del list_4[3]  ## del list_4
        - pop() 리스트 마지막 값 꺼내오기
        - clear() 리스트를 빈 값으로 만들기
        - sort() 오름차순 정렬 ## sort(reverse = True) => 내림차순 정렬
        - in ## print(99 in std) ## 99가 std 안에 있는지 확인하는 함수

    - 함수
    - 구구단, 별 찍기