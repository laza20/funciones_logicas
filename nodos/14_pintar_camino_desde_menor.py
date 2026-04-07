"""
El "Ordenador" Automático
Vamos a escribir una función que, en lugar de sumar, imprima los valores. 
Tu misión es completar la función para que siga el orden: Izquierda -> Actual -> Derecha.
"""

from inicializar_nodos import nodos_con_hijos_bts

def pintar_menor_a_mayor(raiz):
    if raiz is None:
        return
    
    pintar_menor_a_mayor(raiz.left)
    
    print(raiz.valor)
    
    pintar_menor_a_mayor(raiz.right)
    
    
def pintar_orden_a_menor_a_mayor(raiz):
    if raiz is None:
        return
    
    pintar_menor_a_mayor(raiz.left)
    
    print(raiz.valor)
    
    pintar_menor_a_mayor(raiz.right)
    

def inicializar():
    raiz = nodos_con_hijos_bts()
    pintar_menor_a_mayor(raiz)
    
    
inicializar()
