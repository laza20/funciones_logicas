"""
 Ejercicio 5: El problema de las dos sumas - Versión Ordenada (LeetCode Medium)
 Ya me contaste que resolviste el clásico Two Sum (probablemente usando un Hash Map). 
 Este es su hermano gemelo, pero con una regla que cambia las reglas del juego.
 El EnunciadoTe van a dar una lista de números enteros numbers que ya está ordenada de menor a mayor 
 (en orden ascendente) y un número entero target (objetivo).
 Debes encontrar dos números en la lista que sumados den exactamente el número target.
 La función debe devolver los índices (posiciones) de esos dos números.
 Regla de oro: No puedes usar memoria extra (nada de diccionarios ni sets). 
 Tienes que resolverlo solo moviéndote dentro de la lista original.
 Ejemplos:
 Entrada: 
 numbers = [2, 7, 11, 15], 
 target = 9
 Salida: [0, 1] 
 (Porque 2 + 7 = 9)
 Entrada: 
 numbers = [2, 3, 4], 
 target = 6
 Salida: [0, 2] 
 (Porque 2 + 4 = 6)
"""

from typing import List

def ingresar_lista()->List[int]:
    fin = 0
    lista_numeros=[]
    while fin != 1:
        lista_numeros.append(int(input("Ingrese el numero que desea añadir a la lista: ")))
        fin = int(input("Si desea finalizar la carga ingrese 1, en caso contrario presione otro numero: "))    
        
    return sorted(lista_numeros)

def ingresar_target()->int:
    verificar_resultado = int(input("ingrese el target que desea encontrar: "))
    return verificar_resultado

def obtener_posiciones(lista_numeros:List[int], target:int)-> List:
    j = len(lista_numeros) - 1
    i = 0
    while i < len(lista_numeros):
        suma = 0
        suma = lista_numeros[i] + lista_numeros[j]
        if suma == target:
            return (i, j)
        
        if suma > target:
            j -= 1
        else:
            i += 1
            
        if i == j:
            []



def inicializar():
    lista_numeros = ingresar_lista()
    target = ingresar_target()
    resultado = obtener_posiciones(lista_numeros, target)
    print(resultado)


inicializar()
