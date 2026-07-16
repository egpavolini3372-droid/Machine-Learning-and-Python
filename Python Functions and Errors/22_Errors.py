
try:
    print(0/0) # ZeroDivisionError
except ZeroDivisionError as error:
    print(error) # NameError


try:
    suma = lambda x, y : x + y
    assert suma(2,2) == 5 # AssertionError
except AssertionError as error2:
    print(error2)

try:
    age = 10    
    if age < 18:
         raise Exception("No se permiten menores de edad")
except Exception as error3:
    print(error3)
 