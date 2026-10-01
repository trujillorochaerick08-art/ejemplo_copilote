'''
planteamiento del problema

calcular la x. Los valores de a, b y c deberán ser introducidos desde el teclado
'''

# problema: calcular la x. Los valores de a, b y c deberán ser introducidos desde el teclado
# entradas: a, b, c
# salida: x
#algoritmo
# 1. Leer a, b y c
# 2. Calcular x = ((b-a**2)**1/2)/c
# 3. Mostrar x
#contrato de funciones
#leerDatos()
#Entrada: ninguna
#Salida: a, b, c
#Responsabilidad: pedir los datos al usuario
#calcularX(a, b, c)
#Entrada: a, b, c
#Salida: x
#Responsabilidad: calcular, no imprimir,x=((b-a**2)**1/2)/c
#casos de prueba
#caso 1: a=2, b=20, c=5
#Entrada: 2, 20, 5
#Salida: 0.8
#caso2: a=3, b=30, c=6
#Entrada: 3, 30, 6
#Salida: 1.0
#caso3: a=4, b=40, c=7
#Entrada: 4, 40, 7
#Salida: 1.2    

#restricciones:
# - no imprimir dentro de la función calcularSalario
# - devolver el rresultado
# - no usar bibliotecas externas
# - no usar variables globales
# - no realices llamadas a funciones dentro de este archivo


def leerDatos():
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    return a, b, c

def calcularX(a, b, c):
    x = ((b - a**2)**(1/2)) / c
    return x
def mostrarX(x):
    print(f"El valor de x es: {x}")