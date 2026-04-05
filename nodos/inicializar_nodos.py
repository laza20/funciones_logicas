class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        
        
def cuatro_nodos_return_head():
    a = Nodo(5)
    b = Nodo(9)
    c = Nodo(90)
    d = Nodo(77)
    a.next = b
    b.next = c
    c.next = d
    return a


def cuatro_nodos_return_head():
    a = Nodo(5)
    b = Nodo(9)
    c = Nodo(90)
    d = Nodo(77)
    a.next = b
    b.next = c
    c.next = d
    return a


def lista_a():
    a = Nodo(1)
    b = Nodo(5)
    c = Nodo(7)
    d = Nodo(9)
    e = Nodo(10)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    return a

def lista_b():
    a = Nodo(4)
    b = Nodo(6)
    c = Nodo(8)
    d = Nodo(11)
    e = Nodo(13)
    f = Nodo(15)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    return a