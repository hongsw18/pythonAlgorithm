'''
1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.
공이 들어있지 않은 바구니는 0을 출력한다..

5 4
1 2 3
3 4 4
1 4 1
2 2 2
예제 출력 1 
1 2 1 1 0
'''

n , m = map(int,input().split())
beg = [0] * n

for i in range (m):
    i,j,k = map(int,input().split())
    for x in range(i,j+1):
        beg[x-1] = k
for i in range(n):
    print(beg[i],end = " ")