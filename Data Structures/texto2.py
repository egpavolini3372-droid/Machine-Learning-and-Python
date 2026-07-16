texto = "Este es un texto de ejemplo para demostrar operaciones con cadenas en Python."

print(texto[2])  # Imprime el tercer carácter del texto completo
print(len(texto))  # Imprime la longitud total del texto
print(texto[2:7])  # Imprime el tercer carácter del texto completo

curso="este curso es de python "
print(curso.capitalize())  # Imprime 'Este curso es de python '
print(curso.replace("python", "Java"))  # Imprime 'este curso es de

textoDivido =texto.split(" ")
print(textoDivido)  # Imprime la lista de palabras en el texto

# Normalizar texto
texto_mayusculasMasMinusculas = texto.upper()

print(bool("python" in texto_mayusculasMasMinusculas))  # Imprime: False Java '
print(bool(""))  # Imprime: False 
print(bool(0))  # Imprime: False 
print(bool([]))  # Imprime: False  
print(bool(None))  # Imprime: False 

x=410310931.2
print(isinstance(x, int))   # Imprime: False