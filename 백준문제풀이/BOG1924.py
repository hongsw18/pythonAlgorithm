'''
입력
첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다. 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.

출력
첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.

예제 입력 1 
1 1
예제 출력 1 
MON
예제 입력 2 
3 14

'''
def day_of_week(x, y):
    # 각 월의 일 수를 리스트로 저장
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 2007년 1월 1일은 월요일이므로 해당 요일을 기준으로 초기화
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    total_days = y - 1

    for i in range(1, x):
        total_days += days_in_month[i]

    day_of_week_index = (total_days) % 7  

    return days[day_of_week_index]

# 입력 받기
x, y = map(int, input().split())

# 결과 출력
result = day_of_week(x, y)
print(result)

