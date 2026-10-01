'''
PLANTEAMENTO DEL PROBLEMA

Calcula el salario semanal de 
un trabajador. Las horas 
mayores a 40 se pagan al 
triple
'''

# PROBLEMA: calcular salario semanal
# ENTRADAS: horas_trabajadas, pago_por_hora
# SALIDA: salario_semanal
# ALGORITMO
# 1. Leer horas trabajadas
# 2. Leer pago por hora
# 3. Si horas <= 40:
#       salario = horas * pago
# 4. Si no:
#       extra = horas - 40
#       salario = (40 * pago) + (extra * pago * 2)
# 5. Mostrar salario

#contrato de funciones
#leerDatos()
#Entrada: ninguna
#Salida: horas y pago
#Responsabilidad: pedir 

#calcularSalario(horas, pago)
#Entrada: horas y pago
#Salida: salario
#Responsabilidad: 
#calcular, no imprimir

#mostrarsalario(salario)
#entrada: salario
#Salida: ninguna
#Responsabilidad: 
#mostrar resultado

#casos de prueba
#Caso 1: horas = 40, pago = 10
#Entrada: 40, 10
#Salida: 400
#Caso 2: horas = 45, pago = 10
#Entrada: 45, 10
#Salida: 550
#Caso 3: horas = 50, pago = 12
#Entrada: 50, 12
#Salida: 840

#restricciones:
# - no imprimir dentro de la función calcularSalario
# - devolver el rresultado
# - no usar bibliotecas externas
# - no usar variables globales
# - no realices llamadas a funciones dentro de este archivo



def leerDatos():
    horas = float(input("Ingrese las horas trabajadas: "))
    pago = float(input("Ingrese el pago por hora: "))
    return horas, pago

def calcularSalario(horas, pago):
    if horas <= 40:
        salario = horas * pago
    else:
        extra = horas - 40
        salario = (40 * pago) + (extra * pago * 3)
    return salario
    
def mostrarSalario(salario):
    print(f"El salario semanal es: {salario}")
