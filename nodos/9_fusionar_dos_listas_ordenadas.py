"""
📝 El Enunciado: 
Fusionar dos listas ordenadasImagina que estás trabajando en el backend de un sistema de música y 
tienes dos listas de reproducción ya ordenadas por duración de menor a mayor. 

Tu objetivo es combinarlas en una sola lista gigante que también esté perfectamente ordenada.

Tu objetivo:
Escribe una función llamada fusionar_listas(l1, l2) que reciba la cabeza (head) de dos listas enlazadas.
Ambas listas ya vienen ordenadas de menor a mayor. 
Debes devolver la cabeza de una nueva lista enlazada que contenga todos los nodos de ambas, 
también ordenada de menor a mayor.📥 
Ejemplo de Entrada:
Lista 1 (l1): 1 -> 3 -> 5 -> None
Lista 2 (l2): 2 -> 4 -> 6 -> None
📤 Ejemplo de Salida:La función debe retornar la cabeza de la lista: 
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
"""

from inicializar_nodos import lista_a, lista_b, Nodo

def ordenar_lista_nodos(head_a, head_b):
    
    dummy = Nodo(0) 
    actual = dummy

    while head_a is not None and head_b is not None:
        if head_a.valor < head_b.valor:
            actual.next = head_a 
            head_a = head_a.next 
        else:
            actual.next = head_b 
            head_b = head_b.next
            
        actual = actual.next
        
    if head_a is not None:
        print("AAA")
        actual.next = head_a
    elif head_b is not None:
        print("BBB")
        actual.next = head_b
            
    return dummy.next



def mostrar_resultado(res):
    print(res)

def inicializar():
    head_a = lista_a()
    head_b = lista_b()
    dummy_head = ordenar_lista_nodos(head_a, head_b)
    nodo_actual = dummy_head
    while nodo_actual is not None:
        print({nodo_actual.valor})
        nodo_actual = nodo_actual.next
    
    
inicializar()