# date : 20240130
# desc : 복합 자료형 list

# s1 = 80
# s2 = 90
# s3 = 100
# s4 = 50
# s5 = 60  학생수만큼 변수를 생성해야함. but 리스트를 사용하여 하나의 변수로 관리 가능
# 총 갯수 10(N) 이면 인덱스의 마지막 값은 (N-1) == 9이다. 
# index = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
std = [80, 90, 100, 50, 60]

print(std[0])

list_1 = [265, 3.5, '문자열', True, [1,2,3,4], (4,5), std] # 리스트 안에는 모든게 다 들어갈 수 있음!!!
print(list_1[2])

list_1[6] = '바꾼 값'
print(list_1[6])

## 리스트 연산  
print(list_1[2:4])  ## list [x : y] => x 값에는 자기가 출력하고 싶은 인덱스 값, y값에는 자기가 출력하고 싶은 인덱스 +1 값

print(list_1[-1])  ## list[-1] => 뒤에서 첫번째 값
print(list_1[-2])  ## list[-2] => 뒤에서 두번째 값

## 이중 리스트
print(list_1[4][2]) # [1,2,3,4] 중 3만 가져오기

list_2 = [[1,2,3],[4,5,6],[7,8,9]]
print(list_2[1][2]) # 6

list_4 = [1,2,3]
list_5 = [7,8,9]
# list_3 = list_4 + list_5
## 리스트 연산 +,* 만 가능!!
print(list_4 + list_5) # +는 리스트를 연결!
print(list_5 * 2) # *는 리스트를 반복!

## 리스트 길이
print(len(std))
## append() 리스트 마지막에 하나 추가
## insert(index, val) 리스트의 index 이후에 val추가

list_1.append('hello')
list_1.insert(2,'hihihihi') # 2번째 인덱스에 값을 추가 (원래값은 뒤로 밀림)
print(list_1)

## extend() 기존 리스트 확장 => + 와 유사 하나 다름
list_4.extend(list_5)
print(list_4)

## 리스트 삭제
del list_4[3]
print(list_4)

## pop() 마지막 값을 꺼내오기
val = list_5.pop()
print(val)
print(list_5)

print(std)
val = std.pop(2)
print(val)
print(std)

## clear() => 빈 리스트로 만들어 버리기
list_5.clear()
print(list_5)

## sort()
print(list_1)
# list_1.sort() ## 문자열, 숫자, 불이 섞여있는 리스트는 정렬안됨
std.sort()
print(std)
std.sort(reverse = True)
print(std)

# in, not in
print(99 in std) # True
print(98 in std) # False

# reverse(), copy(), count() .... 
# *리스트 : 전개 연산자
list_a = [1,3,5]
list_b = [2,4,8]
list_c = [*list_a, *list_b]
print(list_c)

list_d = [list_a, list_b]
print(list_d)