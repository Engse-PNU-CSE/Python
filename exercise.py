import sys
n = int(sys.stdin.readline())
x, y  = map(int, sys.stdin.readline().split())

max_x, min_x = x, x
max_y, min_y = y, y
for _ in range(n-1) :
    x, y  = map(int, sys.stdin.readline().split())
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    min_x = min(x, min_x)
    min_y = min(y, min_y)
print((max_x-min_x)*(max_y-min_y))
