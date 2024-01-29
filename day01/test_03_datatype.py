# date : 20240129
# desc : 자료형

## 기본 자료형 - 숫자형, 문자형, 불형, None형
## 복합 자료형 - 리스트형, 튜플형, 딕셔너리, 집합

## None 형 == Null(null) / (c, c++, Java, SQL)
## 값은 값인데 아무것도 지정할 수 없는 값 ( 비어있는 값이 아님 ) => None ( 아무것도 알 수 없는 상태 ) ex. 숫자가 들었는지 글자가 들었는지 알 수 없음
## 이용할 수 없는, 할당되지 않는, 적용 불가하다는 의미

apple = None

print(apple)

## 숫자형 - 정수형, 실수형, 진수형

### 정수
ten = 10
hundred = 100
temp = -8

### 실수
pi = 3.141592
tax_rate = 10.0
emp_earn_rate = 3.3
test_val = 2e10
print(test_val)

### 진수
bit142 = 0b10001110
oct9 = 0o11
hex255 = 0xff
print(bit142)
print(oct9)
print(hex255)

## 문자형 - 파이썬에는 문자, 문자열 차이가 없음
greeting = 'Hello!'
greeting = "Hello!" # 홑따옴표, 쌍따옴표 모두 문자열을 나타냄
print(greeting)

multi_str = '''Hello
I am a programmer.
Have a good afternoon'''
print(multi_str)
multi_str2 = 'Line1 \n' \
             'Line2 \n' \
             'Line3'
print(multi_str2)

## 불형 ( Bool, Boolean)

isCheck = False
print(isCheck)

isCheck = True
print(isCheck)

answer = (3 == 6)
print(answer)

answer = (3.0 == 3)
print(answer)

## 자료형이 어떤 타입인지 체크
print(type(apple))
print(type(hundred))
print(type(test_val))
print(type(hex255))
print(type(greeting))
print(type(isCheck))