"""
Ingresar una lista de numeros, si existe un repetido dara True, caso contrario False.
"""
from typing import List

def ingresar_numeros()->List:
    fin = 0
    lista_num = []
    while fin != 1:
        lista_num.append(int(input("Ingrese el numero a agregar a la lista: ")))
        fin = int(input("Si desea finalizar la carga ingrese 1, en caso contrario ingrese cualquier otro numero: "))
        
    return lista_num

        
def verificar_repetidos(lista_num:List)->List:
    i = 0
    conjunto = set()
    while i < len(lista_num):
        if lista_num[i] in conjunto:
            return True
        else:
            conjunto.add(lista_num[i])
            i += 1
        
        
    return False
    
    
def mostrar(resultado:bool):
    print(resultado)
    
def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total
    
def inicializar():
    fin_total = 0
    tanda = 1
    while fin_total != 1:
        lista_numeros = ingresar_numeros()
        resultado = verificar_repetidos(lista_numeros)
        mostrar(resultado)
        fin_total = finaliza()
        tanda += 1
        
    
    
inicializar()