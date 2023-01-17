# script 1
arch = open('archivo.txt')
contenido = arch.read()
print (contenido)

# script 2
arch = open('archivo.txt')
contenido = arch.readlines()
print (contenido)

# script 3
contenido = ''
arch = open('archivo.txt')
while True:
	line = arch.readline()
	contenido += line
	if line == '':
		break
print(contenido)

# Para todos los casos:
arch.close()