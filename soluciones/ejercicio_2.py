'''
planteamiento del problema

calcular la n 
'''
#problema: calcular n, con los valores n
# entradas: n
# salida: n

#algoritmo
# 1. Leer n
# 2. Calcular n
# 3. Mostrar n

#contrato de funciones  
#leerDatos()
#Entrada: ninguna   
#Salida: n
#Responsabilidad: pedir los datos al usuario

#calcularN(n)
#Entrada: n
#Salida: n
#Responsabilidad: calcular,no imprimir math.sqrt(2 * math.pi) * math.e ** -n * n ** (n+1/2)

#casos de prueba
#caso 1: n=5
#Entrada: 5
#Salida: 118.0191679575901
#caso2: n=10
#Entrada: 10
#Salida: 362.0657618774149
#caso3: n=15
#Entrada: 15
#Salida: 1170.604056735924

#restricciones:
# - no imprimir dentro de la función calcularSalario
# - devolver el rresultado
# - no usar bibliotecas externas
# - no usar variables globales
# - no realices llamadas a funciones dentro de este archivo

def leerDatos():
    n = float(input("Ingrese el valor de n: "))
    return n
def calcularN(n):
    import math
    n = math.sqrt(2 * math.pi) * math.e ** -n * n ** (n+1/2)
    return n
def mostrarN(n):
    print(f"El valor de n es: {n}")