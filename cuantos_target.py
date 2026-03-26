"""
Mostrar la cantidad de sub arrays que hay.
"""
from typing import List

def ingresar_numeros()->List:
    fin = 0
    lista_num = []
    while fin != 1:
        lista_num.append(int(input("Ingrese el numero a agregar a la lista: ")))
        fin = int(input("Si desea finalizar la carga ingrese 1, en caso contrario ingrese cualquier otro numero: "))
        
    return lista_num

def target():
    return int(input("Ingrese el target: "))
    
        
def obtener_targets(lista_num:List, nums_target:int)->List:
    dict_apariciones = {"cantidad_targets":0}
    dict_resultados = {0:1}
    i = 0
    suma = 0
    while i < len(lista_num):
        suma += lista_num[i] 
        if suma - nums_target in dict_resultados:
            print(f"Resultado: {suma - nums_target}")
            dict_apariciones["cantidad_targets"] += dict_resultados[suma - nums_target]
        
        if suma not in dict_resultados:
            dict_resultados[suma] = 1
        else:
            dict_resultados[suma] += 1
        
        i += 1

    return dict_apariciones
            
    
        
        
def mostrar(dict_apariciones, lista_numeros, tanda):
    print(f"Lista inicial: '{lista_numeros}', cantidad de targets: '{dict_apariciones["cantidad_targets"]}', es la prueba continua numero: '{tanda}'")
    
def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total
    
    
def inicializar():
    fin_total = 0
    tanda = 1
    while fin_total != 1:
        lista_numeros = ingresar_numeros()
        num_target = target()
        dict_apariciones = obtener_targets(lista_numeros, num_target)
        mostrar(dict_apariciones, lista_numeros, tanda)
        fin_total = finaliza()
        tanda += 1
        
    
    
inicializar()
    