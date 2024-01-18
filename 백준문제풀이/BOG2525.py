'''
오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.


14 30
20
예제 출력 1 
14 50
23 48
25

'''

h , m = map(int,input().split())
t = int(input())

h += (t // 60)
m += (t % 60)

if m >= 60 :
    m-= 60
    h+= 1
if h >=24 :
    h -= 24

print(h,m)
    
             

