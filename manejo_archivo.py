import pintura

def imprimir_datos(lista):
    archivo = open("datos.txt", "w")
    for i in range(len(lista)):
        archivo.write("{},{},{},{},{}\n".format(lista[i].cota,lista[i].nombre,lista[i].precio,lista[i].status,lista[i].eliminado ))
    archivo.close()


def leer_datos():
    archivo = open("datos.txt", "r")
    lista = []
    for linea in archivo:
        x=linea.split(",")
        aux= pintura.Pintura(x[0],x[1],x[2])
        aux.status=x[3]
        if(x[4].replace(" ","")=="False"):
            aux.eliminado=False
        elif(x[4].replace(" ","")=="True"):
            aux.eliminado=True
            
        lista.append(aux)
    archivo.close()
    return lista

