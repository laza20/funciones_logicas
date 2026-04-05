"""
Imagina que estás en una entrevista y te dan esta función para completar. 
El objetivo es buscar si un número existe dentro de la lista enlazada.

Completa el código donde están los puntos suspensivos:
"""


class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.next = None 
        
a = Nodo(5)
b = Nodo(9)
c = Nodo(89)
d = Nodo(77)


def valores_nodos():
    a.next = b
    b.next = c
    c.next = d

    a.next = a.next.next
    print(a.next.valor) #89
    return 


def inicializar():
    head = valores_nodos()
    
inicializar()
