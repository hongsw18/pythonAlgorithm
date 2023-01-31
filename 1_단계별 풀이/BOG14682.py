'''
(12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다. 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.
'''

a = int(input())
b = int(input())


if (a > 0) and (b > 0):
    print(1)
elif (a < 0) and (b > 0):
    print(2)
elif (a < 0) and (b < 0):
    print(3)
elif (a > 0) and (b < 0):
    print(4)