import funciones
import indexes

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
                                                

"""pintura_cota1= indexes.Cota_Indexada("ABCD1234",1)
pintura_cota2= indexes.Cota_Indexada("DCBA1234",1)
pintura_cota3= indexes.Cota_Indexada("FGAE1234",1)
pintura_cota4= indexes.Cota_Indexada("GHAS1234",1)
pintura_cota5= indexes.Cota_Indexada("ADDF1234",1)
pintura_cota6= indexes.Cota_Indexada("ADFF1234",1)
pintura_cota7= indexes.Cota_Indexada("GADE1234",1)
pintura_cota8= indexes.Cota_Indexada("GHSQ1234",1)
pintura_cota9= indexes.Cota_Indexada("RTFW1234",1)
lista=[]
lista.append(pintura_cota1)
lista.append(pintura_cota2)
lista.append(pintura_cota3)
lista.append(pintura_cota4)
lista.append(pintura_cota5)
lista.append(pintura_cota6)
lista.append(pintura_cota7)
lista.append(pintura_cota8)
lista.append(pintura_cota9)
funciones.ordenar_lista_cota(lista)
for x in lista:
        print(x.cota)"""

lista=[]
cotas=[]
nombres=[]

funciones.insertar_pintura(lista,cotas,nombres)

print(lista[0].cota)
