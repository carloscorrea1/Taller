'''
3.Construir un programa para ir de compras en un supermercado
que permita la construcción del siguiente MENU:

1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.8)
2. Digitar 2 para mostrar todos los productos registrados (+0.8)
3. Digitar 0 para SALIR

Finalmente, versione y comparta el repositorio según las indicaciones
dadas+(1.4)

'''

centinela=0
print("****MENU SUPERMERCADO****")
print("Digite 1.PARA INDICAR CODIGO, NOMBRE, PRECIO DE PRODUCTO")
print("Digite 2.PARA MOSTRAR PRODUCTOS REGISTRADOS")
print("Digite 3.PARA SALIR")
productos=[]

while(centinela!=3):
    centinela=(int(input("ingrese su opcion por favor: ")))
    producto={}
    if(centinela==1):
        producto['codigo']=input("ingrese el codigo del producto: ")
        producto['nombre']=input("ingrese el nombre del producto: ")
        producto['precio']=input("ingrese el precio del producto: ")
        productos.append(producto)
        
    elif(centinela==2):
        
       print(productos)
       
    elif(centinela==3):
        
        print("Muchas gracias vuelva prontp")  
    
        break
   
    else: print("digite una opcion")    
    