# 4번 문제
from urllib.request import Request, urlopen
import webbrowser 
def get_url():
    req = Request(f'https://www.{url_name}.com/')
    res = urlopen(req)
    print(f'https://www.{url_name}.com/')
    webbrowser.open(f'https://www.{url_name}.com/') # 입력받는 웹브라우저를 바로 실행 시켜줌
    return res
    

url_name = input('url 이름을 영문으로 입력하세요 : ')
get_url()