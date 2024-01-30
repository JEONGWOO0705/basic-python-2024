# file : test_15_output.py
# desc : 콘솔 출력 포맷 양식 String Format

string_1 = '{}'.format('457945') # {} 위치에 함수(format) 뒤에 들어있는 값을 치환, 원하는 양식으로 표현
print(type(string_1))

name = 'Jeongwoo Hwang' ##input('이름 입력 > ')
string_2 = '안녕하세요, {} 입니다.'.format(name)
print(string_2)

string_3 = '{} {} {}'.format(4000, '만', '빌려주세요')
print(string_3)

# 정수를 문자열 포맷 d
# =: 기호와 숫자를 분리, 05: 다섯자리를 만들때 빈자리를 0으로 채우기, d:정수, 02d: 두자리수 만들때 빈자리 0으로 채우기

string_4 = '____{:5d}____'.format(100) # {:5d}는 100이 들어가기전에 index 5 만큼 앞에 차지한다는 말!!
print(string_4)

string_4 = '____{:05d}____'.format(100) # {:05d}는 100이 들어가기전에 index 5 만큼 앞에 차지한다는 말, 빈칸에는 0이 들어감!!
print(string_4)

# 실수 문자열 포맷 f (기본 소수점 6자리까지 표현)
# 7.2f 전체 자리수를 7자리로, 소수점 뒤는 2자리 fix
val = 78.333333333333333333
string_5 = '_____{:.2f}_____'.format(val) # {:.2f} => 소수점 둘째자리까지 표현해라, {:7.2f} 앞에 7자리 만들고 소수점 둘째자리까지 만들어라 
print(string_5)

# 파이썬 3.6 이후 도입. .format() 함수를 아예 사용안함
# 이게 제일 좋앙
string_6 = f'_____{val:7.2f}_____'
print(string_6)

string_7 = 'Hello, World'
print(string_7.upper()) ## upper() 모든 글자를 대문자로 변환!!
print(string_7.lower()) ## lower() 모든 글자를 소문자로 변환!!
print(string_7.lower().capitalize()) ## .capitalize() 첫글자를 대문자로 변환

print(string_7.split(' ')) ## 특정한 단어로 자르는 함수 => 리스트로 나옴

string_8 = 'Hello, I am JW Hwang. I am a programmer. Good Luck for your day.'
words = string_8.split(' ')
print(words)
print(f'string_8 문장의 단어 갯수는 {len(words)}입니다.')

string_9 = 'A10'
print(string_9.isalnum()) # True
print(string_9.isnumeric()) # False, A는 알파벳이기 때문에

string_10 = '10.5' # 소수점은 함수로 만들어서 처리해야...
print(string_10.isdecimal()) # False

print('안냥' in '안녕하세요') # 문장안에 단어가 있는지 확인 