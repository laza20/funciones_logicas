class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None 
        
        
a = Nodo(1)
b = Nodo(5)
c = Nodo(9)
a.siguiente = b
b.siguiente = c
suma = 0
nodo_actual = a
while nodo_actual != None:
    suma += nodo_actual.valor
    nodo_actual = nodo_actual.siguiente



print(f"la suma de los nodos es de: {suma}")