import sys
n, m = map(int, sys.stdin.readline().split())
heardmissing = set()
seemissing = set()
for i in range(n):
    heardmissing.add(sys.stdin.readline().rstrip())
for i in range(m):
    seemissing.add(sys.stdin.readline().rstrip())
result = sorted(heardmissing.intersection(seemissing))
print(len(result))
for v in result:
    print(v)