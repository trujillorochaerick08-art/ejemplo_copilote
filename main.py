from soluciones.salario_semanal import calcularSalario, mostrarSalario
from soluciones.ejercicio_1 import leerDatos, calcularX, mostrarX
from soluciones.ejercicio_2 import leerDatos as leerDatosN, calcularN, mostrarN
def main():
   while True:
       print("menu de opciones:")
       print("1. Calcular salario semanal")
       print("2. Calcular x")
       print("3. Calcular n")
       print("4. Salir")
       opcion = input("Seleccione una opción: ")
       if opcion == "1":
           horas = float(input("Ingrese las horas trabajadas: "))
           pago = float(input("Ingrese el pago por hora: "))
           salario = calcularSalario(horas, pago)
           mostrarSalario(salario)
       elif opcion == "2":
              a, b, c = leerDatos()
              x = calcularX(a, b, c)
              mostrarX(x)
       elif opcion == "3":
                n = leerDatosN()
                resultado_n = calcularN(n)
                mostrarN(resultado_n)
         elif opcion == "4":
             print("Saliendo del programa...")
                break
             
       else:
           print("Opción no válida")

if __name__ == "__main__":
    main()