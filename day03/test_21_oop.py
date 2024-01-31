# date : 20240131
# file : test_21_oop.py
# desc : 객체 지향 클래스 만들기

# 클래스(사람이라는 객체를 만들기 위한 청사진) 만들기
class Person: # 사람 클래스 선언
    name = '' # 클래스 안에 들어가 있는 변수를 멤버 변수라고 한다. # 함수 안에는 매개 변수
    age = 0
    gender = ''
    
    def __init__(self) -> None: # 생성자 함수(스페셜 함수) 클래스의 객체를 생성할때 동작. 부르지 않아도 자동 호출됨
    ## init == initialize 초기화
        self.name = '홍길동'
        self.age = 29
        self.gender = '남자'

    def __str__(self) -> str:  # class를 호출 할 때 원하는 형태로 변환해서 보여줄때 __str을 사용함
        strs = f'커스텀 출력, 이름 {self.name} 객체 생성'
        return strs
    # 멤버 함수 매개변수 self는 필수!!!
    def walk(self):  # self는 자기 자신, 매개변수에 아무것도 넣지않음. class에서 함수를 만들때 self 사용
        print(f'{self.name}이(가) 걷습니다.')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다')

# 사람 객체 생성, Instance(사례, 예제), 객체 == Instance
mg = Person() # 객체를 생성할때는, 함수 호출처럼 작성하면됨
es = Person()

# print(id(mg)) 다른 객체인지 확인
mg.name = '황정우'  # 객체명.멤버변수 = ...
mg.age = 27
mg.gender = '남자'

es.name = '애슐리'
es.age = 28
es.gender = '여자'

print(f'mg => 이름 : {mg.name} / 나이 : {mg.age}세 / 성별 : {mg.gender}')
print(f'es => 이름 : {es.name} / 나이 : {es.age}세 / 성별 : {es.gender}')

mg.walk()
print('1분동안 걷는다')
mg.stop()

es.walk()
print('걷기 싫음')
es.stop()

print('생성자 함수 추가 이후--------------------------------------------')
gd = Person()
print(f'gd => 이름 : {gd.name} / 나이 : {gd.age}세 / 성별 : {gd.gender}')
print(gd) ## def__str__ 함수 자동 호출