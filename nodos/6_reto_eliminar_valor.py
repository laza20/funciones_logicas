"""
Eliminar todos los nodos que tengan un valor específico.

Para este reto, supongamos que el nodo que queremos eliminar nunca será el primero de la lista 
(así no nos complicamos con la cabeza por ahora).

Completa los puntos suspensivos de esta función:
"""
class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.next = None 

def inicializar_nodos():
    a = Nodo(5)
    b = Nodo(9)
    c = Nodo(90)
    d = Nodo(77)
    a.next = b
    b.next = c
    c.next = d
    return a

def obtener_valor_objetivo():
    valor_a_eliminar = 900
    return valor_a_eliminar

def eliminar_nodo_por_valor(head, valor_a_eliminar):
    actual = head
    
    while actual.next is not None:
        if actual.next.valor == valor_a_eliminar:
            actual.next = actual.next.next
            return True
            
        actual = actual.next
        
    return False

def mostrar_resultado(res):
    print(res)

def inicializar():
    head = inicializar_nodos()
    valor_a_eliminar = obtener_valor_objetivo()
    resultado = eliminar_nodo_por_valor(head, valor_a_eliminar)
    mostrar_resultado(resultado)
    
    
inicializar()