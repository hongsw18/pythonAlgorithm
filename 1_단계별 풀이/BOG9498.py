'''
90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력

시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수


'''

a = int(input())

if (0 <= a) & (a <= 100) & (a > 89):
    print("A")
if (0 <= a) & (a <= 100) & (a > 79) & (a < 90) & (a <= 89):
    print("B") 
if (0 <= a) & (a <= 100) & (a > 69) & (a <= 79) & (a < 80): 
    print("C")
if (0 <= a) & (a <= 100) & (a > 59) & (a <= 69) & (a < 70):
    print("D")
if (0 <= a) & (a <= 100) & (a < 60):
    print("F")    