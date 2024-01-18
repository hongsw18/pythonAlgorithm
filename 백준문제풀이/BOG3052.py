'''
첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.
'''


a = []

for i in range(10):
    b = int(input())
    c = b % 42
    a.append(c)
    
d = set(a)
print(len(d))