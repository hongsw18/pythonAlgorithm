'''
입력
첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.

출력
첫째 줄에 상수의 대답을 출력한다.

예제 입력 1 
734 893
예제 출력 1 
437

'''

def change_num(a, b):
    sum = (a % 10) * 100
    sum = sum + ((a // 10) % 10) * 10
    sum = sum + a // 100

    n = (b % 10) * 100
    n = n + ((b // 10) % 10) * 10
    n = n + b // 100

    result = max(sum, n)

    return result

a, b = map(int, input().split())
print(change_num(a, b))
