# date : 20240131
# file : test_20_function.py
# desc : 함수 만들기 (계산기 기능)

def add(x, y) -> int:
    result = x + y
    return result

def minus(x, y) -> int:
    result = x - y
    return result

def multi(x, y) -> int:
    result = x * y
    return result

def divide(x, y) -> float:
    result = x / y
    return result

def say_hello() -> None:
    print('hello')
    # return None 은 생략

say_hello()

print('더하기 ->')
a,b = map(int,input('두 수를 입력하세요 > ').split(' '))
결과 = add(a,b)
print(f'{a} + {b} = {결과}')  # return은 함수 결과값이 바뀐다!
print(f'{a} - {b} = {minus(a, b)}')  
print(f'{a} x {b} = {multi(a, b)}')  
print(f'{a} ÷ {b} = {divide(a, b)}')  
