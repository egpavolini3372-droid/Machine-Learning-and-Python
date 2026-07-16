def msaludar(nombre, nacionalidad="Argentina"):
    print("Hola", nombre, "de", nacionalidad)

msaludar("Pepe")
msaludar("Luis")
msaludar("Ana", "Chile")

def sumar(a,b):
    return a + b

resultadosumar = sumar(3,5)
print("El resultado de la suma es:", resultadosumar)

def multiplicar(a,b):
    return a * b

resul_multiplicar = multiplicar(4,6)
print("El resultado de la multiplicación es:", resul_multiplicar)

def dividir(a,b):
    if b == 0:
        return "Error: División por cero"
    return a / b
resul_dividir = dividir(50,2)
print("El resultado de la división es:", resul_dividir)