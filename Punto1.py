'''1.Construir un programa que permita ingresar 20 números enteros y
cuente cuantos números negativos fueron ingresados (+1)'''

numerosenteros=[]
numerosnega=[]
## definir variable centinela
contador=0
contadornega=0
while(contador<5):
    
    numero=(int(input("ingrese por favor un numero: ")))
    numerosenteros.append(numero)
    contador=contador+1
    if(numero<0):
        contadornega=contadornega+1
        numerosnega.append(numero)

print("los numeros que ingreso fueron",numerosenteros)
print("los numeros impares fueron",numerosnega)
print("el total de numeros negativos fueron",contadornega)
      ##  numerosimpares.append()