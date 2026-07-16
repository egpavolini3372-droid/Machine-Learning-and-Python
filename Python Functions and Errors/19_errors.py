
#print(0/0) # ZeroDivisionError
#print(result) # NameError

suma = lambda x, y : x + y
assert suma(2,2) == 4 # AssertionError

age = 10

if age < 18:
    raise Exception("No se permiten menores de edad")




