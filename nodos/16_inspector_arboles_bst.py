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

    

    
def es_valido(nodo, minimo, maximo):
    if nodo is None:
        return True
    
    print(minimo, nodo.valor, maximo)
    if not (minimo < nodo.valor < maximo):
        return False
    
    izq_valida = es_valido(nodo.left, minimo, nodo.valor)
    der_valida = es_valido(nodo.right, nodo.valor, maximo)
    
    return izq_valida and der_valida
    

    
    
    
    
    

def inicializar():
    raiz = nodos_con_hijos_bts()
    retorno = es_valido(raiz, float('-inf'), float('inf'))
    if retorno == False:
        print(retorno)
    else:
        print(True)
    
    
    
inicializar()
