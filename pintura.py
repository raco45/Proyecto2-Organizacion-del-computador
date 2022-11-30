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
      print("Cota de la obra :{} ".format(self.cota))
      print("Nombre de la obra:{} ".format(self.nombre))
      print("Precio de la obra :{} ".format(self.precio))
      print("Status de la obra:{} ".format(self.status))
    else:
      print(f'\nLa pinrtura {self.nombre} ha sido eliminada.')



#Elimina logicamente la pintura
def eliminar(self):
  self.eliminado=True

def en_mantenimiento(self):
  self.status="EN MANTENIMIENTO"
  
def en_exhibicon(self):
  self.status="EN EXHIBICIÓN"

"""def anadir_pintura(lista):
  cota = funciones.pedir_cota()
  nombre = funciones.val_nombres("\nIngrese el nombre de la pintura: ", lista)
  precio = funciones.val_int('\nIngrese el precio de la pintura: ')
  status = funciones.val_menu('''\nIngrese el estatus de la pintura:
    \n1. En exhibicion.
    \n2. En mantenimiento.
    \n---->   ''', 3)
"""
  

