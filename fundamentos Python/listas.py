
frutas = ["manzana", "naranja", "kiwi"]
print(frutas)
print(type(frutas))  # Imprime el tipo de dato de la variable frutas
print(frutas[0])  # Imprime el primer elemento de la lista
print(frutas[-1])  # Imprime el último elemento de la lista
print(len(frutas))  # Imprime la longitud de la lista

frutas[1]="banana"  # Modifica el segundo elemento de la lista
print(frutas)

print(frutas[1:3])  # Imprime una sublista desde el segundo hasta el tercer elemento

if "manzana" in frutas:
    print("La manzana está en la lista de frutas")  # Verifica si "manzana" está en la lista

# Agregar elementos a la lista
# Append
vehiculos = ["auto", "moto", "bicicleta"]
vehiculos.append("camioneta")  # Agrega "camioneta" al final de la lista
print(vehiculos)
# Insert
vehiculos.insert(1, "avión")  # Inserta "avión" en la segunda posición
print(vehiculos)

# Remover elementos de la lista
# Remove
vehiculos.remove("moto")  # Elimina "moto" de la lista
print(vehiculos)
# Pop
vehiculos.pop(1)  # Elimina el segundo elemento de la lista
print(vehiculos)
# Del
del vehiculos[0]  # Elimina el primer elemento de la lista
print(vehiculos)
# Clear
vehiculos.clear()  # Elimina todos los elementos de la lista
print(vehiculos)

vehiculos = ["auto", "moto", "bicicleta"]
vehiculos.sort()  # Ordena la lista en orden alfabético
print(vehiculos)

vehiculos.reverse()  # Invierte el orden de la lista
print(vehiculos)

num1=[3, 1, 4]
num2=[6, 5, 2, 7]
num1.extend(num2)  # Extiende num1 con los elementos de num2
print(num1)
print(num2)
num1.sort()  # Ordena num1 en orden ascendente
print(num1)

num3=num1+num2  # Concatena num1 y num2 en num3
print(num3)
