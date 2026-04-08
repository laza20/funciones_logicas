"""
Calcular la Altura del Árbol (Max Depth)
La altura (o profundidad) de un árbol es la cantidad de niveles que 
tiene desde la raíz hasta la hoja más lejana.

Tu objetivo:
Escribe una función calcular_altura(raiz) que recorra el árbol y devuelva el número de niveles.
"""
from inicializar_nodos import nodos_con_hijos_bts

    
def profundidad(nodo):
    if nodo is None:
        return 0
    
    izq = profundidad(nodo.left)
    der = profundidad(nodo.right)
    
    return 1 + max(izq, der)
    
        

    


def inicializar():
    raiz = nodos_con_hijos_bts()
    cantidad_de_hojas = profundidad(raiz)
    print(f"la cantidad de hojas es: {cantidad_de_hojas}")
    
    
    
inicializar()