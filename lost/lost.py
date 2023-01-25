'''

Después de 6 temporadas esta emblemática serie LOST llega a su finaI, lo cual se ha convertido en todo un acontecimiento mundial, por esta razón, la cadena ABC creó un concurso para que los fanáticos ganen premios, entre ellos viajar a USA para conocer a los personajes. Dicho concurso consiste en enviar mensajes al número LOST, y dependiendo de la cantidad de mensajes enviados se entregan los premios. Para determinar los ganadores, se tiene en el archivo fanaticos.txt la siguiente información:
País de procedencia y número de participantes
y para cada participante:
Nombre del participante, edad, cantidad de mensajes enviados
Ante esta situación, la ABC, lo llama a usted, que es un excelente estudiante de la materia de computación 1 de la facultad de ingeniería de la UC para que desarrolle una aplicación de consola de VB2008 que determine e imprima por pantalla:

1.	Nombre, edad y país de procedencia del participante que va a viajar a USA para conocer al elenco de LOST.
2.	Nombre del primer participante de 23 años que envió más de 10 mensajes.
3.	Promedio de mensajes enviados por los participantes de cada país.
4.	País que cuenta con la menor cantidad de participantes.
Consideraciones:
• El participante que viajara a USA es el que envió la mayor cantidad de mensajes.


'''

Module Module1
    'Elaborado Por: Valmore Dominguez
    'Preparaduría Computacion I. Parcial 2, período 1-2012
    Sub Main()
        'LOST
        'Lista de listas    Interna: conocida    Externa: desconocida


        'Variables de entrada
        Dim pais As String 'Pais de Procedencia
        Dim participantes As Integer 'Cantidad de participantes por pais
        Dim nombre_participante As String 'Nombre de cada participante
        Dim edad As Integer 'Edad de cada participante
        Dim cantidad_mensajes As Integer 'Mensajes enviados por cada participante

        'Variables de Salida
        Dim nombre_ganador As String 'Nombre del participante que envió la mayor cantidad de mensajes
        Dim edad_ganador As Integer 'edad del participante que envióa mas mensajes
        Dim pais_ganador As String 'Pais de procedencia del participante que envió mas mensajes
        Dim nombre_primero As String 'Nombre del primer participante de 23 años que envió más de 10 mensajes
        Dim promedio_mensajes_por_pais As Single 'Promedio de mensajes enviados por cada pais
        Dim pais_menor_cantidad As String 'Pais con la menor cantidad de participantes


        'Variables de Proceso
        Dim bandera_ganador As Integer 'Variable para el calculo del participante ganador
        Dim mayor_cantidad_mensajes As Integer 'Variable para comparar y calcular el ganador del concurso
        Dim bandera_primero As Boolean 'Variable para el cálculo del primer participante de 23 en enviar mas de 10 mensajes
        Dim acumulador_mensajes_por_pais As Integer 'Variable para cálculo del promedio de mensajes por cada pais
        Dim bandera_pais As Integer 'Variable para el cálculo del pais con menor cantidad de participantes
        Dim menor_cantidad_participantes As Integer 'Variable para comparar y calcular el pais con menor cantidad de participantes


        'Apertura de archivo
        FileOpen(1, "fanaticos.txt", OpenMode.Input)

        'Inicializacion de Herramientas referentes a todos los paises
        bandera_pais = 0
        bandera_ganador = 0
        bandera_primero = True


        While Not EOF(1)
            'Lectura referente a cada pais
            Input(1, pais)
            Input(1, participantes)

            'Cálculo del pais con menor cantidad de participantes
            If bandera_pais = 0 Then

                pais_menor_cantidad = pais
                menor_cantidad_participantes = participantes
                bandera_pais = 1

            ElseIf participantes < menor_cantidad_participantes Then

                pais_menor_cantidad = pais
                menor_cantidad_participantes = participantes
            End If

            'Inicializacion de Herramientas para el cálculo del promedio de mensajes por pais
            acumulador_mensajes_por_pais = 0

            'Ciclo referente a la lista interna (Participantes)
            For i = 1 To participantes
                'Lectura de datos de los participantes
                Input(1, nombre_participante)
                Input(1, edad)
                Input(1, cantidad_mensajes)

                'Acumulador para Cálculo del promedio de mensajes por cada pais
                acumulador_mensajes_por_pais = acumulador_mensajes_por_pais + cantidad_mensajes

                'Cálculo del ganador del concurso
                If bandera_ganador = 0 Then

                    'Captura del primer participante
                    nombre_ganador = nombre_participante
                    edad_ganador = edad
                    pais_ganador = pais
                    mayor_cantidad_mensajes = cantidad_mensajes
                    bandera_ganador = 1

                ElseIf cantidad_mensajes > mayor_cantidad_mensajes Then

                    'Comparacion para el cálculo del ganador
                    nombre_ganador = nombre_participante
                    edad_ganador = edad
                    mayor_cantidad_mensajes = cantidad_mensajes
                    pais_ganador = pais

                End If

                'Cálculo del primer participante de 23 años en enviar mas de 10 mensajes
                If bandera_primero And edad = 23 And cantidad_mensajes > 10 Then

                    nombre_primero = nombre_participante
                    bandera_primero = False

                End If



            Next

            'Cálculo del promedio de mensajes enviados por cada pais
            If participantes > 0 Then
                promedio_mensajes_por_pais = acumulador_mensajes_por_pais / participantes
                Console.WriteLine("Promedio de mensajes enviados de {0}  =  {1}", pais, promedio_mensajes_por_pais)
            End If


        End While

        'Impresion de Resultados para todos los paises
        Console.WriteLine("Ganador del concurso LOST")
        Console.WriteLine("Nombre: {0}  Edad: {1}   Pais de Procedencia: {2}", nombre_ganador, edad_ganador, pais_ganador)


        If bandera_primero = False Then
            'Hubo una persona de 23 años que envió mas de 10 mensajes
            Console.WriteLine("Nombre del participante de 23 años en enviar mas de 10 mensajes: " & nombre_primero)
        Else

            Console.WriteLine("No hubo personas de 23 años con mas de 10 mensajes")

        End If

        Console.WriteLine("Pais con menor cantidad de mensajes: " & pais_menor_cantidad)

        Console.WriteLine("_______________________________")
        Console.WriteLine("Pulse una tecla para finalizar")
        Console.ReadKey()


        'Cierre de archivos
        FileClose(1)

    End Sub

End Module
