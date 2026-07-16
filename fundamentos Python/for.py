palabra = "python"

for letra in palabra:
    print(letra)  # Imprime cada letra de la palabra "python" en una línea separada

frutas=["manzana", "naranja", "kiwi"]

for fruta in frutas:
    print(fruta)  # Imprime cada fruta en la lista en una línea separada


for fruta in frutas:
    if fruta == "naranja":
        break
    print(fruta)  # 
    break


frutas=["manzana", "naranja", "kiwi"]
adjetivos=["riquísima", "ácida", "exótica"]

for fruta in frutas:
    for adjetivo in adjetivos:
        print(fruta + " es " + adjetivo)  # Imprime combinaciones de frutas y adjetivos
        
for fruta in frutas:
    if fruta == "naranja":
        continue
    print(fruta)  # 
    break

for i in range(3,5):
    print(i)  # Imprime 3 y 4

for i in range(2,11,2):
    print(i)  # Imprime 2, 4, 6, 8


