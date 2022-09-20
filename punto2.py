'''2.Leer información de 10 frutas {nombre, color, precio} para preparar
un salpicón; el programa debe permitir mostrar las 10 frutas ingresadas
al mismo tiempo+(1)
'''

frutalista=[]
contador=0
while(contador<2):
    frutas={}
    frutas['nombre'] =input("ingrese el nombre de la fruta: ")
    frutas['color'] =input("ingrese el color de la fruta: ")
    frutas['precio'] =(float(input("ingrese el precio de la fruta: ")))
    frutalista.append(frutas)
    contador=contador+1
     
print(frutalista)
    
   