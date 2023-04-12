'''
첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지 않는다. 
단어는 공백 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 또한 문자열은 공백으로 시작하거나 끝날 수 있다.

The Curious Case of Benjamin Button
예제 출력 1 
6

 The first character is a blank
예제 출력 2 
6
'''

word = input().split()
print(len(word))
    
    