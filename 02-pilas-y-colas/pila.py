#Pila
#Last IN First OUT

pila = []
i = 0

while 1==1 :
    print("1.- Push")
    print("2.- Pop")
    print("3.- Peek")
    print("4.- Is_Emply")
    print("5.- All_cola")
    print("9.- Salir")
    opcion = int(input("Ingresa una opcion: "))

    match opcion:
        case 1:
            pila.append(i)
            print("Haz agregado " + str(i) + " a la pila.")
            i += 1

        case 2:
            if i != 0:
                pila.remove(i-1)
                print("Haz eliminado " + str(i-1) + " de la pila")
                i -= 1
            else: 
                print("La pila esta vacia.")

        case 3:
            if i != 0:
                print(pila[i-1])
            else: 
                print("La pila esta vacia.")

        case 4:
            if i != 0:
                print("Not Emply")
            else:
                print("Emply")

        case 5:
            for i in pila:
                print("[" + str(i) + "]", end="")
            print("<--")

        case 9:
            print("Saliendo...")
            break

        case _:
            print("Selecciona una opcion valida.")
