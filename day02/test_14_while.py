# file : test_14_while.py
# desc : while 문

## while 참 인 조건 : 
## 공통점  if 조건: elif 조건:, for in range():, while 조건:
count = 0
while count < 10: # count 변수 값이 10보다 작거나 같은 동안 반복
    count = count + 1
    print('나무찍기 ', count, '번째')

count = 0
while True: # 참인 동안 True => 항상 참, 무한 루프
    count = count + 1
    print('나무 찍기', count)
    if count == 10:
        break # 이 반복문을 빠져나가라


number = 0
while True:
    number = number + 1
    if str(number).count('3') >= 1 or \
       str(number).count('6') >= 1 or \
       str(number).count('9') >= 1: # 숫자를 문자열로 바꾼 값에 '3', '6', '9'
       print('짝')  # continue는 반복에서 제외
    else:
        print(number)

    if number > 31:
        break      # break는 반복문을 완전히 빠져나가는것