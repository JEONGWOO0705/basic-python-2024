# date : 20240131
# file : test_19_starprint.py
# desc : 별찍기 또는 파리미드 만들기

for i in range(1,5+1):
    # 첫번째 i가 1일때는 range(1,2) 1번 반복
    # i가 2이면, range(1,3), 2번 반복
    for j in range(1,6-i+1): 
        print('*', end='') # 엔터대신 empty
    print()




