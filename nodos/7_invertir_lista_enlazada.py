"""
Imagina que tenemos la lista: 
A -> B -> C -> None.
Queremos que termine luciendo así: 
None <- A <- B <- C
"""




class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

def invertir_lista(head):
    previo = None
    actual = head
    
    while actual is not None:
        siguiente_nodo = actual.next
        
        actual.next = previo
        
        previo = actual
        
        actual = siguiente_nodo
        
    return previo

def inicializar_nodos():
    a = Nodo(5)
    b = Nodo(9)
    c = Nodo(90)
    d = Nodo(77)
    a.next = b
    b.next = c
    c.next = d
    actual = a
    while actual is not None:
        print(f"Inicial: {actual.valor}")
        actual = actual.next
    return a


def mostrar_resultado(res):
    print(res)

def inicializar():
    head = inicializar_nodos()
    previo = invertir_lista(head)
    while previo is not None:
        print(f"Inicial: {previo.valor}")
        previo = previo.next
    
    
inicializar()