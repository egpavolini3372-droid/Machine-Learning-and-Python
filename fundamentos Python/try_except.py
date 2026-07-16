
try:
    numero=10/0
    print(numero)
except ZeroDivisionError:
    print("Error: División por cero no permitida.")

try:
    print(x)  # Esto generará un error NameError
except NameError:
    print("Error: La variable 'x' no está definida.")
