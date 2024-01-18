'''
26
예제 출력 1 
4
'''
n = int(input())  #26
sum = n
count = 0


while True :
    
    a = sum // 10  #2
    b = sum % 10   #6
    c = (a+b) % 10  #8
    sum = (b*10) + c  #68
    
    count = count+1 
    if (sum == n):
        break
print(count)




    
