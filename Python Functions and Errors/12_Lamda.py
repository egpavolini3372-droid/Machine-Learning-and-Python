
def incrementar(x):
    return x + 1

increment_V2 = lambda x : x + 1

resultado = incrementar(10)
resultado2 = increment_V2(10)

print(resultado)
print(resultado2)

fullname = lambda name, lastname: f"Full name is {name.title()}, {lastname.title()}"

text = fullname("Erwin", "Pavolini")
print(text)


