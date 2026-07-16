from re import M


print("Hola, 'mundo'")  # Imprime Hola, 'mundo'

multiples = """Esto es un texto
que abarca varias   líneas
y mantiene    los espacios utilizando comillas triples."""          
print(multiples)    

palabra = 'Python_es_genial'
print(palabra[0])  # Imprime 'P'
print(len(palabra))  # Imprime '14'

estaIncluida = 'genial' in palabra
print(estaIncluida)  # Imprime 'True'   
noEstaIncluida = 'Java' not in palabra
print(noEstaIncluida)  # Imprime 'True'

Mayusculas = palabra.upper()
print(Mayusculas)  # Imprime 'PYTHON_ES_GENIAL'
Minusculas = palabra.lower()
print(Minusculas)  # Imprime 'python_es_genial'

espacios = '   Hola Mundo   '
print(espacios.strip())  # Imprime 'Hola Mundo'
print(espacios)  # Imprime 'Hola Mundo   '