import sys
n, score = map(int, input().split())
num = list(map(int, sys.stdin.readline().split()))
count = list()

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
             count.append(num[i] + num[j] + num[k])
if(score in count) : print(score)

