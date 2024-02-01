# date : 20240201
# file : test_25_web.py
# desc : urllib 모듈 사용법

# from urllib.request import *              # *은 request 안에 모든 함수를 쓰겠다.
from urllib.request import Request, urlopen # request안에 Request 클래스와, urlopen클래스만 쓰겠다.

req = Request('https://www.naver.com/') # 네이버 웹주소 (url)
res = urlopen(req) # url 주소로 웹사이트 열어 달라고 요청

print(f'응답 코드 : {res.status}') # url로 요청된 웹사이트 응답 확인
# print(res.read())


# urllib.request 보다 성능이 조금더 나은 모듈
import requests

res2 = requests.get('https://www.naver.com/')

print(res2.status_code)
print(res2.text)