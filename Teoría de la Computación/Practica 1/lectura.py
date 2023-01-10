import re

#Lectura del alfabeto
patron = '[abc]+'
frase = "ieo eo"

print(len(re.findall(patron,frase)))