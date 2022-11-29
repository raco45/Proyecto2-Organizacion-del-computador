import funciones
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
print(texto)                                         
lista = []
lista_cotas=[]
lista_nombres=[]
def main():
        print('''\nBienvenid@ al Louvre (Hola Andres)\n''')
        while True:
                menu = funciones.val_menu('''\nIndique que quiere realizar a continuacion:
                \n1. Insertar pintura dentro de la base de datos.
                \n2. Consultar base de datos.
                \n3. Editar status de una pintura.
                \n4. Eliminar una pintura.
                \n5. Compactador.
                \n6. Exit
                \n ==>  ''', 7)
                if menu == 1:
                        funciones.insertar_pintura(lista,lista_cotas,lista_nombres)
                        print("Una nueva pintura ha sido agregada a la base de datos ")
                        continue
                if menu == 2:
                        while True:
                                tipo = funciones.val_menu('''\nQue tipo de consulta desea realizar:
                                \n1. Por cota.
                                \n2. Por nombre.
                                \n ==> ''', 3)
                                if tipo == 1:
                                        
                                        funciones.busqueda_cota(lista_cotas, lista)
                                        otra = funciones.val_menu('''\nDesea realizar otra busqueda:
                                        \n1. Si
                                        \n2. No.
                                        \n ==>  ''', 3)
                                        if otra == 1:
                                                continue
                                        else:
                                                break
                                      
                                if tipo == 2:
                                        funciones.busqueda_nombre(lista_nombres, lista)
                                        otra = funciones.val_menu('''\nDesea realizar otra busqueda:
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
                                tipo = funciones.val_menu('''\nQue tipo de consulta desea realizar:
                                \n1. Por cota.
                                \n2. Por nombre.
                                \n ==> ''', 3)
                                if tipo == 1:
                                        funciones.cambio_estado(tipo,lista,lista_cotas,lista_nombres)
                                        otra = funciones.val_menu('''\nDesea realizar otra busqueda:
                                        \n1. Si
                                        \n2. No.
                                        \n ==>  ''', 3)
                                        if otra == 1:
                                                continue
                                        else:
                                                break
                                if tipo == 2:
                                        funciones.cambio_estado(tipo,lista,lista_cotas,lista_nombres)
                                        otra = funciones.val_menu('''\nDesea realizar otra busqueda:
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
                                tipo = funciones.val_menu('''\nQue tipo de consulta desea realizar:
                                \n1. Por cota.
                                \n2. Por nombre.
                                \n ==> ''', 3)
                                if tipo == 1:
                                        funciones.eliminacion_logica(tipo,lista, lista_cotas, lista_nombres)
                                        otra = funciones.val_menu('''\nDesea realizar otra busqueda:
                                        \n1. Si
                                        \n2. No.
                                        \n ==>  ''', 3)
                                        if otra == 1:
                                                continue
                                        else:
                                                break
                                if tipo == 2:
                                        funciones.eliminacion_logica(tipo,lista, lista_cotas, lista_nombres)
                                        otra = funciones.val_menu('''\nDesea realizar otra busqueda:
                                        \n1. Si
                                        \n2. No.
                                        \n ==>  ''', 3)
                                        if otra == 1:
                                                continue
                                        else:
                                                break
                        continue 
                if menu == 5:
                        for x in lista:
                                print(x.cota)
                        funciones.compactador(lista,lista_cotas,lista_nombres)
                        print("Las pinturas eliminadas han sido removidas de la lista")
                        for x in lista:
                                print(x.cota)
                        continue

                if menu == 6:
                        print('\nBye bye <3\n')
                        break   


main()