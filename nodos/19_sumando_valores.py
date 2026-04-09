"""
El Sumiller de Nodos (Sum of Nodes)
Tu misión es calcular la suma total de todos los valores almacenados en el árbol. 
No importa si es un nodo raíz, un hijo o una hoja; si tiene un número, hay que sumarlo.

Tu objetivo:
Escribe una función sumar_nodos(raiz) que devuelva la suma de todos los valor del árbol.
"""
from inicializar_nodos import nodos_con_hijos_bts

    
def calcular(nodo):
    if nodo is None:
        return 0
    print(nodo.valor)
    return nodo.valor + calcular(nodo.left) + calcular(nodo.right)
    
        

    


def inicializar():
    raiz = nodos_con_hijos_bts()
    resultado = calcular(raiz)
    print(f"El resultado de la suma de todos los nodos es de: {resultado}")
    
    
    
inicializar()