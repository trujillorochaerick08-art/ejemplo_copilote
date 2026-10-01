from soluciones.salario_semanal import calcularSalario, mostrarSalario

def main():
    horas=float(input("Ingrese las horas trabajadas: "))
    pago=float(input("Ingrese el pago por hora: "))
    salario = calcularSalario(horas, pago)
    mostrarSalario(salario)

if __name__ == "__main__":
    main()