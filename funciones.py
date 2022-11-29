import busqueda
import pintura 
#validaciones 

#pedir cota

def pedir_cota(lista):
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
                        auxi=busqueda.busqueda_binaria_cota(lista,cota.upper())
                        if(auxi== None):
                            return cota.upper() 
                        elif(auxi!=None):
                            print("Esa cota ya existe")
                            continue
        except :
            print("Se ha identificado un error")
            continue 

def pedir_nombre(lista):
    while True:
        try:
            string = input("Ingrese el nombre de la pintura: ")
            if (string.replace(" ", "").isalpha() and len(string.replace(" ",""))<=30 and len(string.replace(" ",""))>0):
                string = string.capitalize()
                auxi=busqueda.busqueda_binaria_nombre(lista,string)
                if(auxi== None):
                    return string 
                elif(auxi!=None):
                    print("Ya existe una pintura con ese nombre ")
                    continue
                     
            else:
                print('Ingrese una opcion valida')
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
        num = input('''\nIngrese el estatus de la pintura:
    \n1. En exhibicion.
    \n2. En mantenimiento.
    \n---->   ''')
        if num.replace(" ", "").isnumeric() and 1<=int(num)<3:
            num = int(num)
            if(num==1):
                pintura.en_exhibicon()
            else:
                pintura.en_mantenimiento()
        else:
            print('Ingrese una opcion valida.')

def val_nombres(msg1, lista): #añadele lo de que si se repite el nombre
    while True:
        string = input(msg1)
        if string.replace(" ", "").replace('&', '').isalpha():
            string = string.title()
            return string
            break
        else:
            print('Ingrese una opcion valida')

def val_menu(msg1, n):
    while True:
        num = input(msg1)
        if num.replace(" ", "").isnumeric() and 1<=int(num)<n:
            num = int(num)
            return num
            break
        else:
            print('Ingrese una opcion valida.')