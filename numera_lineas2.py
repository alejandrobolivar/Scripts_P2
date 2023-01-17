arch = open("archivo.txt")
for i, linea in enumerate(arch):
    linea = linea.rstrip("\n")
    print (" %4d: %s" % (i, linea))
arch.close()