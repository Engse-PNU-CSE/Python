import sys
line = list(map(int, sys.stdin.readline().split()))
line.sort()
if line[2] >= line[1] + line[0]:
    print(line[1] + line[0] + line[1] + line[0] - 1)
else :
    print(sum(line))
