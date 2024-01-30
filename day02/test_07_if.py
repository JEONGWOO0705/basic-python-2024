# date : 20240130
# desc : if 문 응용
import datetime

now = datetime.datetime.now() # 현재의 년 월 일 시 분 초 를 가져옴

if now.hour < 12:
    print('오전 입니다')

else:
    print('오후 입니다.')