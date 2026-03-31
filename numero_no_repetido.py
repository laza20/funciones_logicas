"""
Ejercicio 3: Encontrar el elemento que no se repite (LeetCode Easy)
El Enunciado
Te van a dar una lista de números enteros donde todos los números se repiten exactamente dos veces, excepto uno, que aparece solo una vez. Tu objetivo es encontrar ese número que no se repite.
(Nota: Tienes que resolverlo con una complejidad de tiempo lineal, es decir, recorriendo la lista la menor cantidad de veces posible).
Ejemplos:
Entrada: nums = [2, 2, 1] ➡️ Salida: 1
Entrada: nums = [4, 1, 2, 1, 2] ➡️ Salida: 4
Entrada: nums = [1] ➡️ Salida: 1
"""
from typing import List

def ingresar_lista()->List[int]:
    fin = 0
    lista_numeros=[]
    while fin != 1:
        lista_numeros.append(int(input("Ingrese el numero que desea añadir a la lista: ")))
        fin = int(input("Si desea finalizar la carga ingrese 1, en caso contrario presione otro numero: "))    
        
    return lista_numeros

def encontrar_unico(nums: List[int]) -> int:
    conteo = {}
    
    for n in nums:
        if n in conteo:
            conteo[n] += 1
        else:
            conteo[n] = 1
    
    for k, v in conteo.items():
        if v == 1:
            return k

    return "Todos los numeros esta repetidos."



def inicializar():
    lista_numeros = ingresar_lista()
    resultado = encontrar_unico(lista_numeros)
    print(resultado)


inicializar()