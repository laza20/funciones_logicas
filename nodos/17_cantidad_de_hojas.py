"""
El Contador de Hojas (Count Leaves)
En un árbol, una hoja es aquel nodo que no tiene hijos 
(es decir, tanto su left como su right son None). Tu misión es contar cuántas de estas 
"puntas" tiene el árbol en total.

Tu objetivo:
Escribe una función contar_hojas(raiz) que recorra todo el árbol y devuelva el número total 
de nodos hoja.
"""
from inicializar_nodos import nodos_con_hijos_bts

    
def hojas(nodo):
    if nodo is None:
        return 0
    
    if nodo.right is None and nodo.left is None:
        return 1
    
    return hojas(nodo.left) + hojas(nodo.right)
        

    


def inicializar():
    raiz = nodos_con_hijos_bts()
    cantidad_de_hojas = hojas(raiz)
    print(f"la cantidad de hojas es: {cantidad_de_hojas}")
    
    
    
inicializar()