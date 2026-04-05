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

        
def buscar_valor(head, valor_objetivo):
    nodo_actual = head

    while nodo_actual is not None:
        if nodo_actual.valor == valor_objetivo:
            return True 
        
        nodo_actual = nodo_actual.next

    return False


def valores_nodos():
    a.next = b
    b.next = c
    c.next = d

    valor_objetivo = 555
    head = a
    return head, valor_objetivo


def inicializar():
    head, valor_objetivo = valores_nodos()
    retorno = buscar_valor(head, valor_objetivo)
    print(retorno)
    
inicializar()
