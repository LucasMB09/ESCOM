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
            return

        print(f"Desapilar {self.superior.dato}")
        self.superior = self.superior.siguiente

    def imprimir(self):
        print("Imprimiendo pila:")
        # Recorrer la pila e imprimir valores
        nodo_temporal = self.superior
        while nodo_temporal != None:
            print(f"{nodo_temporal.dato}")
            nodo_temporal = nodo_temporal.siguiente

    def estaVacia(self):
        if self.superior == None:
            return 1
        else:
            return 0



pila = Pila()
print(pila.estaVacia())
pila.push("Luis")
pila.push("María José")
pila.push("Ethan")
pila.imprimir()
pila.pop()
pila.imprimir()
pila.push("Leon Scott Kennedy")
pila.imprimir()
pila.pop()
pila.pop()
pila.imprimir()
pila.pop()
pila.pop()
pila.imprimir()