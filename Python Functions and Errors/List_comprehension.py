
numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = [i for i in numbers if i % 2 == 0]

print('v2 =>', even_numbers_v2)

x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print(y)
print(type(y))

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])