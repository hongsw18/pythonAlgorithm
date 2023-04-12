'''
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

5
54321
예제 출력 2 
15
'''

a = int(input())
b = list(input())

total = 0

for i in range(a):
    total += int(b[i])

print(total)