a = [1, 2, "4"]
b = ["3", "4"]
c = a + b
print(c)
d = b * 3
print(d)

a = [[1, 2, 3], [4, 5, 6]]
b = a[0:2]
a[0][1]=257
print(a, id(a[0][1]))
print(b, id(b[0][1]))