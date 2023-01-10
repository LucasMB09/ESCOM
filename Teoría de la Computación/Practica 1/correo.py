web=input("Ingrese su web empresarial:")
primNom=input("Ingrese su primer nombre:")
secNom=input("Ingrese su segundo nombre:")
apell=input("Ingrese su apellido:")
fnac=input("Ingrese su fecha de nacimiento:")

s1 = primNom[0]
s2 = secNom[0]
s4 = fnac[2:]
s6 = web[4:-4]

correo = s1 + s2 + apell + s4 + "@" + s6 + ".com"
print(correo)
