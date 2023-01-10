numPotencia = input("Introduce un numero del -5 al 5 para obtener una potencia del alfabeto: ")
alfabeto = input("Introduce un alfabeto: ")
if int(numPotencia) > 0:
    potencia =  alfabeto * int(numPotencia)
elif int(numPotencia) < 0:
    numPotencia = int(numPotencia) * -1
    alfabetoInvertido = alfabeto[::-1]
    potencia = alfabetoInvertido * numPotencia
else:
    potencia = "[ ]"
print(potencia)
