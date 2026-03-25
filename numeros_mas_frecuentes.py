"""
Mostrar los elementos que mas veces son ingresados.
"""
from typing import List

def ingresar_numeros()->List:
    fin = 0
    lista_num = []
    while fin != 1:
        lista_num.append(int(input("Ingrese el numero a agregar a la lista: ")))
        fin = int(input("Si desea finalizar la carga ingrese 1, en caso contrario ingrese cualquier otro numero: "))
        
    return lista_num

def numeros_retorno():
    return int(input("Ingrese la cantidad de numeros que desea retornar: "))
    
        
def obtener_mas_frecuentes(lista_num:List, nums_tops:int)->List:
    diccionario_acomodado = {}
    for i in lista_num:
        if i in diccionario_acomodado:
            diccionario_acomodado[i] += 1
        else:
            diccionario_acomodado[i] = 1
            
    i = 0    
    lista_mas_frecuentes = sorted(diccionario_acomodado.items(), key=lambda x: x[1], reverse=True)
    lista_acomodada = []
    while i < nums_tops:
        lista_acomodada.append(lista_mas_frecuentes[i][0])
        i += 1
    
    return lista_acomodada
        
        
def mostrar(lista_acomodada, lista_numeros, tanda):
    print(f"Lista inicial: '{lista_numeros}', Lista acomodada: '{lista_acomodada}', es la prueba continua numero: '{tanda}'")
    
def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total
    
    
def inicializar():
    fin_total = 0
    tanda = 1
    while fin_total != 1:
        lista_numeros = ingresar_numeros()
        nums_tops = numeros_retorno()
        lista_acomodada = obtener_mas_frecuentes(lista_numeros, nums_tops)
        mostrar(lista_acomodada, lista_numeros, tanda)
        fin_total = finaliza()
        tanda += 1
        
    
    
inicializar()
    