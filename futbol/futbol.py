'''
La FIFA está analizando las estadísticas del mundial, por lo que se almacenó en un archivo
de nombre juegos.dat para cada uno de los Partidos, la siguiente información
Fecha del partido, Equipo1, Equipo2, Goles del equipo1, Goles del equipo2
Desarrolle un programa en VB2008, que lea la información y genere dos archivos de
nombre ganadores.dat y perdedores.dat que deben contener a los equipos ganadores,
los perdedores respectivamente. La información a escribir en ambos archivos es: Nombre
del equipo y número de goles anotados. Adicionalmente imprima por pantalla, la
siguiente información:
1. Porcentaje de partidos que quedaron empatados
2. Equipos participantes en el partido donde hubo la mayor cantidad de goles
anotados
Consideraciones
 La fecha del partido se encuentra almacenada como dd/mm/aaaa
 Equipo1 y Equipo2 son los nombres de los equipos
 Si el partido quedó empatado no hay ni ganador, ni perdedor, por lo que no se escribe en ningún archivo
 Todas las salidas por pantalla, deben tener los mensajes apropiados
'''

Module Module1
    'Ejercicio: Evaluando los resultados del Futbol
    'Solución: Br. Carrillo Luis
    'Fecha: 22/06/2012

    Sub Main()

        'Entrada
        Dim fecha As String
        Dim equipo1, equipo2 As String
        Dim golesEquipo1, golesEquipo2 As Integer

        'Salida 
        Dim porcentajeEmpatados As Single
        Dim equipo1Mayor, equipo2Mayor As String 'Equipos participantes en partido con más goles

        'Variables Auxiliares
        Dim diferenciaDeGoles As Integer
        Dim sumaDeGoles As Integer
        Dim partidosEmpatados As Integer
        Dim numeroDeEquipos As Integer
        Dim bandera As Boolean
        Dim mayorCantidaDeGoles As Integer

        'Inicialización
        bandera = True
		partidosEmpatados = 0
        numeroDeEquipos = 0

        'Apertura de archivos
        FileOpen(1, "juegos.txt", OpenMode.Input)
        FileOpen(2, "ganadores.txt", OpenMode.Output)
        FileOpen(3, "perdedores.txt", OpenMode.Output)

        'Ciclo de control para lectura de registros de la lista

        While Not EOF(1)

            Input(1, fecha)
            Input(1, equipo1)
            Input(1, equipo2)
            Input(1, golesEquipo1)
            Input(1, golesEquipo2)


            diferenciaDeGoles = golesEquipo1 - golesEquipo2

            'Validación de resultado del partido para impresión en el archivo correspondiente

            If diferenciaDeGoles = 0 Then
                'Contador del número de partidos empatados
                partidosEmpatados = partidosEmpatados + 1
            ElseIf diferenciaDeGoles < 0 Then
                PrintLine(2, equipo2, golesEquipo2)
                PrintLine(3, equipo1, golesEquipo1)
            ElseIf diferenciaDeGoles > 0 Then
                PrintLine(2, equipo1, golesEquipo1)
                PrintLine(3, equipo2, golesEquipo2)
            End If


            'Detección del partido con mas goles

            sumaDeGoles = golesEquipo1 + golesEquipo2

            If bandera Then
                equipo1Mayor = equipo1
                equipo2Mayor = equipo2
                mayorCantidaDeGoles = sumaDeGoles
                bandera = False
            ElseIf sumaDeGoles > mayorCantidaDeGoles Then
                equipo1Mayor = equipo1
                equipo2Mayor = equipo2
                mayorCantidaDeGoles = sumaDeGoles
            End If

            'Contador del número de equipos en la lista
            numeroDeEquipos = numeroDeEquipos + 1

        End While

        porcentajeEmpatados = partidosEmpatados / numeroDeEquipos

        Console.WriteLine("Porcentaje de equipos que quedaron empatados: " & FormatPercent(porcentajeEmpatados))

        Console.WriteLine("Equipos participantes en partido con más goles: " & equipo1Mayor & " y " & equipo2Mayor)

        FileClose()

        Console.ReadKey()

    End Sub

End Module

