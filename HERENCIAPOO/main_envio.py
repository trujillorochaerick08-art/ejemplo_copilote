from clases.paqueteria import Envio,EnvioExpress,EnvioSobre


def main():
    envio = Envio("Yamel",10)
    sobre = EnvioSobre("Benito")
    express = EnvioExpress("Aranza",20)

    print(envio.resumen())
    print(sobre.resumen())
    print(express.resumen())

if __name__ == "__main__":
    main()