# date : 20240131
# file : test_24_lotto.py
# desc : 로또 번호 생성

import random as rnd # 랜덤은 주로 rnd로 사용

# number = list(range(1,46))
# lottery = list()

# for i in range(6): # 0,1,2,3,4,5 여섯번 반복
#     lottery.append(rnd.choice(number)) # 1~45 까지 숫자 하나를 랜덤으로 꺼내기 choice

# lottery.sort()
# print(lottery)

number = weight = list(range(1,46))
lottery = list()
rnd.shuffle(weight) # 가중치로 섞음

lottery = rnd.choices(number, weights=weight, k=6)
lottery.sort()
print(lottery)