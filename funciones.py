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
            num = input("Introduzca el precio de la obra: ")
            if num.replace(" ", "").isnumeric() and 1<=float(num):
                num = float(num)
                return num
            else:
                print('Ingrese una opcion valida.')
        except:
            print("Se ha identificado un error")
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


def ordenar_lista_nombre(lista):
    for step in range(1, len(lista)):
        key = lista[step].nombre
        j = step - 1
        
        while j >= 0 and key < lista[j].nombre:
            lista[j + 1].nombre = lista[j].nombre
            j = j - 1
              
        lista[j + 1].nombre = key
        
def ordenar_lista_cota(lista):
    for step in range(1, len(lista)):
        key = lista[step].cota
        j = step - 1
        
        while j >= 0 and key < lista[j].cota:
            lista[j + 1].cota = lista[j].cota
            j = j - 1
               
        lista[j + 1].cota = key
        
def busqueda_cota(lista_ordenada, lista_pinturas):
    try:
        ordenar_lista_cota(lista_ordenada)
        cota=pedir_cota()
        pos=busqueda.busqueda_binaria_cota(lista_ordenada,cota)
        if(pos==None):
            print("No se ha encontrado ninguna pintura con esa cota")
        elif(pos!=None):
            if(lista_pinturas[pos].eliminado==True):
                print("La pintura que estas buscando ha sido eliminada")
            else:
                print("Se ha encontrado la siguiente pintura")
                lista_pinturas[pos].mostrar_pintura()
    except:
        print("Se ha detectado un error ")

        
def busqueda_nombre(lista_ordenada, lista_pinturas):
    try:
        ordenar_lista_cota(lista_ordenada)
        nombre=pedir_nombre()
        pos=busqueda.busqueda_binaria_nombre(lista_ordenada,nombre)
        if(pos==None):
            print("No se ha encontrado ninguna pintura con ese nombre")
        elif(pos!=None):
            if(lista_pinturas[pos].eliminado==True):
                print("La pintura que estas buscando ha sido eliminada")
            else:
                print("Se ha encontrado la siguiente pintura")
                lista_pinturas[pos].mostrar_pintura()
    except:
        print("Se ha detectado un error ")
        



