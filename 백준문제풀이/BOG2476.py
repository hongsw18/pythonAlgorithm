'''

첫째 줄에는 참여하는 사람 수 N이 주어지고 그 다음 줄부터 N개의 줄에 사람들이 주사위를 던진 3개의 눈이 빈칸을 사이에 두고 각각 주어진다. 

출력
첫째 줄에 가장 많은 상금을 받은 사람의 상금을 출력한다.

예제 입력 1 
3
3 3 6
2 2 2
6 2 5
예제 출력 1 
12000

'''

sum = [] 

count = int(input())

for _ in range(count):
    a,b,c = map(int,input().split()) 
    
    if a == b == c :
        sum.append(10000+(a)*1000)
        
    elif a == b != c:
        sum.append(1000+(a)*100)
    
    elif a == c :
        sum.append(1000+(a)*100)  
      
    elif a != b == c:
        sum.append(1000+(b)*100)
        
    elif a != b != c:
        sum.append(max(a, b, c) * 100)
        
        
    
print(max(sum))