"""
Taget con numeros negativos.
"""

from typing import List

def ingresar_lista()->List:
    fin = 0
    lista_numeros=[]
    while fin != 1:
        lista_numeros.append(int(input("Ingrese el numero que desea añadir a la lista: ")))
        fin = int(input("Si desea finalizar la carga ingrese 1, en caso contrario presione otro numero: "))    
        
    return lista_numeros

def ingresar_taget()->int:
    target = int(input("Ingrese el subarray (Target) que desea encontra: "))
    return target

def buscar_target(lista_numeros:List, target:int)->bool:
    i = 0
    conjunto = {0}
    suma = 0
    while i < len(lista_numeros):
        numero = lista_numeros[i]
        suma += numero
        print(conjunto)
        print(suma)
        print(target)
        if suma - target in conjunto:
            return True
        
        conjunto.add(suma)
        i += 1
        
    return False

        

        
def verificar_sub_conjunto_encontrado(target:int, conjunto:set)->bool:
    if target in conjunto:
        return True
    
    return False

def inicializar():
    lista_numeros = ingresar_lista()
    target = ingresar_taget()
    resultado = buscar_target(lista_numeros, target)
    print(resultado)
    
    
inicializar()
