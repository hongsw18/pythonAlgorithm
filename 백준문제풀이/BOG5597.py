'''
입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.
'''
# 1부터 30까지의 리스트를 생성 
num = [i for i in range(1, 31)]

# 입력받은 숫자를 리스트에서 제거
for _ in range(28):
    data = int(input())
    num.remove(data)
print(min(num))
print(max(num))