'''
 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
 
 0 1 2 2 2 7
예제 출력 1 
1 0 0 0 0 1
'''

chess = [1, 1, 2, 2, 2, 8]
a = list(map(int,input().split()))
for i in range(6):
    chess[i] = chess[i] - a[i]
print(*chess)