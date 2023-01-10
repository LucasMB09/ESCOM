posicion = 0

def q0(cad,posicion):
    if cad[posicion] == '1':
        if (len(cad)-1) == posicion:
            print("Cadena no valida")
        else:
            posicion = posicion + 1
            q1(cad,posicion)
    elif cad[posicion] == '0':
        if (len(cad)-1) == posicion:
            print("Cadena no valida")
        else:
            posicion = posicion + 1
            q2(cad,posicion)
    else:
        print("Cadena no valida")

def q1(cad,posicion):
    if cad[posicion] == '1':
        print("Cadena valida")
    elif cad[posicion] == '0':
        if (len(cad)-1) == posicion:
            print("Cadena no valida")
        else:
            posicion = posicion + 1
            q2(cad,posicion)
    else:
        print("Cadena no valida")

def q2(cad,posicion):
    if cad[posicion] == '1':
        if (len(cad)-1) == posicion:
            print("Cadena no valida")
        else:
            posicion = posicion + 1
            q1(cad,posicion)
    elif cad[posicion] == '0':
        print("Cadena valida")
    else:
        print("Cadena no valida")

cad = input("Introduce una cadena: ")
q0(cad,posicion)