def cal(n):
    if n == 0:
        return 2
    else:
        return 2*cal(n-1)-1
print(cal(int(input())) ** 2)