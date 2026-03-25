"""
Mostrar por consola una lista con los ceros al final
"""
from typing import List

def ingresar_numeros()->List:
    fin = 0
    lista_num = []
    while fin != 1:
        lista_num.append(int(input("Ingrese el numero a agregar a la lista: ")))
        fin = int(input("Si desea finalizar la carga ingrese 1, en caso contrario ingrese cualquier otro numero: "))
        
    return lista_num

        
def acomodar_lista(lista_num:List)->List:
    lista_form = lista_num.copy()
    pos = 0
    i = 0
    while i < len(lista_form):
        if lista_form[i] != 0:
            lista_form[pos] = lista_form[i]
            pos += 1
        
        i += 1
        
    while pos < len(lista_form):
        lista_form[pos] = 0
        pos += 1
    
    return lista_form
        
        
def mostrar(lista_acomodada, lista_numeros, tanda):
    print(f"Lista inicial: '{lista_numeros}', Lista acomodada: '{lista_acomodada}', es la prueba continua numero: '{tanda}'")
    
    
    
def inicializar():
    fin_total = 0
    tanda = 1
    while fin_total != 1:
        lista_numeros = ingresar_numeros()
        lista_acomodada = acomodar_lista(lista_numeros)
        mostrar(lista_acomodada, lista_numeros, tanda)
        fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
        tanda += 1
        
    
    
inicializar()
    