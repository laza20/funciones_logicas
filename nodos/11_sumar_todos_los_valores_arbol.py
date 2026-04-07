"""
Tu Primer Mini-Reto: Sumar todos los valores
Vamos a escribir una función recursiva para sumar todos los números de un árbol. 
Te voy a dar la lógica en español y tú la traduces a Python.
La lógica recursiva dice:
Caso base: 
Si el nodo en el que estoy es None, la suma es 0.
Caso recursivo: 
La suma total de este punto hacia abajo es: 
mi propio valor + la suma de mi subárbol izquierdo + la suma de mi subárbol derecho.
"""


def sumar_arbol(nodo):
    if nodo is None:
        return 0
        
    return nodo.valor + sumar_arbol(nodo.right) + sumar_arbol(nodo.left)