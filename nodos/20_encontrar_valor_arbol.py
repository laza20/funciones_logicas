"""
Escribe una función buscar_valor(nodo, objetivo) que devuelva True si el objetivo está en el árbol 
y False si no lo encuentra.
"""
from inicializar_nodos import nodos_con_hijos_bts

    
def buscar(nodo, objetivo):
    if nodo is None:
        return False
    
    print(nodo.valor)

    if objetivo == nodo.valor:
        return True
    elif objetivo < nodo.valor:
        return buscar(nodo.left, objetivo)
    else:
        return buscar(nodo.right, objetivo)

    
    

def inicializar():
    raiz = nodos_con_hijos_bts()
    objetivo = 5
    resultado = buscar(raiz, objetivo)
    print(resultado)
    
    
    
inicializar()