"""
🏋️‍♂️ Ejercicio 7: Consulta de Sumas en Rango (LeetCode Easy)
El EnunciadoTe van a dar una lista de números enteros nums. 
Tu objetivo es crear una estructura (o función) que pueda responder rápidamente a varias 
consultas de tipo: 
"¿Cuál es la suma de los elementos desde el índice i hasta el índice j (inclusive)?".
La regla de oro: Imagina que te van a hacer miles de estas consultas sobre la misma lista. 
No puedes usar un bucle for en cada consulta para sumar los números desde i hasta j porque 
el programa sería demasiado lento. 
Debes preparar la lista de alguna forma para responder cada consulta en tiempo récord: O(1)
.Ejemplo:
Entrada: nums = [-2, 0, 3, -5, 2, -1]
Consulta 1: Sumar desde índice 0 hasta 2 ➡️ nums[0] + nums[1] + nums[2] = -2 + 0 + 3 = 1
Consulta 2: Sumar desde índice 2 hasta 5 ➡️ nums[2] + nums[3] + nums[4] + nums[5] = 3 + (-5) + 2 + (-1) = -1
Consulta 3: Sumar desde índice 0 hasta 5 ➡️ Suma de todos = -3
"""

from typing import List, Dict

def ingresar_lista()->List[int]:
    fin = 0
    lista_numeros=[]
    while fin != 1:
        lista_numeros.append(int(input("Ingrese el numero que desea añadir a la lista: ")))
        fin = int(input("Si desea finalizar la carga ingrese 1, en caso contrario presione otro numero: "))    
        
    return lista_numeros

def ingresar_la_cantidad_de_retornos()->int:
    k_uno = int(input("Ingrese el primer indice: "))
    k_dos = int(input("Ingrese el segundo indice: "))
    return k_uno, k_dos

def obtener_lista_principal(lista_numeros:List[int])->List[int]:
    suma = 0
    i = 0
    dict_res = {}
    for i in range(len(lista_numeros)):
        suma += lista_numeros[i]
        dict_res[i] = suma
        
    return dict_res

def realizar_operacion_secundaria(dict_res:Dict, k_uno:int, k_dos:int)->int:
    suma_total = dict_res[k_dos]
    suma_total -= dict_res[k_uno-1]
    return suma_total
    
def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total

def otra_operacion():
    operacion = int(input("Si no desea realizar otra operacion ingrese 1, caso contrario ingrese otro numero: "))
    return operacion


def inicializar():
    fin_total = 0
    fin_parcial = 0
    while fin_total != 1:
        lista_numeros= ingresar_lista()
        dict_res = obtener_lista_principal(lista_numeros)
        
        while fin_parcial != 1:
            k_uno, k_dos = ingresar_la_cantidad_de_retornos()
            if k_uno != 0:
                suma_total = realizar_operacion_secundaria(dict_res, k_uno, k_dos)
            else:
                suma_total = dict_res[k_dos]
            print(f"La suma desde el indice '{k_uno}' hasta el indice '{k_dos}' da como resultado: {suma_total}")
            fin_parcial = otra_operacion()
            
        fin_total = finaliza()
        
inicializar()