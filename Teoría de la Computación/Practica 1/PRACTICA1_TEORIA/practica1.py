import re
import random

"""--------------------------FUNCIONES------------------------------"""
def cadenasIngresadas(): #Funcion para imprimir las cadenas ingresadas
    for i in range (2):
        print(cadenas[i])

def listaAlfabeto(inicio,final): #Funcion para hacer de los elementos de un alfabeto una lista
  return list(map(chr, range(ord(inicio), ord(final)+1))) 

"""--------------------------Punto 1: Lectura del Alfabeto--------------------------"""
e = input("Introduce el alfabeto:")
inicio_e = e[0]
final_e = e[len(e)-1]
E = '[' + e + ']+' 
notE = '[^' + e + ']+' #Aquellos elementos que no pertenecen al alfabeto


"""--------------------------Punto 2: Leer 2 cadenas--------------------------"""

#Lectura de las cadenas
cadenas = []
for i in range (2): #Iterador para leer la cadena 2 veces
    w = input("Introduce la cadena {}(w{}): ".format(i+1,i+1))
    #Validacion de la cadena 1
    lcad = len(re.findall(notE,w)) #Re.findall busca coincidencias (patron, cadena)
    while(lcad!=0): #Si la lista de coincidencias no es 0 (deberia si la cadena es aceptada) no es correcta
        w = input("Introduce una cadena valida:")
        lcad = len(re.findall(notE,w))
    cadenas.append(w) #Agregamos uno por uno los elementos al arreglo
    print("Cadena {} valida:".format(i+1,i+1),w)

print("Las cadenas ingresadas son:")
cadenasIngresadas()


"""--------------------------Punto 3: Prefijos, sufijos...--------------------------"""
#Comprobar si w1 es prefijo de w2
if cadenas[1].startswith(cadenas[0])==True:
    print("w1 es un prefijo de w2")
if cadenas[1].endswith(cadenas[0])==True:
    print("w1 es un sufijo de w2")
if cadenas[1].find(cadenas[0]):
    print("w1 es una subcadena de w0")

"""--------------------------Punto 4: Generar lenguajes--------------------------"""

print("Se requieren generar 2 lenguajes aleatorios con el alfabeto E")
np = input("Ingrese el numero de elementos a ser generados: ")
l = input("Ingrese la longitud de los elementos: ")
listaLenguaje = listaAlfabeto(inicio_e,final_e) #Se crea una lista con los elementos del alfabeto
L1 = []
L2 = []
for i in range(int(np)):
        L1.append(''.join(random.choice(listaLenguaje) for _ in range(int(l))))
for i in range(int(np)):
        L2.append(''.join(random.choice(listaLenguaje) for _ in range(int(l))))
print("El primer lenguaje generado de forma aleatoria es: ",L1)
print("El segundo lenguaje generado de forma aleatoria es: ",L2)

"""--------------------------Punto 5: Resta de lenguajes--------------------------"""

setL1 = set(L1) #Usamos set para convertir una lista en un conjunto
setL2 = set(L2)
Ld = list(setL1 - setL2)
print("La diferencia de L1 - L2 es: ",Ld)

"""--------------------------Punto 6: Potencia del alfabeto--------------------------"""
numPotencia = input("Introduce un numero del -5 al 5 para obtener una potencia del alfabeto: ") #Leemos el numero [-5,5]
alfabeto = ''.join(listaLenguaje) #Se concatenan los elementos de la lista que contiene al alfabeto
if int(numPotencia) > 0:
    potencia =  alfabeto * int(numPotencia)
elif int(numPotencia) < 0:
    numPotencia = int(numPotencia) * -1
    alfabetoInvertido = alfabeto[::-1]
    potencia = alfabetoInvertido * numPotencia
else:
    potencia = "[ ]"
print(potencia)