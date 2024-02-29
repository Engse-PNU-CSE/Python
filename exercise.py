n = int(input())
for i in range(n):
    coin = [0, 0, 0, 0]
    money = int(input())
    while money > 0:
        if(money >= 25):
            coin[0]=int(money/25)
            money -= int(money/25)*25
        elif(money >= 10):
            coin[1]=int(money/10)
            money -= int(money/10)*10
        elif(money >= 5):
            coin[2]=int(money/5)
            money -= int(money/5)*5
        else:
            coin[3]=money
            money=0
    for c in coin:
        print(c, end=" ")
    print()