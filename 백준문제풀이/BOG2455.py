'''
입력
각 역에서 내린 사람 수와 탄 사람 수가 빈칸을 사이에 두고 첫째 줄부터 넷째 줄까지 역 순서대로 한 줄에 하나씩 주어진다. 

출력
첫째 줄에 최대 사람 수를 출력한다.  

예제 입력 1 
0 32
3 13
28 25
39 0
예제 출력 1 
42


'''


score = [0] * 4 
n = 0 

for i in range(4):
   
    A, B = map(int, input().split())
    n = n + B - A
    score[i] = n
    
print(max(score))    

