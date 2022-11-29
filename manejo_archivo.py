#se imprimen los datos del la lista en un archivo de texto
def imprimir_datos(lista):
    archivo = open("datos.txt", "w")
    for i in range(len(lista)):
        archivo.write(str(lista[i]) + " ")
    archivo.close()

# Path: manejo_archivo.py
#se lee el archivo de texto y se almacenan los datos en una lista
def leer_datos():
    archivo = open("datos.txt", "r")
    lista = []
    for linea in archivo:
        lista.append(linea)
    archivo.close()
    return lista

