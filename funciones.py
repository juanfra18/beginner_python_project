"""
FUNCIONES BASE
"""
def ordenar(vector):
    n = len(vector)
    for h in range(n):
        for i in range(n - 1):
            if vector[i] > vector[i + 1]:
                aux = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = aux

def nuevo_vuelo(numero, salida, destino, aerolinea, maximo):
    file = open("vuelos.txt", "a")
    vuelo = f"{numero},{salida},{destino},{aerolinea},{maximo},0"
    file.write(f"{vuelo}\n")
    file.close()

def existe_vuelo(numero):
    file = open("vuelos.txt", "r")
    array = file.readlines()
    n = len(array)
    contador = 0
    for i in range(n):
        linea = array[i]
        vector = linea.split(",")
        if vector[0] == numero:
            contador += 1
    file.close()
    if contador >= 1:
        return True
    else:
        return False

def busca_vuelo(numero):
    archivo = open("vuelos.txt", "r")
    array = archivo.readlines()
    n = len(array)
    for i in range(n):
        linea = array[i]
        vector = linea.split(",")
        if vector[0] == numero:
            lugar = i
            archivo.close()
            return lugar

def aumentar_pasajeros(numero):
    lugar = busca_vuelo(numero)
    file = open("vuelos.txt", "r")
    vuelos = file.readlines()
    file.close()
    vuelo = vuelos[lugar]
    arrayvuelo = vuelo.split(",")
    n = int(arrayvuelo[5].strip())
    n += 1
    h = str(n)
    arrayvuelo[5] = f"{h}\n"
    vuelo = ",".join(arrayvuelo)
    vuelos[lugar] = vuelo
    file = open("vuelos.txt", "w")
    for linea in vuelos:
        file.write(linea)
    file.close()

def disminuir_pasajeros(numero):
    lugar = busca_vuelo(numero)
    file = open("vuelos.txt", "r")
    vuelos = file.readlines()
    file.close()
    vuelo = vuelos[lugar]
    arrayvuelo = vuelo.split(",")
    n = int(arrayvuelo[5].strip())
    n -= 1
    h = str(n)
    arrayvuelo[5] = f"{h}\n"
    vuelo = ",".join(arrayvuelo)
    vuelos[lugar] = vuelo
    file = open("vuelos.txt", "w")
    for linea in vuelos:
        file.write(linea)
    file.close()

def busca_pasajero(dni):
    archivo = open("pasajeros.txt", "r")
    array = archivo.readlines()
    n = len(array)
    for i in range(n):
        linea = array[i]
        vector = linea.split(",")
        if vector[0] == dni:
            lugar = i
            archivo.close()
            return lugar

def vuelo_pasajero(dni):
    file = open("pasajeros.txt", "r")
    array = file.readlines()
    place = busca_pasajero(dni)
    linea = array[place]
    vector = linea.split(",")
    vuelo = vector[3].strip()
    file.close()
    return vuelo

def vuelo_lleno(numero):
    file = open("vuelos.txt", "r")
    lugar = busca_vuelo(numero)
    vuelos = file.readlines()
    linea = vuelos[lugar]
    vuelo = linea.split(",")
    file.close()
    if vuelo[5].strip() == vuelo[4]:
        return True
    else:
        return False

def existe_pasajero(dni):
    file = open("pasajeros.txt", "r")
    array = file.readlines()
    n = len(array)
    contador = 0
    for i in range(n):
        linea = array[i]
        vector = linea.split(",")
        if vector[0] == dni:
            contador += 1
    file.close()
    if contador >= 1:
        return True
    else:
        return False   

def existe_pasajero_en_vuelo(dni, numero):
    contador = 0
    file = open("pasajeros.txt", "r")
    pasajeros = file.readlines()
    n = len(pasajeros)
    for i in range(n):
        linea = pasajeros[i]
        pasajero = linea.split(",")
        if pasajero[0] == dni and pasajero[3] == f"{numero}\n":
            contador += 1
    file.close()
    if contador == 1:
        return True
    else:
        return False

def nuevo_pasajero(dni, nombre, apellido, vuelo):
    file = open("pasajeros.txt", "a")
    pasajero = f"{dni},{nombre},{apellido},{vuelo}"
    file.write(f"{pasajero}\n")
    file.close()

def borrar_pasajero(dni):
    file = open("pasajeros.txt", "r")
    array1 = file.readlines()
    array2 = array1
    n = len(array1)
    for i in range(n):
        linea = array1[i]
        vector = linea.split(",")
        if vector[0] == dni:
            array2[i] = ""
    file.close()
    file = open("pasajeros.txt", "w")
    for h in range(n):
        file.write(array2[h])
    file.close()

def borrar_vuelo(numero):
    file = open("vuelos.txt", "r")
    array1 = file.readlines()
    array2 = array1
    n = len(array1)
    for i in range(n):
        linea = array1[i]
        vector = linea.split(",")
        if vector[0] == numero:
            array2[i] = ""
    file.close()
    file = open("vuelos.txt", "w")
    for h in range(n):
        file.write(array2[h])
    file.close()   

def borrar_pasajeros_vuelo(numero):
    file = open("pasajeros.txt", "r")
    array1 = file.readlines()
    array2 = array1
    n = len(array1)
    for i in range(n):
        linea = array1[i]
        vector = linea.split(",")
        if vector[3].strip() == numero:
            array2[i] = ""
    file.close()
    file = open("pasajeros.txt", "w")
    for h in range(n):
        file.write(array2[h])
    file.close()

def cambiar_vuelo(numero, opcion): 
    file = open("vuelos.txt", "r")
    array = file.readlines()
    for i in range(len(array)):
        linea = array[i]
        vuelo = linea.split(",")
        if vuelo[0] == numero:
            if opcion == "1":
                vuelo[1] = input("Ingrese la nueva ciudad de partida: ")
            elif opcion == "2":
                vuelo[2] = input("Ingrese la nueva ciudad de destino: ")
            elif opcion == "3":
                vuelo[3] = input("Ingrese la nueva aerolínea: ")
            elif opcion == "4":
                vuelo[4] = input("Ingrese la nueva cantidad máxima de pasajeros: ")
            linea = ",".join(vuelo)
            array[i] = linea
    file.close()
    file = open("vuelos.txt", "w")
    for line in array:
        file.write(line)
    file.close()

def vuelos_aerolinea(aerolinea):
    file = open("vuelos.txt", "r")
    array1 = file.readlines()
    array2 = []
    file.close()
    for linea in array1:
        vuelo = linea.split(",")
        if vuelo[3] == aerolinea:
            array2.append(linea)
    return array2   

def pasajeros_vuelo(numero):
    file = open("pasajeros.txt", "r")
    array1 = file.readlines()
    array2 = []
    file.close()
    for linea in array1:
        pasajero = linea.split(",")
        nro = pasajero[3].strip()
        if nro == numero:
            array2.append(linea)
    return array2
    
def vuelos_destino(destino):
    file = open("vuelos.txt", "r")
    array1 = file.readlines()
    array2 = []
    file.close()
    for linea in array1:
        vuelo = linea.split(",")
        if vuelo[2] == destino:
            array2.append(linea)
    return array2     

"""
FUNCIONES DE LAS OPCIONES
"""
#GESTIÓN VUELOS
def crear_vuelo():
    exite = False
    while not exite:
        salir = False
        while not salir:
            nro = input("Ingrese el número de vuelo a añadir: ")
            if existe_vuelo(nro):
                print("El vuelo ya existe")
            elif nro == "0":
                print("No se puede añadir un vuelo con dicho número")
            else:
                salir = True
        partida = input("Ingrese la ciudad de partida: ")
        llegada = input("Ingrese el destino: ")
        aero = input("Ingrese la aerolínea del vuelo: ")
        maximo = input("Ingrese la cantidad máxima de pasajeros: ")
        nuevo_vuelo(nro, partida, llegada, aero, maximo)
        print("\nHecho\n\n")
        opcion = input("Ingrese '0' para salir, otra tecla para añadir más vuelos: ")
        if opcion == "0":
            exite = True

def eliminar_vuelo():
    salir = False
    while not salir:
        nro = input("Ingrese el número de vuelo a eliminar. Ingrese '0' para salir: ")
        if nro == "0":
            salir = True
        elif existe_vuelo(nro):
            borrar_vuelo(nro)
            borrar_pasajeros_vuelo(nro)
            print("\nHecho\n\n")
        else:
            print("El vuelo no existe")

def modificar_vuelo():
    salir = False
    while not salir:
        nro = input("Ingrese el número de vuelo a modificar. Ingrese '0' para salir: ")
        if nro == "0":
            salir = True
        elif existe_vuelo(nro):
            exite = False
            while not exite:
                file = open("vuelos.txt", "r")
                vuelos = file.readlines()
                lugar = busca_vuelo(nro)
                vuelo = vuelos[lugar].split(",")
                print(f"\nDATOS DEL VUELO:\n\nNúmero de vuelo: {vuelo[0]}\nPartida: {vuelo[1]}\nDestino: {vuelo[2]}\nAerolínea: {vuelo[3]}\nMáximo de pasajeros: {vuelo[4]}\nPasajeros actuales: {vuelo[5]}\n\n")
                file.close()
                opcion = input("Ingrese el dato del vuelo a modificar. 1: salida; 2: destino; 3: aerolínea; 4: maximo;\notro para salir: ")
                if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4":
                    cambiar_vuelo(nro, opcion)
                    print("\nHecho\n")
                else:
                    exite = True 
        else:
            print("El vuelo no existe")
#GESTIÓN PASAJEROS
def agregar_pasajero():
    salir = False
    while not salir:
        nro = input("\nIngrese el número del vuelo al que quiere añadir al pasajero: ")
        if not existe_vuelo(nro):
            print("El vuelo no existe")
        else:
            if vuelo_lleno(nro):
                print("El vuelo está lleno")
                break
            else:
                dni = input("Ingrese el dni del nuevo pasajero: ")
                if existe_pasajero_en_vuelo(dni, nro):
                    print("El pasajero ya está asignado al vuelo")
                else:
                    apellido = input("Ingrese el apellido: ")
                    nombre = input("Ingrese el nombre: ")
                    nuevo_pasajero(dni, nombre, apellido, nro)
                    aumentar_pasajeros(nro)
                    print("\nHecho\n\n")
                    opcion = input("Ingrese '0' para salir, otra tecla para añadir más pasajeros: ")
                    if opcion == "0":
                        salir = True

def eliminar_pasajero():
    salir = False
    while not salir:
        dni = input("Ingrese el dni del pasajero a eliminar. Ingrese '0' para salir: ")
        if dni == "0":
            salir = True
        elif existe_pasajero(dni):
            file = open("pasajeros.txt", "r")
            array = file.readlines()
            for i in range(len(array)):
                linea = array[i]
                pasajero = linea.split(",")
                if pasajero[0] == dni:
                    nro = pasajero[3].strip()
                    disminuir_pasajeros(nro)
            file.close()
            borrar_pasajero(dni)
            print("\nHecho\n\n")
        else:
            print("El pasajero no existe")

def modificar_pasajero():
    salir = False
    while not salir:
        dni = input("Ingrese el dni del pasajero a modificar. Ingrese '0' para salir: ")
        if dni == "0":
            salir = True
        elif not existe_pasajero(dni):
            print("El pasajero no existe")
        else:
            file = open("pasajeros.txt", "r")
            array = file.readlines()
            for i in range(len(array)):
                linea = array[i]
                pasajero = linea.split(",")
                if pasajero[0] == dni:
                    exite = False
                    while not exite:
                        vuelo1 = pasajero[3].strip()
                        print(f"\nDATOS DEL PASAJERO:\nDNI: {pasajero[0]}\nNombre: {pasajero[1]}\nApellido: {pasajero[2]}\nNúmero de vuelo: {vuelo1}\n\n")
                        opcion = input("Ingrese que quiere modificar. 1: dni; 2: nombre; 3: apellido; 4: vuelo.\nIngrese otro para salir: ")
                        if opcion == "1":
                            pasajero[0] = input("Ingrese el nuevo dni: ")
                        elif opcion == "2":
                            pasajero[1] = input("Ingrese el nuevo nombre: ")
                        elif opcion == "3":
                            pasajero[2] = input("Ingrese el nuevo apellido: ")
                        elif opcion == "4":
                            cont = False
                            while not cont:
                                vuelo2 = input("Ingrese el nuevo vuelo. Ingrese '0' para salir: ")
                                if vuelo2 == "0":
                                    cont = True
                                elif existe_vuelo(vuelo2):
                                    if existe_pasajero_en_vuelo(dni, vuelo2):
                                        print("El pasajero ya está en el vuelo")
                                    elif vuelo_lleno(vuelo2):
                                        print("El nuevo vuelo está lleno")
                                    else:
                                        disminuir_pasajeros(vuelo1)
                                        pasajero[3] = f"{vuelo2}\n"
                                        aumentar_pasajeros(vuelo2)
                                        cont = True
                                else:
                                    print("El vuelo no existe")
                        else:
                            exite = True
                    linea = ",".join(pasajero)
                    array[i] = linea
            file.close()
            file = open("pasajeros.txt", "w")
            for line in array:
                file.write(line)
            file.close()

#CONSULTAS
def listar_vuelos():
    file = open("vuelos.txt", "r")
    vector = file.readlines()
    ordenar(vector)
    for linea in vector:
        vuelo = linea.split(",")
        print(f"\nNro. de vuelo: {vuelo[0]}")
        print(f"Lugar de partida: {vuelo[1]}")
        print(f"Destino: {vuelo[2]}")
        print(f"Aerolínea: {vuelo[3]}")
        print(f"Cantidad máxima de pasajeros: {vuelo[4]}")
        print(f"Cantidad de pasajeros actual: {vuelo[5]}")
        print("--------------------------------------------------")
    file.close()

def listar_vuelos_aerolinea():
    aero = input("Ingrese de que aerolínea quiere ver los vuelos: ")
    vector = vuelos_aerolinea(aero)
    ordenar(vector)
    for linea in vector:
        vuelo = linea.split(",")
        print(f"\nNro. de vuelo: {vuelo[0]}")
        print(f"Lugar de partida: {vuelo[1]}")
        print(f"Destino: {vuelo[2]}")
        print(f"Aerolínea: {vuelo[3]}")
        print(f"Cantidad máxima de pasajeros: {vuelo[4]}")
        print(f"Cantidad de pasajeros actual: {vuelo[5]}")
        print("--------------------------------------------------")

def listar_pasajeros():
    file = open("pasajeros.txt", "r")
    vector = file.readlines()
    ordenar(vector)
    for linea in vector:
        pasajero = linea.split(",")
        print(f"\nDNI: {pasajero[0]}")
        print(f"Apellido: {pasajero[2]}")
        print(f"Nombre: {pasajero[1]}")
        print(f"Nro. de vuelo: {pasajero[3]}")
        print("--------------------------------------------------")
    file.close()

def listar_pasajeros_vuelo():
    nro = input("Ingrese el número de vuelo del cual quiere ver pasajeros: ")
    vector = pasajeros_vuelo(nro)
    ordenar(vector)
    for linea in vector:
        pasajero = linea.split(",")
        print(f"\nDNI: {pasajero[0]}")
        print(f"Apellido: {pasajero[2]}")
        print(f"Nombre: {pasajero[1]}")
        print(f"Nro. de vuelo: {pasajero[3]}")
        print("--------------------------------------------------")

def listar_vuelos_destino():
    destino = input("Ingrese de que destino quiere ver los vuelos: ")
    vector = vuelos_destino(destino)
    ordenar(vector)
    for linea in vector:
        vuelo = linea.split(",")
        print(f"\nNro. de vuelo: {vuelo[0]}")
        print(f"Lugar de partida: {vuelo[1]}")
        print(f"Destino: {vuelo[2]}")
        print(f"Aerolínea: {vuelo[3]}")
        print(f"Cantidad máxima de pasajeros: {vuelo[4]}")
        print(f"Cantidad de pasajeros actual: {vuelo[5]}")
        print("--------------------------------------------------")
"""
FUNCIONES MENÚ
"""
def gestion_vuelos():
    salir = False
    while not salir:
        print("\nGESTIÓN VUELOS\n\n")
        opcion = input("Ingrese qué quiere hacer:\n'1': Crear un vuelo\n'2': Modificar datos de un vuelo\n'3': Eliminar un vuelo\nIngrese otro para salir: ")
        if opcion == "1":
            crear_vuelo()
        elif opcion == "2":
            modificar_vuelo()
        elif opcion == "3":
            eliminar_vuelo()
        else:
            salir = True

def gestion_pasajeros():
    salir = False
    while not salir:
        print("\nGESTIÓN PASAJEROS\n\n")
        opcion = input("Ingrese qué quiere hacer:\n'1': Agregar un pasajero\n'2': Modificar datos de un pasajero\n'3': Eliminar un pasajero\nIngrese otro para salir: ")
        if opcion == "1":
            agregar_pasajero()
        elif opcion == "2":
            modificar_pasajero()
        elif opcion == "3":
            eliminar_pasajero()
        else:
            salir = True

def consultas():
    salir = False
    while not salir:
        print("\nCONSULTAS\n\n")
        opcion = input("Ingrese que quiere ver:\n'1': Listar todos los vuelos\n'2': Listar todos los vuelos de una aerolínea\n'3': Listar todos los pasajeros\n'4': Listar todos los pasajeros de un vuelo\n'5': Listar todos los vuelos de un destino\nIngrese otro para salir: ")
        if opcion == "1":
            listar_vuelos()
        elif opcion == "2":
            listar_vuelos_aerolinea()
        elif opcion == "3":
            listar_pasajeros()
        elif opcion == "4":
            listar_pasajeros_vuelo()
        elif opcion == "5":
            listar_vuelos_destino()
        else:
            salir = True