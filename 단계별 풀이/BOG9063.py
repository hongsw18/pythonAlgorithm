'''
입력
첫째 줄에는 점의 개수 N (1 ≤ N ≤ 100,000) 이 주어진다. 이어지는 N 줄에는 각 점의 좌표가 두 개의 정수로 한 줄에 하나씩 주어진다. 각각의 좌표는 -10,000 이상 10,000 이하의 정수이다. 

출력
첫째 줄에 N 개의 점을 둘러싸는 최소 크기의 직사각형의 넓이를 출력하시오. 

예제 입력 1 
3
20 24
40 21
10 12
예제 출력 1 
360
예제 입력 2 
1
15 13
예제 출력 2 
0

'''

import sys

input = sys.stdin.readline
x_lst = []
y_lst = []
for _ in range(int(input())) :
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)
print((max(x_lst) - min(x_lst)) * (max(y_lst) - min(y_lst)))
      