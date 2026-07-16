frutas = {"maçã", "banana", "naranja", "uva","limon","banana","uva"}
print(frutas)
print(type(frutas))
print("Tamaño del conjunto frutas:", len(frutas))




numeros={1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,2,2}
print(numeros)  

for i in numeros:
    print(i)
print("Tamaño del conjunto numeros:", len(numeros))

for j in frutas:
    print(j)

print("banana" in frutas)
print("kiwi" not in frutas)

# Agregar elementos al conjunto
frutas.add("kiwi")
print(frutas)
frutas.update(["mango", "papaya", "piña"]) # Agrega múltiples elementos al conjunto, tambien agrega listas, conjuntos o tuplas
print(frutas)

# Remover elementos del conjunto
frutas.remove("limon")  # Elimina "limon" del conjunto, genera un error si el elemento no existe
print(frutas)
frutas.discard("uva")  # Elimina "uva" del conjunto, no genera error si el elemento no existe
print(frutas)
frutas.pop()  # Elimina un elemento aleatorio del conjunto
print(frutas)
frutas.clear()  # Elimina todos los elementos del conjunto
print(frutas)

conjuntoA={1,2,3,4,5}
conjuntoB={4,5,6,7,8}

# Unión de conjuntos
union=conjuntoA.union(conjuntoB)
print("Unión:", union)
# Intersección de conjuntos
interseccion=conjuntoA.intersection(conjuntoB)
print("Intersección:", interseccion)
# Diferencia de conjuntos
diferencia=conjuntoA.difference(conjuntoB)
print("Diferencia A-B:", diferencia)