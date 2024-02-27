squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares, value)

squares = [value ** (1/3) for value in range(1, 11)]
print(squares, value)