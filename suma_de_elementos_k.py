"""
El Enunciado
Te van a dar una lista de números enteros nums y un número entero k. Debes encontrar la suma máxima de cualquier "subarray" 
(un grupo de elementos contiguos, es decir, pegados uno al lado del otro) que tenga exactamente una longitud de k.

Ejemplos:
Entrada: nums = [1, 5, 4, 2, 9, 9, 9], 
k = 3
Salida: 27
Explicación: Los subarrays de tamaño 3 son:
[1, 5, 4] suma 10
[5, 4, 2] suma 11
[4, 2, 9] suma 15
[2, 9, 9] suma 20
[9, 9, 9] suma 27 ➡️ ¡Esta es la suma máxima!
"""
from typing import List

def ingresar_lista()->List[int]:
    fin = 0
    lista_numeros=[]
    while fin != 1:
        lista_numeros.append(int(input("Ingrese el numero que desea añadir a la lista: ")))
        fin = int(input("Si desea finalizar la carga ingrese 1, en caso contrario presione otro numero: "))    
        
    return lista_numeros

def ingresar_resultado()->int:
    verificar_resultado = int(input("ingrese la cantidad de numeros del subarray: "))
    return verificar_resultado

def max_k(nums: List[int], k:int) -> int:
    resultado_actual = 0
    for n in nums[:k]:
        resultado_actual += n
    
    resultado_mayor = resultado_actual
    for i in range(k, len(nums)):
        resultado_actual -= nums[i-k]
        resultado_actual += nums[i]
        if resultado_actual > resultado_mayor:
            resultado_mayor = resultado_actual
            
    return resultado_mayor



def inicializar():
    lista_numeros = ingresar_lista()
    k = ingresar_resultado()
    resultado = max_k(lista_numeros, k)
    print(resultado)


inicializar()
