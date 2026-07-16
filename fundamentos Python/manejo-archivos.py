
# manejo-archivos.py
# Read (r)
# Write (w)
# Append (a)
# create (x)

try:
    f=open("archivo.txt", "r")
    print(f.readline())
    f.close()
except FileNotFoundError:
    print("Error: Archivo no encontrado.")

try:
    f=open("archivo.txt", "w")
    print(f.readline())
    f.close()
except FileNotFoundError:
    print("Error: Archivo no encontrado.")