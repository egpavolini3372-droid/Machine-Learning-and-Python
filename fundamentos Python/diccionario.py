
from webbrowser import get


auto=   {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020,
    "color": "Rojo"
}
print(auto)
print("Marca del auto:", auto["marca"])
print(auto.get("modelo"))
print(auto.keys())
print(auto.values())

if "año" in auto:
    print("El año del auto es:", auto["año"])

auto["color"] = "Azul"

print("Color modificado:", auto["color"])
print(auto)

auto.update({"año": 2021, "precio": 20000})
print("Año y precio actualizados:", auto)
print(auto)

auto.pop("modelo")
print("Después de eliminar el modelo:", auto)

auto.popitem()
print("Después de eliminar el último elemento agregado:", auto)

auto=   {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020,
    "color": "Rojo"
}

for k in auto:
    print(k, ":", auto[k])

for k,v in auto.items():
    print(k, "->", v)

familia={
    "hijo1": {"nombre": "Juan", "edad": 10},
    "hijo2": {"nombre": "Ana", "edad": 8},
    "hijo3": {"nombre": "Luis", "edad": 12}
}
print(familia)
print("Nombre del hijo2:", familia["hijo2"]["nombre"])