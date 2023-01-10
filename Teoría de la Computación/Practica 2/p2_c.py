#COMPLETA

posicion = 0

def valido():
    print("Cadena valida")
def noValido():
    print("Cadena no valida")

def q0(cad,posicion):
    if (len(cad)-1) == posicion:
            print("Cadena no valida")
    else:
        if cad[posicion] == 'a':
            q1(cad,posicion+1)
        elif cad[posicion] == 'b':
            q2(cad,posicion+1)
        elif cad[posicion] == 'c':
            q3(cad,posicion+1)
        elif cad[posicion] == 'd':
            q4(cad,posicion+1)
        else:
            noValido()

def q1(cad,posicion):
    if cad[posicion] == 'a':
        if len(cad)-1 == posicion:
            valido()
        else:
            q5(cad,posicion+1)
    else:
        if (len(cad)-1) == posicion:
            print("Cadena no valida")
        elif cad[posicion] == 'b':
            q2(cad,posicion+1)
        elif cad[posicion] == 'c':
             q3(cad,posicion+1)
        elif cad[posicion] == 'd':
              q4(cad,posicion+1)
        else:
             noValido()

def q2(cad,posicion):
    if cad[posicion] == 'b':
        if len(cad)-1 == posicion:
            valido()
        else:
            q5(cad,posicion+1)
    else:
        if (len(cad)-1) == posicion:
            print("Cadena no valida")
        elif cad[posicion] == 'a':
            q1(cad,posicion+1)
        elif cad[posicion] == 'c':
            q3(cad,posicion+1)
        elif cad[posicion] == 'd':
            q4(cad,posicion+1)
        else:
             noValido()

def q3(cad,posicion):
    if cad[posicion] == 'c':
        if len(cad)-1 == posicion:
            valido()
        else:
            q5(cad,posicion+1)
    else:
        if (len(cad)-1) == posicion:
            print("Cadena no valida")
        elif cad[posicion] == 'a':
            q1(cad,posicion+1)
        elif cad[posicion] == 'b':
            q2(cad,posicion+1)
        elif cad[posicion] == 'd':
            q4(cad,posicion+1)
        else:
             noValido()

def q4(cad,posicion):
    if cad[posicion] == 'd':
        if len(cad)-1 == posicion:
            valido()
        else:
            q5(cad,posicion+1)
    else:
        if (len(cad)-1) == posicion:
            print("Cadena no valida")
        elif cad[posicion] == 'a':
            q1(cad,posicion+1)
        elif cad[posicion] == 'b':
            q2(cad,posicion+1)
        elif cad[posicion] == 'c':
            q3(cad,posicion+1)
        else:
             noValido()

def q5(cad,posicion):
    if cad[posicion] == 'a' or cad[posicion] == 'b' or cad[posicion] == 'c' or cad[posicion] == 'd':
        if len(cad)-1 == posicion:
            valido()
        else:
            q5(cad,posicion+1)
    else:
        noValido()

def q6(cad,posicion):
    if cad[posicion] == 'a' or cad[posicion] == 'b' or cad[posicion] == 'c' or cad[posicion] == 'd':
        if len(cad)-1 == posicion:
            valido()
        else:
            q5(cad,posicion+1)
    else:
        noValido()

def q7(cad,posicion):
    if cad[posicion] == 'a' or cad[posicion] == 'b' or cad[posicion] == 'c' or cad[posicion] == 'd':
        if len(cad)-1 == posicion:
            valido()
        else:
            q5(cad,posicion+1)
    else:
        noValido()
    
def q8(cad,posicion):
    if cad[posicion] == 'a' or cad[posicion] == 'b' or cad[posicion] == 'c' or cad[posicion] == 'd':
        if len(cad)-1 == posicion:
            valido()
        else:
            q5(cad,posicion+1)
    else:
        noValido()

cad = input("Introduce una cadena: ")
q0(cad,posicion)