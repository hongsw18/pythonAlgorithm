'''
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

Mississipi
예제 출력 1 
?

zZa
예제 출력 2 
Z

'''

word = input().upper()
sp_word = list(set(word))

wcnt = []
for x in sp_word:
    a = word.count(x)
    wcnt.append(a)
    
if wcnt.count(max(wcnt)) > 1:
    print("?")
    
else :
    max_cnt = wcnt.index(max(wcnt))
    print(sp_word[max_cnt])
    
    
    