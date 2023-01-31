'''
472
385
예제 출력 1 
2360
3776
1416
181720
'''

a = int(input())
b = input()


for i in range(2, -1, -1) :
    print(a * int(b[i]))
    

print(a*int(b))
