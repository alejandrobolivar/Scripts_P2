archivo = open("archivo.txt")
i = 1
for linea in archivo:
    linea = linea.rstrip("\n")
    print(" %4d: %s" % (i, linea))
    i+=1
archivo.close()
