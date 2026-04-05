"""
🐢 vs 🏎️ El Problema: Detectar un ciclo (bucle infinito)
Imagina que estás trabajando en una lista enlazada muy grande. 
Por un error en el código un nodo del final termina apuntando a un nodo que estaba más atrás.

Si intentamos recorrer esa lista con nuestro clásico bucle while actual is not None:, 
¡el programa se quedará en un bucle infinito y la memoria colapsará!
La solución de Floyd:
Imagina una pista de carreras circular. 
Si pones a correr a una tortuga y a una liebre en la misma pista:
La tortuga avanza lento (de 1 en 1 nodo).
La liebre avanza rápido (de 2 en 2 nodos).
Si la lista es lineal y no tiene ciclos, la liebre llegará al final (None) rápidamente. 
Pero si hay un ciclo, la liebre y la tortuga se quedarán dando vueltas y, eventualmente, 
¡la liebre alcanzará a la tortuga por detrás!
"""
from inicializar_nodos import cuatro_nodos_return_head

def tiene_ciclo(head):
    if head is None:
        return False
        
    tortuga = head
    liebre = head
    
    while liebre is not None and liebre.next is not None:
        tortuga = tortuga.next
        liebre = liebre.next.next
        if tortuga == liebre:
            return True
            
    return False 




def mostrar_resultado(res):
    print(res)

def inicializar():
    head = cuatro_nodos_return_head()
    ciclo = tiene_ciclo(head)
    print(ciclo)
    
    
inicializar()