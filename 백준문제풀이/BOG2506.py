'''
첫째 줄에 문제의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 N개 문제의 채점 결과를 나타내는 0 혹은 1이 빈 칸을 사이에 두고 주어진다. 0은 문제의 답이 틀린 경우이고, 1은 문제의 답이 맞는 경우이다.

출력
첫째 줄에 입력에서 주어진 채점 결과에 대하여 가산점을 고려한 총 점수를 출력한다.

예제 입력 1 
10
1 0 1 1 1 0 0 1 1 0
예제 출력 1 
10

'''
'''
num = [] 
point = 0
n = 1  
m = 0

K = int(input())


for i in range(K):
    point = int()
    if point == 0:
        num = 0
    
    else :
        if num[i] == num[i-1]:
            n += 1
            num = n
            
        else :
            n = 1
            num = 1
        
for i in range(K):
    m = m + num[i]
    
print(m)

'''

# 문제 개수 입력
N = int(input())

# 문제 채점 결과 입력
results = list(map(int, input().split()))

score = 0  # 총 점수
consecutive_correct = 0  # 연속으로 맞춘 문제의 개수

for result in results:
    if result == 1:
        consecutive_correct += 1
        score += consecutive_correct
    else:
        consecutive_correct = 0  # 틀린 경우에는 연속성 초기화

# 결과 출력
print(score)
