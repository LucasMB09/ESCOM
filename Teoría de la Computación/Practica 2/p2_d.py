
def valido():
    print("Monto suficiente. ¡Tome su bebida!")

def noValido():
    print("Dinero insuficiente")

def q0(cad,posicion):
    if cad[posicion] == '1':
        if len(cad)-1 == posicion:
            noValido()
        else:
            q1(cad,posicion+1)
    elif cad[posicion] == '2':
        if len(cad)-1 == posicion:
            noValido()
        else:
            q2(cad,posicion+1)
    elif cad[posicion] == '5':
        if len(cad)-1 == posicion:
            valido()
        else:
            q5(cad,posicion+1)
    else:
        noValido()

def q1(cad,posicion):
    if cad[posicion] == '1':
        if len(cad)-1 == posicion:
            noValido()
        else:
            q2(cad,posicion+1)
    elif cad[posicion] == '2':
        if len(cad)-1 == posicion:
            noValido()
        else:
            q3(cad,posicion+1)
    elif cad[posicion] == '5':
        if len(cad)-1 == posicion:
            valido()
        else:
            q5(cad,posicion+1)
    else:
        noValido()

def q2(cad,posicion):
    if cad[posicion] == '1':
        if len(cad)-1 == posicion:
            noValido()
        else:
            q3(cad,posicion+1)
    elif cad[posicion] == '2':
        if len(cad)-1 == posicion:
            noValido()
        else:
            q4(cad,posicion+1)
    elif cad[posicion] == '5':
        if len(cad)-1 == posicion:
            valido()
        else:
            q5(cad,posicion+1)
    else:
        noValido()

def q3(cad,posicion):
    if cad[posicion] == '1':
        if len(cad)-1 == posicion:
            noValido()
        else:
            q4(cad,posicion+1)
    elif cad[posicion] == '2' or cad[posicion] == '5':
        if len(cad)-1 == posicion:
            valido()
        else:
            q5(cad,posicion+1)
    else:
        noValido()

def q4(cad,posicion):
    if cad[posicion] == '1' or cad[posicion] == '2' or cad[posicion] == '5':
        if len(cad)-1 == posicion:
            valido()
        else:
            q5(cad,posicion+1)
    else:
        noValido()

def q5(cad,posicion):
    if cad[posicion] == '1' or cad[posicion] == '2' or cad[posicion] == '5':
        if len(cad)-1 == posicion:
            valido()
        else:
            q5(cad,posicion+1)
    else:
        noValido()

cad = input("Ingrese $5 para entregarle una bebida: ")
if len(cad) == 0:
    noValido
else:
    q0(cad,0)