import sys
n, m = map(int, sys.stdin.readline().split())
a = set(map(int, sys.stdin.readline().split()))
b= set(map(int, sys.stdin.readline().split()))

c = a.union(b) - a.intersection(b)
print(len(c))