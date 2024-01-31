# date : 20240131
# file : test_22_car.py
# desc : Car class 만들기

class Car:
    wheel_num = 4
    color = 'white'
    __plate_num = '' ## plate_num 앞에 __을 붙히면 인캡슐레이션, 즉 객체를 생성할때 말고는 plate_num을 변경 할 수 없음
    company = ''
    gear_type = ''

    # 전진, 후진, 우회전, 좌회전

    def moveForward(self):
        print(f'{self.__plate_num}이 전진합니다.')

    def moveBackward(self):
        print(f'{self.__plate_num}이 후진합니다.')


    def moveLeft(self):
        print(f'{self.__plate_num}이 좌회전합니다.')
    
    def moveRight(self):
        print(f'{self.__plate_num}이 우회전합니다.')

# 생성자를 변경했으니깐, 변경된 생성자로 호출
    def __init__(self, number, comp, col, gear) -> None:
        self.__plate_num = number
        self.company = comp
        self.color = col
        self.gear_type = gear
    def __str__(self) -> str: # print(객체) 출력되는 부분
        return f'제 차는 {self.__plate_num} 입니다. {self.color} 입니다.'
    
    def getPlateNumber(self): #외부에서는 접근할 수 없도록 막는 조치
        return self.__plate_num

    def setPlateNumber(self, new_plateNumber):
        self.__plate_num = new_plateNumber

sarah = Car('17두3150', '현대 자동차', '회색', '자동')
# 객체를 생성하는 곳과 객체를 사용하는 곳이 다를 수 있습니다.
print(sarah)
print(f'차 번호는 {sarah.getPlateNumber()}')
print(f'차 색상은 {sarah.color}')
sarah.moveForward()

sarah.__plate_num = 'qkqkqkqkqkqk'
print(sarah) # 막아놔서 차번호가 바뀌지 않음

sarah.setPlateNumber('13두3413')
print(sarah) # setPlateNumber 함수를 활용하여 차 번호를 바꿈

# csuv = Car('14호1342', '기아 자동차', '검정색', '자동')
# print(f'차 번호는 {csuv.__plate_num}')