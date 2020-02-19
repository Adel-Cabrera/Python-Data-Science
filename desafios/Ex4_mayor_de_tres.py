import random

num_array = []

for i in range(3):
  num_array.append(random.randint(-100, 100))

max_num = max(num_array)

print(num_array)
print(f"El número mayor es {max_num}")
