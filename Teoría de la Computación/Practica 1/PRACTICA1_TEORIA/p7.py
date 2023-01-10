import re

def run():
    decision = ''
    while True:
        cadena = input("Introduce una cadena (debe tener una longitud minima de 5 caracteres): ")
        if len(cadena) >= 5:
            ver = revision(cadena)
            if ver:
                print(f"La cadena {cadena} es correcta")
            else: 
                print(f"La cadena {cadena} no es correcta")

            decision = input("Desea continuar? [si/no]: ")
            if decision == 'no' or decision == 'NO':
                break
        else: 
            print("La longitud no es correcta, intente de nuevo")


def revision(cadena):
    x = re.search(r'^(\d)(?!\1+$)\d*$', cadena)
    print(x)
    if x == None:
        return False
    else: 
        return True

if __name__ == '__main__':
    run()