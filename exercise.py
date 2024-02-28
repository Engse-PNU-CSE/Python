ran = list(map(int, input().split()))
myList = list(map(int, input().split()))

for i in myList:
    if(i < ran[1]):
        print(i, end=" ")
