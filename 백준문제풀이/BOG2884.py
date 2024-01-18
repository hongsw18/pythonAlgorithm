'''
원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다.

24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.

10 10
예제 출력 1 
9 25
'''

h , m = map(int,input().split())

if (m < 45) :
    m = m + 60
    if (h == 0) and (m < 105) :
        print (h + 23 , m - 45)
    elif (h == 0) and (m > 105) :
        print(h , m - 45)
    elif (h != 0) and (m > 105) :
        print(h , m - 45)
    elif (h != 0) and (m < 105) :
        print(h - 1, m -45)
else :
    print(h , m-45)
        
         

