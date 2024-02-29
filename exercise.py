n = input().upper()
dic = list(set(n))
cnt = []
for i in dic:
    cnt.append(n.count(i))
if cnt.count(max(cnt)) > 1:
    print("?")
else :
    print(dic[cnt.index(max(cnt))])