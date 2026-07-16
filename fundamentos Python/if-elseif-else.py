if 5>3:
    print("5 es mayor a 3") # Imprime 5 es mayor a 3

x=5
y=3
z=1

if x>y and x>z:
    print("x es mayor a y and z") # Imprime x es mayor a y
elif x == y:
    print("x es igual a y") # No se imprime
else:

    print("y es mayor a x")
a = "python"
b= "java"
c= "c++"
if a == b:
    print("a es igual a b") # No se imprime
elif a == c:
    print("a es igual a c") # No se imprime
else:
    print("a no es igual a b ni a c") # Imprime a no es igual a b ni a c


if a == c:
    if a!=b:
        print("a es diferente de b e igual c") # Imprime a es diferente a b e igual a c
    else:
        print("a no es igual a c") # No se imprime