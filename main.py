from funciones import *
import indexes
import busqueda

texto="""  _______   __                                                    __        __                                                         
|       \ |  \                                                  |  \      |  \                                                        
| $$$$$$$\ \$$  ______   _______  __     __   ______   _______   \$$  ____| $$  ______    _______                                     
| $$__/ $$|  \ /      \ |       \|  \   /  \ /      \ |       \ |  \ /      $$ /      \  /       \                                    
| $$    $$| $$|  $$$$$$\| $$$$$$$\\$$\ /  $$|  $$$$$$\| $$$$$$$\| $$|  $$$$$$$|  $$$$$$\|  $$$$$$$                                    
| $$$$$$$\| $$| $$    $$| $$  | $$ \$$\  $$ | $$    $$| $$  | $$| $$| $$  | $$| $$  | $$ \$$    \                                     
| $$__/ $$| $$| $$$$$$$$| $$  | $$  \$$ $$  | $$$$$$$$| $$  | $$| $$| $$__| $$| $$__/ $$ _\$$$$$$\                                    
| $$    $$| $$ \$$     \| $$  | $$   \$$$    \$$     \| $$  | $$| $$ \$$    $$ \$$    $$|       $$                                    
 \$$$$$$$  \$$  \$$$$$$$ \$$   \$$    \$      \$$$$$$$ \$$   \$$ \$$  \$$$$$$$  \$$$$$$  \$$$$$$$                                     
                                                                                                                                      
                                                                                                                                      
                                                                                                                                      
                                                                                                                             __       
                                                                                                                            |  \      
                                                                                                                    ______  | $$      
                                                                                                                   |      \ | $$      
                                                                                                                    \$$$$$$\| $$      
                                                                                                                   /      $$| $$      
                                                                                                                  |  $$$$$$$| $$      
                                                                                                                   \$$    $$| $$      
                                                                                                                    \$$$$$$$ \$$      
                                                                                                                                      
                                                                                                                                      
                                                                                                                                      
 __        __                          __                                                                                             
|  \      |  \                        |  \                                                                                            
| $$____   \$$ ______ ____    ______  | $$  ______   __    __   ______                                                                
| $$    \ |  \|      \    \  |      \ | $$ |      \ |  \  |  \ |      \                                                               
| $$$$$$$\| $$| $$$$$$\$$$$\  \$$$$$$\| $$  \$$$$$$\| $$  | $$  \$$$$$$\                                                              
| $$  | $$| $$| $$ | $$ | $$ /      $$| $$ /      $$| $$  | $$ /      $$                                                              
| $$  | $$| $$| $$ | $$ | $$|  $$$$$$$| $$|  $$$$$$$| $$__/ $$|  $$$$$$$                                                              
| $$  | $$| $$| $$ | $$ | $$ \$$    $$| $$ \$$    $$ \$$    $$ \$$    $$                                                              
 \$$   \$$ \$$ \$$  \$$  \$$  \$$$$$$$ \$$  \$$$$$$$ _\$$$$$$$  \$$$$$$$                                                              
                                                    |  \__| $$                                                                        
                                                     \$$    $$                                                                        
                                                      \$$$$$$          """
                                                
lista = []
def main():
        print('''\nBienvenid@ al Louvre (Hola Andres)\n''')
        while True:
                menu = val_menu('''\nIndique que quiere realizar a continuacion:
                \n1. Insertar pintura dentro de la base de datos.
                \n2. Consultar base de datos.
                \n3. Editar status de una pintura.
                \n4. Eliminar una pintura.
                \n5. Exit
                \n ==>  ''', 6)
                if menu == 1:
                        print("insertar pintura")
                        continue
                if menu == 2:
                        while True:
                                tipo = val_menu('''\nQue tipo de consulta desea realizar:
                                \n1. Por cota.
                                \n2. Por nombre.
                                \n ==> ''', 3)
                                if tipo == 1:
                                        #cota = pedir_cota(lista)
                                        print('hacer busqueda por cota')
                                        otra = val_menu('''\nDesea realizar otra busqueda:
                                        \n1. Si
                                        \n2. No.
                                        \n ==>  ''', 3)
                                        if otra == 1:
                                                continue
                                        else:
                                                break
                                      
                                if tipo == 2:
                                        #nombre = pedir_nombre(lista)
                                        print('hacer busqueda por nombre')
                                        otra = val_menu('''\nDesea realizar otra busqueda:
                                        \n1. Si
                                        \n2. No.
                                        \n ==>  ''', 3)
                                        if otra == 1:
                                                continue
                                        else:
                                                break
                        continue
                if menu == 3:
                        while True:
                                tipo = val_menu('''\nQue tipo de consulta desea realizar:
                                \n1. Por cota.
                                \n2. Por nombre.
                                \n ==> ''', 3)
                                if tipo == 1:
                                        #cota = pedir_cota(lista)
                                        #pintura = busqueda_binaria(cota)
                                        print('hacer busqueda por cota, retornar pintura, hacer cambio de status')
                                        otra = val_menu('''\nDesea realizar otra busqueda:
                                        \n1. Si
                                        \n2. No.
                                        \n ==>  ''', 3)
                                        if otra == 1:
                                                continue
                                        else:
                                                break
                                if tipo == 2:
                                        #nombre = pedir_nombre(lista)
                                        #pintura = busqueda_binaria(nombre)
                                        print('hacer busqueda por nombre, retornar pintura, hacer cambio de status')
                                        otra = val_menu('''\nDesea realizar otra busqueda:
                                        \n1. Si
                                        \n2. No.
                                        \n ==>  ''', 3)
                                        if otra == 1:
                                                continue
                                        else:
                                                break
                        continue  
                if menu == 4:
                        while True:
                                tipo = val_menu('''\nQue tipo de consulta desea realizar:
                                \n1. Por cota.
                                \n2. Por nombre.
                                \n ==> ''', 3)
                                if tipo == 1:
                                        #cota = pedir_cota(lista)
                                        #pintura = busqueda_binaria(cota)
                                        print('hacer busqueda por cota, retornar pintura, set eliminado a true')
                                        otra = val_menu('''\nDesea realizar otra busqueda:
                                        \n1. Si
                                        \n2. No.
                                        \n ==>  ''', 3)
                                        if otra == 1:
                                                continue
                                        else:
                                                break
                                if tipo == 2:
                                        #nombre = pedir_nombre(lista)
                                        #pintura = busqueda_binaria(nombre)
                                        print('hacer busqueda por nombre, retornar pintura, set elliminado a true')
                                        otra = val_menu('''\nDesea realizar otra busqueda:
                                        \n1. Si
                                        \n2. No.
                                        \n ==>  ''', 3)
                                        if otra == 1:
                                                continue
                                        else:
                                                break
                        continue 
                if menu == 5:
                        print('\nBye bye <3\n')
                        break   


main()