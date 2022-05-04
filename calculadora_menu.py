#Calculadora con menú

from math import log

#input
bandera = False
x = float(input("Dame el valor del número x: "))
y = float(input("Dame el valor del número y: "))

print("Dame la opción que deseas realizar: \n")
#Se despliega el menú para seleccionar la opción que deseas realizar
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Potencia")
print("6. Logaritmo")
opcion = int(input("Dame la opción: "))

#Processing
if opcion == 1:
    z = x + y
    print(x, " + ", y)
elif opcion == 2:
    z = x - y
    print(x, " - ", y)
elif opcion == 3:
    z = x * y
    print(x, " X ", y)
elif opcion == 4 and y != 0:
    z = x / y
    print(x, " / ", y)
elif opcion == 4 and y == 0:
    print("El denominador es igual a 0")
    print("NO se puede realizar la división")
    bandera = True
elif opcion == 5:
    pow= (x,y)
    print(x, " ^ ", y)
elif opcion == 6 and x > 0:
    z = log(x) 
    print("logaritmo de ", x)
elif opcion == 6 and x <= 0:
    print("El valor de x es <= a 0 y ")
    print("No se puede calcular el logaritmo")
    bandera = True
else:
    print("Opción no válida")

#Se escribe el resultado con otra condición
if opcion < 7 and bandera == False:
    print("Resultado = " , z)