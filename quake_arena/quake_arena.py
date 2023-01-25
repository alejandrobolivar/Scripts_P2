Hola profe! Tengo una  duda. Cuando tengo una lista de lista (lista interna y lista externa) como se en que posición debo colocar las condiciones. Le paso un ejercicio que estoy haciendo y tengo problemas con eso..
# Quake 3 Arena es un juego en red en donde grupos de jugadores se enfrentan entre sí para completar una única misión: exterminar a todos los jugadores de los grupos enemigos.Un día se conformaron grupos de jugadores para realizar un torneo de Quake 3 Arena y al final de la jornada se registra en el archivo torneo.dat la siguiente información de los grupos participantes:
# Nombre del grupo y cantidad de integrantes
#Y por cada integrante del grupo:
#Nombre del jugador, Edad, Cantidad de enemigos que exterminó
#Diseñe un programa en Python, de nombre SuApellido_SuCedula (coloque su apellido y su cedula), que lea el archivo de datos torneo.txt e imprima en el archivo de datos resultados.txt, escribiendo en cada línea el nombre del grupo, la cantidad de integrantes del grupo y la cantidad total de enemigos exterminados por el grupo.
#Además, imprima por pantalla o consola:
#1. Porcentaje de jugadores menores de 23 años por cada grupo.
#2. Nombre del grupo con mayor cantidad enemigos exterminados.
#3. Nombre del jugador que extermino a la menor cantidad de enemigos de toda la lista.
#4. Edad Promedio, por cada grupo, de los jugadores que eliminaron a más de 5 enemigos
#Variales auxiliares.


cont_23=0
acum_elim=0
mayor_elim= 0
band1=0
menor_elim=0
band2=0
edad_5 =0
cont_5 =0
arch1=open('torneo.txt')
registro=arch1.readlines()
linea=0

while linea<len(registro):
    lista_ext= registro[linea].split(',')
    linea += 1
    equipo= lista_ext[0]
    m= int(lista_ext[1])
    print(equipo)

    for _ in range (m):
        lista_int= registro[linea].split(',')
        linea += 1
        nombre = lista_int[0]
        edad= int(lista_int[1])
        eliminados= int(lista_int[2])
        print(nombre, edad, eliminados)


    if edad < 23: #p1
        cont_23 += 1
        grupo_23 = equipo #DUDA: AL PROCESARLO ME IMPRIME DE NUEVO EL
NOMBRE DEL PRIMER EQUIPO

    if band2==0: #p3
        menor_elim= eliminados
        nombre_menor= nombre
        band2=1
    elif eliminados < menor_elim:
        nombre_menor= nombre
        menor_elim= eliminados




        acum_elim += eliminados
    if band1==0: #p2
        mayor_elim= acum_elim
        equipo_elim= equipo
        band1=1
    elif acum_elim > mayor_elim:
        mayor_elim= acum_elim
        equipo_elim= equipo

    if eliminados > 5: #p4 #duda: me repite el nombre del primer
equipo y saca mal la cuenta :(
        edad_5 += edad
        equipo_5= equipo
        cont_5 += 1



    print("porcentaje de jugadores menores a 23 es: ", (cont_23/m)*100
," % por el grupo de: ", grupo_23)
    print("el promedio de edad en jugadores con mas de 5 eliminados es
", edad_5/cont_5 ,"para el equipo de ", equipo_5)

print("el equipo con mayor cantidad de enemigos eliminados es: ", equipo_elim)
print("el jugador con menor eliminados es: ", nombre_menor)

arch1.close()