class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.left = None 
        self.right = None
        
def nodos_con_hijos_bts():
    raiz = NodoArbol(10)

    raiz.left = NodoArbol(8)
    raiz.left.left = NodoArbol(6)
    raiz.left.right = NodoArbol(1456)
    raiz.left.left.left = NodoArbol(3)
    raiz.left.left.right = NodoArbol(7)

    raiz.right = NodoArbol(12)
    raiz.right.left = NodoArbol(11)       
    raiz.right.right = NodoArbol(15)
    raiz.right.right.left = NodoArbol(13)
    raiz.right.right.right = NodoArbol(20)
    return raiz


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