'''
첫째 줄에 두 정수 A, B가 주어진다. (-2,147,483,648 ≤ A, B ≤ 2,147,483,647)

출력
첫째 줄에 답을 출력한다. (-2,147,483,648 ≤ 답 ≤ 2,147,483,647)

예제 입력 1 
1 2
예제 출력 1 
3

'''

def find_sum_between_numbers(a, b):
    # 두 수 중 작은 수와 큰 수를 찾음
    start = min(a, b)
    end = max(a, b)

    # 사이에 있는 수들의 합을 구함
    total_sum = sum(range(start, end + 1))

    return total_sum

# 입력 받기
a, b = map(int, input().split())

# 결과 출력
result = find_sum_between_numbers(a, b)
print(result)
