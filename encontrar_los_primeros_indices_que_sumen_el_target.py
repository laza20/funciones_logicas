"""
Dada una lista de enteros y un número objetivo (target),
retornar los índices de los dos números cuya suma sea igual al target.
"""

"""
Retornar el primer caracter no repetido de una frase.
"""
from typing import List, Dict, Any
import re

def ingresar_numeros()->List[int]:
    fin = 0
    lista_num = []
    while fin != 1:
        lista_num.append(int(input("Ingrese el numero a agregar a la lista: ")))
        fin = int(input("Si desea finalizar la carga ingrese 1, en caso contrario ingrese cualquier otro numero: "))
        
    return lista_num

def ingresar_target()->int:
    target = int(input("Ingrese el subarray (Target) que desea encontra: "))
    return target

    

def encontrar_indices(lista_numeros:List, target:int)->List[int]:
    dic_indices = {}
    i = 0
    while i < len(lista_numeros):
        diferencia = target - lista_numeros[i]
        print(dic_indices)
        if diferencia in dic_indices:
            return [dic_indices[diferencia], i]
        
        dic_indices[lista_numeros[i]] = i
        i += 1
    
    return dic_indices
    
        
        
def mostrar(lista_indices:List[int], lista_numeros:List[int], target:int, tanda:int):
    print(f"La lista inicial es: {lista_numeros}\nEl target es: {target}\nLos indices que dan como resultado el target encuentran en las posiciones: {lista_indices}\nEsta es la prueba numero {tanda} \nSi desea continuar cortar la prueba ingrese 1, caso contrario otro numero.")
    
def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total
    
def contacto_con_usuario()->Any:
    lista_numeros = ingresar_numeros()
    target = ingresar_target()
    return lista_numeros, target

def computo(lista_numeros:List, target:int)->List[int]:
    lista_indices = encontrar_indices(lista_numeros, target)
    return lista_indices

def resultado(dict_indices:Dict, lista_numeros:List, target:int, tanda:int):
    mostrar(dict_indices, lista_numeros, target, tanda)
    
def inicializar():
    fin_total = 0
    tanda = 1
    while fin_total != 1:
        lista_numeros, target = contacto_con_usuario()
        lista_indices = computo(lista_numeros, target)
        resultado(lista_indices, lista_numeros, target, tanda)
        fin_total = finaliza()
        tanda += 1
        
    
    
inicializar()