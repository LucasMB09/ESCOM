import re
import random

e = input("Introduce el alfabeto:")
E = '[' + e + ']+' 
notE = '[^' + e + ']+' #Aquellos elementos que no pertenecen al alfabeto

print(random.sample(E,5))