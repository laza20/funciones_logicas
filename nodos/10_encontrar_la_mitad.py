"""
Encontrar el Nodo Medio
Imagina que estás optimizando el backend de tu juego de trivia y necesitas dividir una 
lista gigante de preguntas exactamente por la mitad, 
pero el sistema no te dice cuántos nodos hay en total (no puedes usar un len()).
Tu objetivo:
Escribe una función llamada encontrar_medio(head) que reciba la cabeza de una lista enlazada.
La función debe devolver el nodo que se encuentra exactamente en la mitad de la lista.
Si la lista tiene un número impar de nodos (ej: 5 nodos), devuelves el nodo del medio (el 3°).
Si la lista tiene un número par de nodos (ej: 6 nodos), devuelves el segundo nodo del medio (el 4°).
📥 Ejemplo 1 (Impar):
Entrada: 1-> 2-> 3-> 4-> 5-> None
Salida: El nodo que contiene el valor 3. 
(Si imprimes desde ahí hasta el final verías 3 -> 4 -> 5).
📥 Ejemplo 2 (Par):
Entrada: $1-> 2-> 3-> 4-> 5-> 6-> None
Salida: El nodo que contiene el valor 4. (Si imprimes desde ahí hasta el final verías 4 -> 5 -> 6).
"""

from inicializar_nodos import lista_a, lista_b, Nodo

def encontrar_medio(head):
    camino_uno = head
    camino_dos = head
    medio = None
    while camino_dos is not None:
        
        if camino_dos.next is None:
            medio = camino_uno
            break
            
        camino_uno = camino_uno.next
        camino_dos = camino_dos.next.next
        
    if medio is None:
        medio = camino_uno
            
    return medio



def mostrar_resultado(res):
    print(res.valor)

def inicializar():
    head_a = lista_a()
    head_b = lista_b()
    medio_a = encontrar_medio(head_a)
    medio_b = encontrar_medio(head_b)
    mostrar_resultado(medio_a)
    mostrar_resultado(medio_b)
    
    
inicializar()