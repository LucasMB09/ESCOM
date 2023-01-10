def listAlphabet(inicio,final):
  return list(map(chr, range(ord(inicio), ord(final)+1))) #Funcion a lista

a = input("Ingresa una cadena: ")
inicio = a[0]
final = a[len(a)-1]
if((inicio.isalpha() and final.isalpha()) == True):
     print(listAlphabet(inicio,final))