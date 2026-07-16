file = open("./text.txt")
#print(file.read())
#print(file.readline()) # Lee linea 1
#print(file.readline()) # Lee linea 2

for line in file: # leer el archivo linea a linea
    print(line)

#file.close() # cerrar archivo

with open("./text.txt") as file: # forma convencional de cerrar archivos
    for line in file:
         print(line)

