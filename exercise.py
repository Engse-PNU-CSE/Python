def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)

n = int(input())
m = list(map(int, input().split()))
result = 0
for i in range(n):
    k = m[i]
    if i != 0:
        n = gcd(k, result)
        result = k*result/n
    else :
        result = k
print(int(result))