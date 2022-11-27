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
    
                   

