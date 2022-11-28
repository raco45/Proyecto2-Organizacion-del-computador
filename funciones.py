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

def val_str(msg1):
    while True:
        string = input(msg1)
        if string.replace(" ", "").isalpha():
            string = string.capitalize()
            return string
            break
        else:
            print('Ingrese una opcion valida')
                   
def val_int(msg1):
    while True:
        num = input(msg1)
        if num.replace(" ", "").isnumeric() and 1<=int(num):
            num = int(num)
            return num
            break
        else:
            print('Ingrese una opcion valida.')

def val_menu(msg1, n):
    while True:
        num = input(msg1)
        if num.replace(" ", "").isnumeric() and 1<=int(num)<n:
            num = int(num)
            return num
            break
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
