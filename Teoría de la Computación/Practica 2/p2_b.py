#COMPLETO

def valida():
    print("Cadena aceptada")

def noValida():
    print("Cadena no aceptada")

def q0(cad,posicion):
    if len(cad) == 0:
        valida()
    elif cad[posicion] == '0':
        if len(cad)-1 == posicion:
            noValida()
        else:
            q1(cad,posicion+1)
    elif cad[posicion] == '1':
        if len(cad)-1 == posicion:
            valida()
        else:
            q3(cad,posicion+1)
    else:
        noValida()

def q1(cad,posicion):
    if cad[posicion] == '0':
        if len(cad)-1 == posicion:
            valida()
        else:
            q2(cad,posicion+1)
    elif cad[posicion] == '1':
        if len(cad)-1 == posicion:
            noValida()
        else:
            q4(cad,posicion+1)
    else:
        noValida()

def q2(cad,posicion):
    if cad[posicion] == '0':
        if len(cad)-1 == posicion:
            noValida()
    elif cad[posicion] == '1':
        if len(cad)-1 == posicion:
            valida()
        else:
            q3(cad,posicion+1)
    else:
        noValida()

def q3(cad,posicion):
    if cad[posicion] == '0':
        if len(cad)-1 == posicion:
            noValida()
        else:
            q1(cad,posicion+1)
    elif cad[posicion] == '1':
        if len(cad)-1 == posicion:
            noValida()
        else:
            q5(cad,posicion+1)
    else:
        noValida()

def q4(cad,posicion):
    if cad[posicion] == '0':
        if len(cad)-1 == posicion:
            valida()
        else:
            q2(cad,posicion+1)
    elif cad[posicion] == '1':
        if len(cad)-1 == posicion:
            noValida()
        else:
            q5(cad,posicion+1)
    else:
        noValida()

def q5(cad,posicion):
    if cad[posicion] == '0' or cad[posicion] == '1':
        if len(cad)-1 == posicion:
            noValida()
        else:
            q5(cad,posicion+1)
    else: 
        noValida()
        
cad = input("Introduce una cadena: ")
q0(cad,0)