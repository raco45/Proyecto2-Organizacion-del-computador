import funciones

class Pintura:
  def __init__(self, cota, nombre, precio):
    self.cota = cota
    self.nombre = nombre
    self.precio = precio
    self.status = None
    self.eliminado = False

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

#Elimina logicamente la pintura
def eliminar(self):
  self.eliminado=True

def en_mantenimiento(self):
  self.status="EN MANTENIMIENTO"
  
def en_exhibicon(self):
  self.status="EN EXHIBICIÓN"



  

