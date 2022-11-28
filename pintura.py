import funciones

class Pintura:
  def __init__(self, cota, nombre, precio, status, eliminado):
    self.cota = cota
    self.nombre = nombre
    self.precio = precio
    self.status = status
    self.eliminado = eliminado

    def mostrar_pintura(self):
        if self.eliminado == False:
             print('''\nCota:{self.cota}
            \nNombre de la pintura: {self.nombre}
            \nPrecio: {self.precio}
            \nStatus: {self.status}}''')
        else:
            print('\nLa pinrtura {self.nombre} ha sido eliminada.')

def mostrar_todas_pinturas(lista):
  for i in lista:
        if lista[i].eliminado == False:
             print('''\nCota:{lista[i].cota}
            \nNombre de la pintura: {lista[i].nombre}
            \nPrecio: {lista[i].precio}
            \nStatus: {lista[i].status}}''')
        else:
            print('\nLa pinrtura {lista[i].nombre} ha sido eliminada.')

def anadir_pintura(lista):
  cota = funciones.pedir_cota()
  nombre = funciones.val_nombres("\nIngrese el nombre de la pintura: ", lista)
  precio = funciones.val_int('\nIngrese el precio de la pintura: ')
  status = funciones.val_menu('''\nIngrese el estatus de la pintura:
    \n1. En exhibicion.
    \n2. En mantenimiento.
    \n---->   ''', 3)

