"""
Tu Reto Final de Árboles
Para cerrar este concepto, vamos a ver si puedes aplicar esta lógica de "comparar y decidir".

El Problema: Queremos encontrar el valor mínimo de un Árbol de Búsqueda Binaria (BST).

Pista: Recuerda la regla: los menores siempre están a la izquierda y los mayores a la derecha.

Si quieres encontrar al más chico de todos... ¿Hacia qué lado deberías viajar siempre hasta que ya no puedas más?
"""

from inicializar_nodos import nodos_con_hijos_bts

def encontrar_menor(raiz):
    if raiz.left is not None:
        return encontrar_menor(raiz.left)
    else:
        return raiz
    
    


def mostrar_resultado(res):
    print(res.valor)

def inicializar():
    raiz = nodos_con_hijos_bts()
    menor_encontrado = encontrar_menor(raiz)
    mostrar_resultado(menor_encontrado)
    
    
inicializar()
