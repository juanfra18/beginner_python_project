El trabajo final consiste en generar 2 archivos en los que se guardaran los datos de vuelos (número de vuelo, lugar de partida, destino, aerolínea, 
cantidad máxima de pasajeros y cantidad de pasajeros en el vuelo) y en el otro archivo los datos de los pasajeros (dni, nombre, apellido, vuelo). 
El programa deberá poseer un menú que tenga las siguientes opciones: gestión vuelos, gestión pasajeros, consultas y salir.

Cuando se entra al menú gestión vuelos se debería poder realizar las siguientes operaciones:
1. Crear un vuelo
2. Modificar datos de un vuelo (todos menos el número de vuelo y la cantidad de pasajeros en el vuelo).
3. Eliminar un vuelo (en caso de que un vuelo posea algún pasajero asignado, se deberán borrar los pasajeros asignados o no se deberá permitir que el vuelo sea borrado
   debido a esto, esto queda a decisión del alumno, es decir no deben existir pasajeros asignados a un vuelo que ya no existe).

Cuando se entra al menú gestión pasajeros se debería poder realizar las siguientes operaciones:
1. Agregar un pasajero y asignarle un vuelo (se podrá hacer esta asignación siempre y cuando el vuelo exista y no haya alcanzado su límite de capacidad. 
   No se podrá asignar un mismo pasajero a un mismo vuelo más de una vez, es decir, no se debe repetir un mismo dni por vuelo).
2. Modificar datos de un pasajero (en caso de modificar el vuelo al que el pasajero está asignado se deberá restar un pasajero en el vuelo a modificar y agregar un 
   pasajero en el nuevo vuelo).
3. Eliminar pasajero (Se deberá reducir el numero de pasajeros del vuelo al que estaba asignado este pasajero)

CONSULTAS:
1. Listar todos los vuelos
2. Listar todos los vuelos de una aerolínea
3. Listar todos los pasajeros
4. Listar todos los pasajeros de un vuelo
5. Listar vuelos por destino.
