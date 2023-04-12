'''
첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
둘째 줄부터 M개의 줄에 걸쳐서 공을 교환할 방법이 주어진다. 각 방법은 두 정수 i j로 이루어져 있으며, i번 바구니와 j번 바구니에 들어있는 공을 교환한다는 뜻이다. (1 ≤ i ≤ j ≤ N)
도현이는 입력으로 주어진 순서대로 공을 교환한다.

5 4
1 2
3 4
1 4
2 2
예제 출력 1 
3 1 4 2 5
'''

n , m = map(int,input().split())
beg = []
ori = int
for i in range(n):
    beg.append(i+1)

for x in range (m):
    i,j = map(int,input().split())
    ori = beg[i-1]
    beg[i-1] = beg[j-1]
    beg[j-1] = ori
for i in range(n):
    print(beg[i],end = " ")