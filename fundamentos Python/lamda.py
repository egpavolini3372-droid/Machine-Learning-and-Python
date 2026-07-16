

x = lambda a, b: a + b
print(x(5, 3))

def mi_funcion(k):
    return lambda a: a * k

double = mi_funcion(2)
triple = mi_funcion(3)
cuadriple = mi_funcion(4)
quintuple = mi_funcion(5)  

print(double(10))  # Imprime 20
print(triple(10))  # Imprime 30
print(cuadriple(10))  # Imprime 40
print(quintuple(10))  # Imprime 50