"""
Espejo de Árbol (Invert Binary Tree)
Imagina que tienes un Árbol Binario y quieres crear su "reflejo" en un espejo. 
Para lograrlo, debes intercambiar todos los hijos izquierdos por los derechos en cada nivel del árbol.

Tu objetivo:
Escribe una función llamada invertir_arbol(raiz) 
que reciba la raíz de un árbol binario y lo modifique de tal forma que quede invertido. 
La función debe devolver la nueva raíz del árbol invertido.
"""

from inicializar_nodos import nodos_con_hijos_bts

def invertir_arbol(raiz):
    if raiz is None:
        return False
    
    invertir_arbol(raiz.right)
    invertir_arbol(raiz.left)
    raiz.left, raiz.right =  raiz.right, raiz.left
    
    return raiz

    
def pintar(raiz):
    if raiz is None:
        return
    
    pintar(raiz.left)
    
    print(raiz.valor)
    
    pintar(raiz.right)

def inicializar():
    raiz = nodos_con_hijos_bts()
    
    print("--- Árbol Original ---")
    pintar(raiz)
    print("\n--- Árbol Invertido ---")
    invertir_arbol(raiz)
    pintar(raiz)
    
    
    
inicializar()
