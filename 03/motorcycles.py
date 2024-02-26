motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(2, 'BMW')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)
print(motorcycles)

motorcycles.append('BMW')
print(motorcycles)

motorcycles.remove('BMW')
print(motorcycles)