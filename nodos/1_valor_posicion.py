class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None 
        
        
x = Nodo(1)
y = Nodo(5)

y.siguiente = x

print(f"valor de y: {y.valor}, siguiente nodo despues de y: {y.siguiente}, valor de x: {x.valor}, siguiente nodo despues de y: {x.siguiente}")