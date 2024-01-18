'''
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)

둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.


10 5
1 10 4 9 2 3 8 5 7 6
예제 출력 1 
1 4 2 3
'''

a, b = map(int, input().split())
r = list(map(int, input().split()))
for i in range(a):
    if r[i] < b:
        print(r[i], end=" ")



    
