"""
Dada una lista de enteros (pueden ser positivos y negativos), encontrar:
la cantidad de subarrays continuos cuya suma sea igual a un target
"""

from typing import List

def ingresar_lista()->List:
    fin = 0
    lista_numeros=[]
    while fin != 1:
        lista_numeros.append(int(input("Ingrese el numero que desea añadir a la lista: ")))
        fin = int(input("Si desea finalizar la carga ingrese 1, en caso contrario presione otro numero: "))    
        
    return lista_numeros

def ingresar_target()->int:
    target = int(input("Ingrese el subarray (Target) que desea encontra: "))
    return target


def buscar_targets(lista_numeros:List, target:int)->int:
    sub_arrays = 0
    dict_resultados = {0:1}
    suma = 0
    for i in range(len(lista_numeros)):
        suma += lista_numeros[i]
            
        if suma - target in dict_resultados:
            sub_arrays += dict_resultados[suma - target]
            
            
        if suma in dict_resultados:
            dict_resultados[suma] += 1
        else:
            dict_resultados[suma] = 1
        print(dict_resultados)

    return sub_arrays

    
        
        
def mostrar(lista_numeros:List[int], target:int, sub_arrays:List[int], tanda:int):
    print(f"La lista inicial es: {lista_numeros}\nEl target ingresado: {target}\nLa cantidad de subarrays encontrados son: {sub_arrays}\nEsta es la prueba numero {tanda} \nLa cantidad de subarrays encontrados son: {sub_arrays}\nSi desea continuar cortar la prueba ingrese 1, caso contrario otro numero.")
    
def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total
    
def contacto_con_usuario():
    lista_numeros = ingresar_lista()
    target = ingresar_target()
    return lista_numeros, target

def computo(lista_numeros:List, target:int)->int:
    sub_arrays = buscar_targets(lista_numeros, target)
    return sub_arrays

def resultado(lista_numeros:List[int], target:int, sub_arrays:List[int], tanda:int):
    mostrar(lista_numeros, target, sub_arrays, tanda)
    
def inicializar():
    fin_total = 0
    tanda = 1
    while fin_total != 1:
        lista_numeros, target = contacto_con_usuario()
        sub_arrays = computo(lista_numeros, target)
        resultado(lista_numeros, target, sub_arrays, tanda)
        fin_total = finaliza()
        tanda += 1
        
    
    
inicializar()