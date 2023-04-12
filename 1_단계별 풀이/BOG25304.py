'''

260000
4
20000 5
30000 2
10000 6
5000 8
예제 출력 1 
Yes
'''
c = 0
p = int(input())
t = int(input())

for _ in range(t):
    a , b = map(int,input().split())
    c = c + a*b
    
if p == c:
    print("Yes")
else :
    print("No")





    
