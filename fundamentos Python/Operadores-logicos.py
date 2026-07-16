x = 5
y = 3
z = 5

print(x == y) # Igualdad
print(x != y) # Desigualdad 
print(x > y)  # Mayor que
print(x < y)  # Menor que
print(x >= y) # Mayor o igual que
print(x <= y) # Menor o igual que

print(x >= z) # Mayor o igual que
print(x <= z) # Menor o igual que

# Operador lógico AND

print(x > y and y > z)  # False 
print(x > y and z >= x) # True

# Operador lógico OR

print(x > y or y > z)  # True
print(y > x or y > z)  # False

# Operador lógico NOT

print(not(x > y))  # False
print(not(y > x))  # True
