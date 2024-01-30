# date : 20240130
# desc : 여러 조건 if 문

date = input('날짜를 입력하세요(예시 : 12-31) > ') # 12-31 문자열

month = date.split('-')[0] # 12
day = date.split('-')[1] # 31

if month == '12' and day == '25': # 12월 25일 
    print('메리 크리스마스!!')
elif month == '1' and day == '1': # 1월 1일
    print('Happy New Year!')
elif month == '4' and day == '14': #
    print('짜장면이나 드셈')
else:
    print('보통날 입니다.') 
