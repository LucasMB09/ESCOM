def valida():
    print("Cadena aceptada")

def noValida():
    print("Cadena no aceptada")

def q0(cad,posicion):
    if cad[posicion] == '+' or cad[posicion] == '-':
        if len(cad)-1 == posicion:
            noValida()
        else:
            q1(cad,posicion+1)
    elif cad[posicion].isdigit():
        if len(cad)-1 == posicion:
            valida()
        else:
            q2(cad,posicion+1)
    else:
        noValida()

def q1(cad,posicion):
    if cad[posicion].isdigit():
        if len(cad)-1 == posicion:
            valida()
        else:
            q2(cad,posicion+1)
    else:
        noValida()

def q2(cad,posicion):
    if cad[posicion].isdigit():
        if len(cad)-1 == posicion:
            valida()
        else:
            q2(cad,posicion+1)
    elif cad[posicion] == '.':
        if len(cad)-1 == posicion:
            noValida()
        else:
            q3(cad,posicion+1)
    elif cad[posicion] == 'E' or cad[posicion] == 'e':
        if len(cad)-1 == posicion:
            noValida()
        else:
            q5(cad,posicion+1)
    else:
        noValida()

def q3(cad,posicion):
    if cad[posicion].isdigit:
        if len(cad)-1 == posicion:
            valida()
        else:
            q4(cad,posicion+1)
    else:
        noValida()

def q4(cad,posicion):
    if cad[posicion].isdigit:
        if len(cad)-1 == posicion:
            valida()
        else:
            q4(cad,posicion+1)
    elif cad[posicion] == 'E' or cad[posicion] == 'e':
        if len(cad)-1 == posicion:
            noValida()
        else:
            q5(cad,posicion+1)
    else:
        noValida()

def q5(cad,posicion):
    if cad[posicion] == '+' or cad[posicion] == '-':
        if len(cad)-1 == posicion:
            noValida()
        else:
            q6(cad,posicion+1)
    elif cad[posicion].isdigit():
        if len(cad)-1 == posicion:
            valida()
        else:
            q7(cad,posicion+1)
    else:
        noValida()

def q6(cad,posicion):
    if cad[posicion].isdigit():
        if len(cad)-1 == posicion:
            valida()
        else:
            q7(cad,posicion+1)
    else:
        noValida()

def q7(cad,posicion):
    if cad[posicion].isdigit():
        if len(cad)-1 == posicion:
            valida()
        else:
            q7(cad,posicion+1)
    else:
        noValida()

cad = input("Introduce una cadena: ")
q0(cad,0)