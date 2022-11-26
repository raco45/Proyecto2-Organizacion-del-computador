class Pintura:
  def __init__(self, cota, nombre, precio, status, eliminado):
    self.cota = cota
    self.nombre = nombre
    self.precio = precio
    self.status = status
    self.eliminado = eliminado

    def mostrar_pintura(self):
        if self.eliminado == True:
             print('''\nCota:{self.cota}
            \nNombre de la pintura: {self.nombre}
            \nPrecio: {self.precio}
            \nStatus: {self.status}}''')
        else:
            print('\nLa pinrtura {self.nombre} ha sido eliminada.')
