from clases.empleados import Empleado,EmpleadoPorHora,Vendedor

def main():
    empleado = Empleado ("Yamel",2500)
    vendedor = Vendedor("benito",2500,1000)
    empleadoPorHora = EmpleadoPorHora("aranza",20,100)

    print(empleado.descripcion())
    print(vendedor.descripcion())
    print(empleadoPorHora.descripcion())

if __name__ == "__main__":
        main()