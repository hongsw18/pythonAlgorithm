'''
5
1 1
2 3
3 4
9 8
5 2
예제 출력 1 
Case #1: 2
Case #2: 5
Case #3: 7
Case #4: 17
Case #5: 7
'''
t = int(input())
i = 0

for _ in range(t):
    a , b = map(int,input().split())
    i += 1
    print(f'Case #{i}: {a+b}')





    
