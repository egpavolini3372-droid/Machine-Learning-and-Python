
from ast import Import
from random import random


x=1 # Entero
y=2.5 # Flotante
z=3+4j # Complejo

print(type(x))  # Imprime: <class 'int'>
print(type(y))  # Imprime: <class 'float'>
print(type(z))  # Imprime: <class 'complex'>

positivo = 10
negativo = -5       

x_f=float(x)  # Convierte entero a flotante
print(x_f)  # Imprime: 1.0

y_i=int(y)    # Convierte flotante a entero
print(y_i)  # Imprime: 2    

entero=5
flotante=5.5

enteroComplejo=complex(entero)  # Convierte entero a complejo
flotanteComplejo=complex(flotante)  # Convierte flotante a complejo     
print(enteroComplejo)  # Imprime: (5+0j)
print(flotanteComplejo)  # Imprime: (5.5+0j)

import random
num_aleatorio = random.randrange(1,10)  # Genera un número aleatorio entre 1 y 10
print(num_aleatorio)