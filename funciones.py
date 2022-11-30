import busqueda
import pintura 
import indexes
#validaciones 

#pedir cota

def pedir_cota():
    while(True):
        try:
            cota= input("Ingresa una cota -->  ").strip()
            if(len(cota) != 8):
                print("Tiene que ingresar 8 caracteres, 4 letras y 4 numeros")
                continue
            else:
                i=0
                palabra=""
                num=""
                for x in cota:
                    if(i<=3):
                        palabra+=x
                    elif(i>3):
                        num+=x
                    i+=1
                if (palabra.isalpha()==False):
                    print("Por favor ingresar 4 letras al inicio")
                    continue
                else:
                    if(num.isnumeric()==False):
                        print("Por favor ingresar 4 numeros al final")
                        continue
                    else:
                            return cota.upper() 
                        
        except :
            print("Se ha identificado un error")
            continue 

def validar_cota(lista):
    while True:
        try:
            cota=pedir_cota()
            auxi=busqueda.busqueda_binaria_cota(lista,cota.upper())
            if(auxi== None):
                return cota
            elif(auxi!=None):
                print("Esa cota ya existe")
                continue
        except:
            print("Se ha encontrado un error")
            continue

def pedir_nombre():
    while True:
        try:
            string = input("Ingrese el nombre de la pintura: ")
            if (string.replace(" ", "").isalpha() and len(string.replace(" ",""))<=30 and len(string.replace(" ",""))>0):
                string = string.capitalize()
                
                return string 
                
            else:
                print('Ingrese una opcion valida')
        except:
            print("Se ha identificado un error")
            continue
                
                
                     

def validar_nombre(lista):
    while True:
        try:
            string=pedir_nombre()
            auxi=busqueda.busqueda_binaria_nombre(lista,string)
            if(auxi== None):
                return string 
            elif(auxi!=None):
                print("Ya existe una pintura con ese nombre ")
                continue
        except:
            print("Se ha identificado un error")
            continue


def pedir_precio():
    while True:
        try:
            num = float(input("Introduzca el precio de la obra: "))
            if 1<=num:
                num = num
                return num
            else:
                print('Ingrese una opcion valida.')
        except:
            print("Se ha identificado un error, ingrese un numero valido")
            continue




def set_status(pintura):
    while True:
        try:
            num = input('''\nIngrese el estatus de la pintura:
        \n1. En exhibicion.
        \n2. En mantenimiento.
        \n---->   ''')
            if num.replace(" ", "").isnumeric():
                num = int(num)
                if(num==1):
                    pintura.status="EN EXHIBICIÓN"
                    break
                elif(num==2):
                    pintura.status="EN MANTENIMIENTO"
                    break
                else:
                    print("Ingrese una opcion valida")
            else:
                print('Ingrese una opcion valida.')
        except:
            print("Se ha identificado un error")
            continue

def val_menu(msg1, n):
    while True:
        num = input(msg1)
        if num.replace(" ", "").isnumeric() and 1<=int(num)<n:
            num = int(num)
            return num
            
        else:
            print('Ingrese una opcion valida.')

def insertar_pintura(lista, cotas_ordenada, nombre_ordenado):
    while True:
        try:
            cota= validar_cota(lista)
            nombre= validar_nombre(lista)
            precio=pedir_precio()
            pintu= pintura.Pintura(cota,nombre,precio)
            set_status(pintu)
            lista.append(pintu)
            objeto_cota= indexes.Cota_Indexada(cota,lista.index(pintu))
            objeto_nombre= indexes.Nombre_index(nombre,lista.index(pintu))
            cotas_ordenada.append(objeto_cota)
            nombre_ordenado.append(objeto_nombre)
            break
        except:
            print("Se ha identificado un error")
            continue



        
def busqueda_cota(lista_ordenada, lista_pinturas):
    try:
        lista_ordenada=sorted(lista_ordenada, key=lambda x: x.cota)
        cota=pedir_cota()
        pos=busqueda.busqueda_binaria_cota(lista_ordenada,cota)
        if(pos==None):
            print("No se ha encontrado ninguna pintura con esa cota")
            return None
        elif(pos!=None):
            if(lista_pinturas[pos].eliminado==True):
                print("La pintura que estas buscando ha sido eliminada")
                return None
            else:
                print("Se ha encontrado la siguiente pintura")
                lista_pinturas[pos].mostrar_pintura()
                return lista_pinturas[pos]
    except:
        print("Se ha detectado un error ")

        
def busqueda_nombre(lista_ordenada, lista_pinturas):
    try:
        lista_ordenada=sorted(lista_ordenada, key=lambda x: x.nombre)
        nombre=pedir_nombre()
        pos=busqueda.busqueda_binaria_nombre(lista_ordenada,nombre)
        if(pos==None):
            print("No se ha encontrado ninguna pintura con ese nombre")
            return None
        elif(pos!=None):
            if(lista_pinturas[pos].eliminado==True):
                print("La pintura que estas buscando ha sido eliminada")
                return None
            else:
                print("Se ha encontrado la siguiente pintura")
                lista_pinturas[pos].mostrar_pintura()
                return lista_pinturas[pos]
    except:
        print("Se ha detectado un error ")
        


def cambio_estado(n, lista_pinturas, lista_cotas, lista_nombres):
    if(n==1):
        pintu=busqueda_cota(lista_cotas, lista_pinturas)
        if(pintu!= None):
            set_status(pintu)
    elif(n==2):
        pintu=busqueda_nombre(lista_nombres, lista_pinturas)
        if(pintu!= None):
            set_status(pintu)  
    pintu.mostrar_pintura()

def eliminacion_logica(n, lista_pinturas, lista_cotas, lista_nombres):
    if(n==1):
        pintu=busqueda_cota(lista_cotas, lista_pinturas)
        if(pintu!= None):
            pintu.eliminado=True
            print("La pintura ha sido eliminada ")
    elif(n==2):
        pintu=busqueda_nombre(lista_nombres, lista_pinturas)
        if(pintu!= None):
            pintu.eliminado=True  
            print("La pintura ha sido eliminada ") 

def compactador(lista_pinturas, lista_cota, lista_nombre):
    lista_cota.clear()
    lista_nombre.clear()
    for x in lista_pinturas:
        if (x.eliminado==True):
            lista_pinturas.remove(x)
        else: 
            objeto_cota= indexes.Cota_Indexada(x.cota,lista_pinturas.index(x))
            objeto_nombre= indexes.Nombre_index(x.nombre,lista_pinturas.index(x))
            lista_cota.append(objeto_cota)
            lista_nombre.append(objeto_nombre)

def llena_listas(lista_pinturas, lista_cota, lista_nombre):
    for x in lista_pinturas:
        objeto_cota= indexes.Cota_Indexada(x.cota,lista_pinturas.index(x))
        objeto_nombre= indexes.Nombre_index(x.nombre,lista_pinturas.index(x))
        lista_cota.append(objeto_cota)
        lista_nombre.append(objeto_nombre)
        

def mostrar_todas_pinturas(lista):
  for i in lista:
    
    print(f'''\nCota:{i.cota}
\nNombre de la pintura: {i.nombre}
\nPrecio: {i.precio}
\nStatus: {i.status}
\nEliminado:{i.eliminado} ''')

def mostrar_orden(lista):
    lista=sorted(lista, key=lambda x: x.nombre)
    #ordenar_lista_nombre(lista)
    for x in lista:
        print(x.nombre, x.posicion)