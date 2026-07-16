# Operadores Asignación
a = 10
a = a + 5  # Asignación simple

print(a)  # Imprime: 15

a = 10 
a += 5  # Asignación con suma
print(a)  # Imprime: 15

a = 10
a -= 3  # Asignación con resta      
print(a)  # Imprime: 7

a = 10
a *= 2  # Asignación con multiplicación 
print(a)  # Imprime: 20

a = 10
a /= 2  # Asignación con división       
print(a)  # Imprime: 5.0

a = 10
a %= 3  # Asignación con módulo
print(a)  # Imprime: 1

a = 10  
a **= 2  # Asignación con exponenciación
print(a)  # Imprime: 100

a = 10
a //= 3  # Asignación con división entera
print(a)  # Imprime: 3  

# WALRUS (Asignación con expresión) WALRUS=Morsa :=
if (n := 5) > 3:    # Asignación de una variable dentro de una expresión
    print(n)  # Imprime: 5