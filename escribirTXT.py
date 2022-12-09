'''
with open("./Ficheros/n.txt", "w", encoding='utf-8') as file_object:
    file_object.write("holis 1óñfg")   

r, w, a, x (create)
t-> text mode
b -> bytes para archivos de fotos
'''

### APARTADO 1 ####
'''
fichero = open("./Ficheros/pruebaTexto.txt", "rt", encoding='utf-8')
# Lectura de línea a línea 
# Cada llamada devolverá una nueva línea hasta llegar al final
#Leer primera línea
# primera_linea = fichero.readline()
# seg_linea = fichero.readline()
# print(primera_linea,seg_linea)

todas_lineas = fichero.readlines()
print(todas_lineas)
'''
#### APARTADO 2 ####
# escribir en un fichero existente
'''
fichero = open("./Ficheros/n.txt", "w", encoding='utf-8')
fichero.write("Aquí vamos a escribir \n") # esto es independiente de writeLines, no se sobreescribe

lista_contenido = [
    'Coodenadas: ', 
    'x',
    'y',
    'z',
    'adiós'
]


lista_contenido = map(lambda line: line + '\n', lista_contenido)
print(lista_contenido)

fichero.writelines(lista_contenido)
fichero.close()
'''

#### APARTADO 3 ####
# AGREGAR CONTENIDO A UN FICHERO EXISTENTE
# fichero = open("./Ficheros/n.txt", "a", encoding='utf-8')
# fichero.write('\n\n\n Esto es una nueva línea')
# fichero.close()

#### APARTADO 4 ####
# Crear un nuevo fichero, escribir en el fichero después de crearlo.
# no se puede leer
"""try:
    fichero = open("./Ficheros/apartado4(1).txt", "x", encoding='utf-8')
    fichero.write("Escribir")
    print(fichero.readable())
    print(fichero.writable())
    fichero.close()
except FileExistsError:
    print("Fichero repetido")"""

#### APARTADO 5 ####
"""fichero = open("./Ficheros/n.txt", encoding='utf-8')
fichero.seek(10) # iniciar a leer a partir del 10mo caracter
print("Leer desde el décimo caracter: \n",fichero.read())
fichero.close()"""

#### APARTADO 6 ####
# Lectura y escritpra simulltáneamente.
fichero = open("./Ficheros/n.txt", 'r+', encoding='utf-8')
lineas = fichero.readlines()
print(lineas)

fichero.write('\nÉsta es nueva')
fichero.close()