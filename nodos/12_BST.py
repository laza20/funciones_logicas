"""
El Árbol de Búsqueda Binaria (BST)
Ahora que entendés cómo recorrerlo, 
vamos a ver un tipo especial de árbol que se usa para buscar datos ultra rápido: el BST.
En un BST, hay una regla sagrada:
Todo lo que es menor que el nodo actual, va a la izquierda.
Todo lo que es mayor que el nodo actual, va a la derecha.
Tu Reto:
Si quisieras buscar si un número X existe en el árbol, 
¿tendrías que recorrer todos los caminos o podrías "descartar" ramas enteras?
Si estás en un nodo que vale 50 y buscás el 25
"""

from inicializar_nodos import nodos_con_hijos_bts

def encontrar_objetivos(raiz:int, objetivo:int)->bool:
    print(raiz.valor)
    if raiz is None:
        return False
    
    if raiz.valor == objetivo:
        return True
    
    if raiz.valor > objetivo:
        return encontrar_objetivos(raiz.left, objetivo)
    else:
        return encontrar_objetivos(raiz.right, objetivo)


def mostrar_resultado(res):
    print(res)

def inicializar():
    objetivo = 3
    raiz = nodos_con_hijos_bts()
    encontrado = encontrar_objetivos(raiz, objetivo)
    mostrar_resultado(encontrado)
    
    
inicializar()
