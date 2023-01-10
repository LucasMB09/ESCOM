def valido():
    print("Cadena valida")
def noValido():
    print("Cadena no valida")

def q0(numero,posicion):
    if numero[posicion] == '+' or numero[posicion] == '-':
        if (len(numero)-1) == posicion:
            noValido()
        else:
            q1(numero,posicion+1)
    elif numero.isdigit():
        if (len(numero)-1) == posicion:
            valido()
        else:
            q2(numero,posicion+1)

def q1(numero,posicion):
    if (numero[posicion].isdigit()):
        if (len(numero)-1) == posicion:
            valido()
        else:
            q2(numero,posicion+1)
    else:
        noValido()

def q2(numero,posicion):
    if numero[posicion].isdigit():
        if (len(numero)-1) == posicion:
            valido()
        else:
            q2(numero,posicion+1)
    elif (len(numero)-1) == posicion:
            noValido()
            if numero[posicion] == '.':
                q3(numero,posicion+1)
            elif numero[posicion] == 'E' or numero[posicion] == 'e':
                q5(numero,posicion+1)
            else:
                noValido()
    else:
        noValido()
    
def q3(numero,posicion):
    if (numero[posicion].isdigit()):
        if (len(numero)-1) == posicion:
            valido()
        else:
            q4(numero,posicion+1)
    else:
        noValido()

def q4(numero,posicion):
    if (numero[posicion].isdigit()):
        if (len(numero)-1) == posicion:
            valido()
        else:
            q4(numero,posicion+1)
    elif numero[posicion] == 'E' or numero[posicion] == 'e':
        if (len(numero)-1) == posicion:
            noValido()
        else:
            q5(numero,posicion+1)
    else:
        noValido()

def q5(numero,posicion):
    if (numero[posicion].isdigit()):
        if (len(numero)-1) == posicion:
            valido()
        else:
            q7(numero,posicion+1)
    elif (numero[posicion] == '+') or (numero[posicion] == '-'):
        if (len(numero)-1) == posicion:
            noValido()
        else:
            q6(numero,posicion+1)
    else:
        noValido()

def q6(numero,posicion):
    if (numero[posicion].isdigit()):
        if (len(numero)-1) == posicion:
            valido()
        else:
            q7(numero,posicion+1)
    else:
        noValido()

def q7(numero,posicion):
    if (numero[posicion].isdigit()):
        if (len(cad)-1) == posicion:
            valido()
        else:
            q7(numero,posicion+1)
    else:
        noValido()


cad = input("Ingrese un numero: ")
q0(cad,0)
