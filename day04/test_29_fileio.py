# date : 20240201
# file : test_29_fileio.py
# desc : 텍스트 파일 읽기

f = open('sample.txt',mode='r', encoding='utf-8')
# 아래의 방법은 기본적이나, 용량 문제로 큰 파일은 읽기가 불가하다. 
# text = f.read() # 텍스트 파일 모든 텍스를 전부 한번에 읽어온다. 
# print(text)

# 아래는 가장 일반적...
while True:
    line = f.readline()
    if not line: break   # 조건문, 반복문 내의 코드가 한 줄만 있으면, if 문 옆에 바로 적기 가능
    print(line.replace('\n',''))  # replace는 대체를 해주는 함수


f.close()