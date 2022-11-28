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


def busqueda_binaria( lista_ordenada, objeto_pintura ):

   lower_bound = 0
   upper_bound = len(lista_ordenada) - 1

   while True:
       if upper_bound < lower_bound:
           objeto_no_encontrado = "Pintura No Encontrada"
           return objeto_no_encontrado

       (midpoint) = lower_bound + (upper_bound - lower_bound) // 2

       if lista_ordenada[midpoint].cota == objeto_pintura:
           return lista_ordenada[midpoint].posicion

       else:
          
           if lista_ordenada[midpoint].cota < objeto_pintura:
               lower_bound = midpoint + 1
          
           else:
               upper_bound = midpoint - 1
 
busqueda_binaria(mi_lista, objeto_pintura)


mi_lista = [{'cota': 1, 'posicion': 'A1'}, {'cota': 2, 'posicion': 'A2'},
          {'cota': 3, 'posicion': 'A3'}, {'cota': 4, 'posicion': 'A4'},
          {'cota': 5, 'posicion': 'A5'}, {'cota': 6, 'posicion': 'A6'},
          {'cota': 7, 'posicion': 'A7'}, {'cota': 8, 'posicion': 'A8'},
          {'cota': 9, 'posicion': 'A9'}, {'cota': 10, 'posicion': 'A10'}]

objeto_pintura = 5

busqueda_binaria(mi_lista, objeto_pintura)


mi_lista = [{'Nombre': 'Alfa', 'posicion': 'A1'}, {'Nombre': 'Bravo', 'posicion': 'A2'},
          {'Nombre': 'Charlie', 'posicion': 'A3'}, {'Nombre': 'Delta', 'posicion': 'A4'},
          {'Nombre': 'Echo', 'posicion': 'A5'}, {'Nombre': 'Foxtrot', 'posicion': 'A6'},
          {'Nombre': 'Golf', 'posicion': 'A7'}, {'Nombre': 'Hotel', 'posicion': 'A8'},
          {'Nombre': 'India', 'posicion': 'A9'}, {'Nombre': 'Juliett', 'posicion': 'A10'}]

objeto_pintura = 'Golf'

busqueda_binaria(mi_lista, objeto_pintura)


mi_lista = [{'cota': 1, 'posicion': 'A1'}, {'cota': 2, 'posicion': 'A2'},
          {'cota': 3, 'posicion': 'A3'}, {'cota': 4, 'posicion': 'A4'},
          {'cota': 5, 'posicion': 'A5'}, {'cota': 6, 'posicion': 'A6'},
          {'cota': 7, 'posicion': 'A7'}, {'cota': 8, 'posicion': 'A8'},
          {'cota': 9, 'posicion': 'A9'}, {'cota': 10, 'posicion': 'A10'}]

objeto_pintura = 11

busqueda_binaria(mi_lista, objeto_pintura)


mi_lista = [{'Nombre': 'Alfa', 'posicion': 'A1'}, {'Nombre': 'Bravo', 'posicion': 'A2'},
          {'Nombre': 'Charlie', 'posicion': 'A3'}, {'Nombre': 'Delta', 'posicion': 'A4'},
          {'Nombre': 'Echo', 'posicion': 'A5'}, {'Nombre': 'Foxtrot', 'posicion': 'A6'},
          {'Nombre': 'Golf', 'posicion': 'A7'}, {'Nombre': 'Hotel', 'posicion': 'A8'},
          {'Nombre': 'India', 'posicion': 'A9'}, {'Nombre': 'Juliett', 'posicion': 'A10'}]

objeto_pintura = 'Kilo'

busqueda_binaria(mi_lista, objeto_pintura)


mi_lista = [{'cota': 1, 'Nombre': 'Alfa', 'posicion': 'A1'},
          {'cota': 2, 'Nombre': 'Bravo', 'posicion': 'A2'},
          {'cota': 3, 'Nombre': 'Charlie', 'posicion': 'A3'},
          {'cota': 4, 'Nombre': 'Delta', 'posicion': 'A4'},
          {'cota': 5, 'Nombre': 'Echo', 'posicion': 'A5'},
          {'cota': 6, 'Nombre': 'Foxtrot', 'posicion': 'A6'},
          {'cota': 7, 'Nombre': 'Golf', 'posicion': 'A7'},
          {'cota': 8, 'Nombre': 'Hotel', 'posicion': 'A8'},
          {'cota': 9, 'Nombre': 'India', 'posicion': 'A9'},
          {'cota': 10, 'Nombre': 'Juliett', 'posicion': 'A10'}]

objeto_pintura = 'Golf'

busqueda_binaria(mi_lista, objeto_pintura)


mi_lista = [{'cota': 1, 'Nombre': 'Alfa', 'posicion': 'A1'},
          {'cota': 2, 'Nombre': 'Bravo', 'posicion': 'A2'},
          {'cota': 3, 'Nombre': 'Charlie', 'posicion': 'A3'},
          {'cota': 4, 'Nombre': 'Delta', 'posicion': 'A4'},
          {'cota': 5, 'Nombre': 'Echo', 'posicion': 'A5'},
          {'cota': 6, 'Nombre': 'Foxtrot', 'posicion': 'A6'},
          {'cota': 7, 'Nombre': 'Golf', 'posicion': 'A7'},
          {'cota': 8, 'Nombre': 'Hotel', 'posicion': 'A8'},
          {'cota': 9, 'Nombre': 'India', 'posicion': 'A9'},
          {'cota': 10, 'Nombre': 'Juliett', 'posicion': 'A10'}]

objeto_pintura = 7

busqueda_binaria(mi_lista, objeto_pintura)

print(busqueda_binaria(mi_lista,objeto_pintura))