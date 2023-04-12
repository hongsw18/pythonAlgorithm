'''

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

5
1 1
2 3
3 4
9 8
5 2
예제 출력 1 
2
5
7
17
7

'''

t = int(input())

for i in range(1,t+1):
    a , b = map(int,input().split())
    print(a+b)





    
