'''
numbers = []

for i in range(1, 11):
    numbers.append(i*2) # Agrega el número i a la lista numbers
print(numbers)

numbers_v2 = [i*2 for i in range(1, 11)]
print(numbers_v2)
'''

numbers = []

for i in range(1, 11):
    if i % 2 == 0:
          numbers.append(i*2) # Agrega el número i a la lista numbers
print(numbers)

numbers_v2 = [i*2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v2)