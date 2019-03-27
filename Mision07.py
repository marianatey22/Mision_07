#Autor: Mariana Teyssier cervantes
#Misión 07 CICLOS WHILE



def dividir():
    dividendo = int(input("Teclea el dividendo: "))
    divisor = int(input("Teclea el divisor: "))
    cociente = 0
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente = cociente + 1

    print("El cociente es:", cociente)
    print("El residuo es:", dividendo)


def encontrarMayor():
    n = int(input("Teclea un número(-1 para salir): "))
    mayor = n

    while n != -1:
        n= int(input("Teclea un número (-1 para salir): "))
        if n > mayor:
            mayor=n
    if mayor == -1:
        print("No hay valor")
    else:
        print("El mayor es", mayor)



def main():
    print("Misión 07. Ciclos While\n"
          "Autor: Mariana Teyssier Cervantes\n"
          "Matrícula: A01745234\n"
          "1. Calcular divisiones \n"
          "2. Encontrar el mayor \n"
          "3. Salir\n")
    opcion = int(input("Teclea tu opción: "))

    while opcion != 0:
        if opcion<=0 or opcion>=4:
            print("Error. Teclea 1, 2 o 3")
        elif opcion == 1:
            dividir()
        elif opcion == 2:
            encontrarMayor()

        opcion = int(input("Teclea tu opción: "))

        if opcion == 3:
            print("Gracias por usar este programa. Vuelve pronto")
            quit()

main()








