'''
입력
20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.

출력
치훈이의 전공평점을 출력한다.

정답과의 절대오차 또는 상대오차가 
\(10^{-4}\) 이하이면 정답으로 인정한다.

제한
1 ≤ 과목명의 길이 ≤ 50
과목명은 알파벳 대소문자 또는 숫자로만 이루어져 있으며, 띄어쓰기 없이 주어진다. 입력으로 주어지는 모든 과목명은 서로 다르다.
학점은 1.0,2.0,3.0,4.0중 하나이다.
등급은 A+,A0,B+,B0,C+,C0,D+,D0,F,P중 하나이다.
적어도 한 과목은 등급이 P가 아님이 보장된다.
예제 입력 1 
ObjectOrientedProgramming1 3.0 A+
IntroductiontoComputerEngineering 3.0 A+
ObjectOrientedProgramming2 3.0 A0
CreativeComputerEngineeringDesign 3.0 A+
AssemblyLanguage 3.0 A+
InternetProgramming 3.0 B0
ApplicationProgramminginJava 3.0 A0
SystemProgramming 3.0 B0
OperatingSystem 3.0 B0
WirelessCommunicationsandNetworking 3.0 C+
LogicCircuits 3.0 B0
DataStructure 4.0 A+
MicroprocessorApplication 3.0 B+
EmbeddedSoftware 3.0 C0
ComputerSecurity 3.0 D+
Database 3.0 C+
Algorithm 3.0 B0
CapstoneDesigninCSE 3.0 B+
CompilerDesign 3.0 D0
ProblemSolving 4.0 P
예제 출력 1 
3.284483

'''

# 과목별 등급에 대한 점수 매핑
grade_points = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0, 'P': None}

# 치훈이의 전공평점 계산 함수
def calculate_gpa(subjects):
    total_credit = 0  # 총 학점
    total_grade_points = 0  # 등급별 총 점수

    for subject in subjects:
        credit, grade = subject[1], subject[2]
        
        # 등급이 'P'인 경우 계산에서 제외
        if grade == 'P':
            continue

        total_credit += credit
        total_grade_points += credit * grade_points[grade]

    if total_credit == 0:
        return 0.0  # 학점이 없는 경우 0.0 반환
    else:
        return total_grade_points / total_credit

# 입력 받기
subjects = []
for _ in range(20):
    subject_info = input().split()
    subjects.append((subject_info[0], float(subject_info[1]), subject_info[2]))

# 전공평점 계산 및 출력
result = calculate_gpa(subjects)
print(f"{result:.6f}")