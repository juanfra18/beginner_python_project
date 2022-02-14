from funciones import *
salir = False
while not salir:
    print("\nMENÚ PRINCIPAL\n\n")
    opcion = input("Ingrese que quiere hacer:\n'1': Gestión vuelos\n'2': Gestión pasajeros\n'3': Consultas\nIngrese otro para salir: ")
    if opcion == "1":
        gestion_vuelos()
    elif opcion == "2":
        gestion_pasajeros()
    elif opcion == "3":
        consultas()
    else:
        salir = True