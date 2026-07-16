from menu import mostrar_menu
def main():
    while True:
        # mostrar el menú
        mostrar_menu()
        opcion=input("Seleccione una opción:\n1. Saludar\n2. Despedirse\n3. Salir\n")  
        if opcion=="1":     
            # pedir un cafe
            pass
        elif opcion=="2":
             # ver el historial de cafes
             pass
        elif opcion=="3":
             print("Saliendo del programa.")
             break
        else:   
             print("Opción no válida. Intente de nuevo.") 
