
tecnologias=("Python", "Java", "C++", "JavaScript")
print(tecnologias)  # Imprime 'tupla completa'
print(tecnologias[0])  # Imprime 'Python'
print(tecnologias[1])  # Imprime 'Java'
print(len(tecnologias))  # Imprime '4'
print(type(tecnologias))  # Imprime '<class 'tuple'>'

tupla=("python",5,True)
print(tupla)  # Imprime 'tupla completa'
print(type(tupla))  # Imprime 'python'

x,y,z = tupla
print(x)  # Imprime 'python'
print(y)  # Imprime '5'
print(z)  # Imprime 'True'

tupla*2
print(tupla*2)  # Imprime 'tupla' dos veces

for item in tupla:
    print(item)  # Imprime cada elemento de la tupla en una línea separada  

listaDeTupla= list(tupla)
print(listaDeTupla)  # Imprime la lista convertida de la tupla
listaDeTupla.append(10)
print(listaDeTupla)  # Imprime la lista con el nuevo elemento agregado