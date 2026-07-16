
from menu import mostrar_menu

def main():
    while True:
        # Mostrar el menu que se esta ofreciendo
        mostrar_menu()    
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
           # pedir un cafe
           pass
        elif opcion == "2":
           # Ver el historial
           pass
        elif opcion == "3":
           print("Gracias por su visita. ¡Hasta luego!")
           break
        else:
              print("Opcion no valida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()