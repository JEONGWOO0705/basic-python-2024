# date : 20240130
# desc : 흐름 제어 if 문

## 조건이 참일떄와 거짓일때로 나누어서 어떤일 처리 if


number = int(input('정수 입력 > ')) ## 입력함수 input(), 입력 함수로 받으면 문자열로 취급됨 -> int로 문자열을 정수형으로 변환시켜주기!! int(input())

if number > 0:
    print('양수 입니다.')   ## if  조건 : 
                                 # 행할 문장 ( 참인 조건 )
elif number == 0: # 양수도 아니고 음수도 아니라면
    print('0 입니다.')
elif number < 0:
    print('음수 입니다.')   ## else : 
                                # 행할 문장 ( 거짓인 조건 )
else:
    print('정의할 수 없습니다.')
