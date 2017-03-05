import string
file = input('Path or file_name: ')
leyendo_archivo = open(file,"r+")
leido = leyendo_archivo.read().translate(str.maketrans('','', string.whitespace))

leyendo_archivo.close()
print (leido)