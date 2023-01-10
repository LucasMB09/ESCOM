def q0(cadena,posicion):
    if cadena[posicion] == 'x':
        q1(cadena,posicion+1)
    else: 
        print("Cadena no valida")

def q1(cadena,posicion):
    if cadena[posicion] == 'y':
        q2(cadena,posicion+1)
    else:
        print("Cadena no valida")

def q2(cadena,posicion):
    if cadena[posicion] == 'z':
        print("Cadena valida")
    else:
        print("Cadena no valida")

cad = input("Introduce una cadena: ")
q0(cad,0)