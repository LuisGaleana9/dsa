#Cola
#First IN First OUT

cola = []
i = 0

while 1 == 1:
    print("1.- enqueue")

    opcion = int(input("Ingresa una opcion: "))

    match opcion:
        case 1:
            cola.append(i)
            print("Ingresaste el valor " + i + " a la cola.")
            i += 1

        case 2:
            cola.remove(0)
        case _:
            print("Selecciona una opcion valida.")

