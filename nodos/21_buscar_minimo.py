"""
Escribe una función buscar_minimo(nodo) que devuelva el valor más pequeño presente en el árbol.
"""
from inicializar_nodos import nodos_con_hijos_bts

    
def buscar_minimo(nodo):
    if nodo is None:
        return None
    if nodo.left is None:
        return nodo
    return buscar_minimo(nodo.left)

def buscar_maximo(nodo):
    if nodo is None:
        return None
    if nodo.right is None:
        return nodo
    return buscar_maximo(nodo.right)
    

def inicializar():
    raiz = nodos_con_hijos_bts()
    resultado = buscar_minimo(raiz)
    resultado_dos = buscar_maximo(raiz)
    print(resultado.valor)
    print(resultado_dos.valor)
    
    
    
inicializar()