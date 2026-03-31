"""
cantidad mayor de numeros consecutivos ingresados.
"""
from typing import List, Dict

def ingresar_lista()->List:
    fin = 0
    lista_numeros=[]
    while fin != 1:
        lista_numeros.append(int(input("Ingrese el numero que desea añadir a la lista: ")))
        fin = int(input("Si desea finalizar la carga ingrese 1, en caso contrario presione otro numero: "))    
        
    return lista_numeros


def convinar_intervalos(lista_numeros:List[List])->List[int]:
    orden_actual = 1
    orden_mayor = 1
    lista_ordenada = sorted(set(lista_numeros))
    for i in range(1, len(lista_ordenada)):
        if lista_ordenada[i] == lista_ordenada[i-1] + 1:
            orden_actual += 1
        else:
            orden_mayor = max(orden_mayor, orden_actual)
            orden_actual = 1
            
        
    return max(orden_mayor, orden_actual)

        
        
        


    
def mostrar(lista_numeros:List[int], retorno:int, tanda:int):
    print(f"La lista inicial es: {lista_numeros}\nLa secuencia mas larga es: {retorno}\nEsta es la prueba numero {tanda}.")
    
def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total
    
def contacto_con_usuario():
    lista_numeros = ingresar_lista()
    return lista_numeros

def computo(lista_numeros:List[int])->List[List]:
    retorno = convinar_intervalos(lista_numeros)
    return retorno

def resultado(lista_numeros:List[int], retorno:int, tanda:int):
    mostrar(lista_numeros, retorno, tanda)
    
def inicializar():
    fin_total = 0
    tanda = 1
    while fin_total != 1:
        lista_numeros = contacto_con_usuario()
        retorno = computo(lista_numeros)
        resultado(lista_numeros, retorno, tanda)
        fin_total = finaliza()
        tanda += 1
        
    
    
inicializar()