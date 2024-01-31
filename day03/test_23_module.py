# date : 20240131
# file : test_23_module.py
# desc : 모듈 사용

import math

PI = 3.141592

radius = 5
print(f'원의 크기는 {radius * radius * PI}')

# print(math.pi)
print(f'정확한 원의 크기는 {radius * radius * math.pi}')

print(f'cos(0) = {math.cos(0)}')

print(2**10)
print(math.pow(2,10))
print(round(3.5))

import math as m
print(m.sin(1))

from math import pi, pow  # 조심해서 사용

print(pi)
print(pow(2,19))