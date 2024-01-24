# 다섯 줄의 입력을 받아서 2차원 리스트에 저장
board = [input() for _ in range(5)]

# 결과를 저장할 변수 초기화
result = ""

# 각 열에 대해서 세로로 읽기
for col in range(15):
    for row in range(5):
        # 현재 열의 길이가 현재 행의 길이보다 크면 글자가 있다는 뜻
        if col < len(board[row]):
            result += board[row][col]

# 결과 출력
print(result)