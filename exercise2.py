n = int(input())
a = list(map(int, input().split()))
check = [False for _ in range(n)]
b = sorted(a)
p = []
for i in range(n):
    for j in range(n):
        if(a[i]==b[j] and check[j]==False): 
            p.append(j)
            check[j]=True
print(p)