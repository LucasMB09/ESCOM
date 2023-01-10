import nltk
from nltk import CFG
import os

#FUNCION PARA SEPARAR LA CADENA EN TOKENS
def creaTokens(cadena):
    nuevaCad = cadena.replace(' ','')
    tokens = list(nuevaCad)
    return tokens

def comeEspacios(cadena):
    nuevaCad = cadena.replace(' ','')
    return nuevaCad

"""---------------INICIA CODIGO DE LA PILA---------------"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.superior = None

    def push(self, dato):
        print(f"Agregando {dato} en la cima de la pila")
        # Si no hay datos, agregamos el valor en el elemento superior y regresamos
        if self.superior == None:
            self.superior = Nodo(dato)
            return
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo

    def pop(self):
        # Si no hay datos en el nodo superior, regresamos
        if self.superior == None:
            print("No hay ningún elemento en la pila para desapilar")
            return 1

        print(f"Desapilar {self.superior.dato}")
        self.superior = self.superior.siguiente

    def imprimir(self):
        print("Imprimiendo pila:")
        # Recorrer la pila e imprimir valores
        nodo_temporal = self.superior
        while nodo_temporal != None:
            print(f"{nodo_temporal.dato}", end=",")
            nodo_temporal = nodo_temporal.siguiente
        print("")
    
    def estaVacia(self):
        if self.superior == None:
            return 1
        else:
            return 0

pila = Pila()
"""-------------------TERMINA CODIGO DE LA PILA------------------"""
def estado(numero):
    print(f"Pase por el estado el estado q{numero}")

#GRAMATICA
grammar = CFG.fromstring("""
E -> SN SV ';'
SN -> ID '='
SV -> ID | SV '+' SV | SV '-' SV | SV '*' SV | SV '/' SV | SV '%' SV | '(' SV ')'
ID -> ID LETRA | ID DIGITO | LETRA | DIGITO
DIGITO -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' 
LETRA -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' | 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z'
""")

grammar.start()
grammar.productions()

"""---------------CODIGO DEL AUTOMATA DE PILA--------------------"""

posicion = 0
letras =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numeros = ['0','1','2','3','4','5','6','7','8','9']
operadores = ['+','-','*','/','%']


def valido():
    print("Pila vacia y me encuentro en un estado de aceptacion: palabra aceptada")
    print()

def noValido():
    print("Sin pila vacia y no me encuentro en un estado de aceptacion: palabra rechazada")
    print()

def q0(cad,posicion):
    estado(0)
    if (len(cad)-1) == posicion:
            noValido()
    else:
        if cad[posicion] in letras:
            q1(cad,posicion+1)
        else:
            noValido()

def q1(cad,posicion):
    estado(1)
    if (len(cad)-1) == posicion:
            noValido()
    else:
        if cad[posicion] in letras:
            q1(cad,posicion+1)
        elif cad[posicion] in numeros:
            q1(cad,posicion+1)
        elif cad[posicion] == '=':
            pila.push("#")
            q2(cad,posicion+1)
        else:
            noValido()

def q2(cad,posicion):
    estado(2)
    if (len(cad)-1) == posicion:
            noValido()
    else:
        if cad[posicion] in letras:
            q3(cad,posicion+1)
        elif cad[posicion] in numeros:
            q3(cad,posicion+1)
        elif cad[posicion] == '(':
            pila.push("#")
            q5(cad,posicion+1)
        else:
            noValido()

def q3(cad,posicion):
    estado(3)
    if (len(cad)-1) == posicion and cad[posicion] == ';':
        pila.pop()
        q6(cad,posicion+1)
    elif (len(cad)-1) == posicion:
        noValido()
    else:
        if cad[posicion] in letras:
            q3(cad,posicion+1)
        elif cad[posicion] in numeros:
            q3(cad,posicion+1)
        elif cad[posicion] in operadores:
            q4(cad,posicion+1)
        elif cad[posicion] == ')':
            pila.pop()
            q7(cad,posicion+1)
        else:
            noValido()

def q4(cad,posicion):
    estado(4)
    if (len(cad)-1) == posicion:
            noValido()
    else:
        if cad[posicion] in letras:
            q3(cad,posicion+1)
        elif cad[posicion] in numeros:
            q3(cad,posicion+1)
        elif cad[posicion] == '(':
            pila.push('#')
            q5(cad,posicion+1)
        elif cad[posicion] == ')':
            pila.pop()
            q7(cad,posicion+1)
        else:
            noValido()

def q5(cad,posicion):
    estado(5)
    if (len(cad)-1) == posicion:
            noValido()
    else:
        if cad[posicion] in letras:
            q3(cad,posicion+1)
        elif cad[posicion] in numeros:
            q3(cad,posicion+1)
        elif cad[posicion] == '(':
            pila.push('#')
            q5(cad,posicion+1)
        else:
            noValido()

def q6(cad,posicion):
    estado(6)
    print(f"¿Pila vacia? = {pila.estaVacia()}")
    if pila.estaVacia() == 1:
        valido()
        tokens = creaTokens(cad)
        parser = nltk.ChartParser(grammar)
        for tree in parser.parse(tokens):
            print(tree)
        tree.draw()
    else:
        noValido()

def q7(cad,posicion):
    estado(7)
    if (len(cad)-1) == posicion and cad[posicion] == ';':
        pila.pop()
        q6(cad,posicion+1)
    elif (len(cad)-1) == posicion:
        noValido()
    else:
        if cad[posicion] in operadores:
            q4(cad,posicion+1)
        else:
            noValido()

"""--------------FIN CODIGO DE AUTOMATA DE PILA------------------"""

while(1):
    cad = input("Introduce una cadena: ")
    nuevaCad = comeEspacios(cad)
    if nuevaCad[0] in numeros:
        print("La primera letra de la variable debe empezar con una letra")
    else:
        q0(nuevaCad,posicion)