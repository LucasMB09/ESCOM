def comeEspacios(cadena):
    nuevaCad = cadena.replace(' ','')
    return nuevaCad

cad = input("Introduce una cadena: ")
nuevaCad = comeEspacios(cad)
print(nuevaCad)