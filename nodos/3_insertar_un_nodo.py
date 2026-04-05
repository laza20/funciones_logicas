class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None 


a = Nodo(1)
c = Nodo(9)
a.siguiente = c

b = Nodo(5)
b.siguiente = c
a.siguiente = b
print(a.siguiente, b.siguiente, c.siguiente)