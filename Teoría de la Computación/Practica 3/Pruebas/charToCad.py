#SALTA ESPACIOS

c = "C1 = a + b"
C = c.split()
print(C)
nuevaCad = "".join(C)
print(nuevaCad)
tokens = list(nuevaCad)
print(tokens)

#OTRA FORMA

print("Otra forma")
print()

c = "C1 = a + b"
nuevaCad = c.replace(' ','')
print(nuevaCad)
tokens = list(nuevaCad)
print(tokens)