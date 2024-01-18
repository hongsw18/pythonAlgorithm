'''
출력
각 테스트 케이스에 대해서 바꾼 값과 단위를 출력한다. 값은 반올림해서 소수점 4째자리까지 출력한다. 단위는 kg, lb, l, g중 하나이며, 설명은 입력 설명에 있다.

예제 입력 1 
5
1 kg
2 l
7 lb
3.5 g
0 l
예제 출력 1 
2.2046 lb
0.5284 g
3.1752 kg
13.2489 l
0.0000 g

'''

count = int(input())

for _ in range(count):
    n, m = input().split()
    n = float(n)

    if m == "kg":
        print(f"{n*2.2046:0.4f} lb")
    elif m == "lb":
        print(f"{n*0.4536:0.4f} kg")
    elif m == "l":
        print(f"{n*0.2642:0.4f} g")
    else:
        print(f"{n*3.7854:0.4f} l")

