'''
첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

5
20 10 35 30 7
예제 출력 1 
7 35
'''

a = map(int, input().split())
r = list(map(int, input().split()))
max = r[0]
min = r[0]


for i in r[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i
print(min, max)
        



    
