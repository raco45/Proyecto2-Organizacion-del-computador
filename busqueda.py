# make a binary searh function for lists of objects that have as parameters: Dimension and posicion, Nombre and posicion.  
# the funtion parameters are: the list, the object to search and the posicion of the object in the list.

#def busqueda_binaria(lista, objeto, cota):
#    low = 0
#    high = len(list) - 1
#    while low <= high:
#        mid = (low + high) // 2
#        guess = list[mid]
#        if guess[cota] == object:
#            return mid
#        if guess[cota] < object:
#            low = mid + 1
#        else:
#            high = mid - 1
#    return None


def busqueda_binaria_cota( lista_ordenada, parametro_busqueda ):

   lower_bound = 0
   upper_bound = len(lista_ordenada) - 1

   while True:
       if upper_bound < lower_bound:
           objeto_no_encontrado = None
           return objeto_no_encontrado

       (midpoint) = lower_bound + (upper_bound - lower_bound) // 2

       if lista_ordenada[midpoint].cota == parametro_busqueda:
           return lista_ordenada[midpoint].posicion

       else:
          
           if lista_ordenada[midpoint].cota < parametro_busqueda:
               lower_bound = midpoint + 1
          
           else:
               upper_bound = midpoint - 1
 
def busqueda_binaria_nombre( lista_ordenada, parametro_busqueda ):

   lower_bound = 0
   upper_bound = len(lista_ordenada) - 1

   while True:
       if upper_bound < lower_bound:
           objeto_no_encontrado = None
           return objeto_no_encontrado

       (midpoint) = lower_bound + (upper_bound - lower_bound) // 2

       if lista_ordenada[midpoint].nombre == parametro_busqueda:
           return lista_ordenada[midpoint].posicion

       else:
          
           if lista_ordenada[midpoint].nombre < parametro_busqueda:
               lower_bound = midpoint + 1
          
           else:
               upper_bound = midpoint - 1