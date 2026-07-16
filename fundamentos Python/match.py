dia = 0

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3: 
        print("Miércoles")
    case 4:

        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")            
    case _:
        print("Día no válido")


fruta = "fresa"
match fruta:
    case "limon":
        print("hoy debo tomar jugo de limon")
    case "manzana":
        print("hoy debo tomar jugo de manzana")
    case "naranja": 
        print("hoy debo tomar jugo de naranja")
    case "pera":
        print("hoy debo tomar jugo de pera")
    case "uva":
        print("hoy debo tomar jugo de uva")
    case "sandía":
        print("hoy debo tomar jugo de sandía")
    case "fresa":
        print("hoy debo tomar jugo de fresa")
    case _:
        print("Fruta no válida")