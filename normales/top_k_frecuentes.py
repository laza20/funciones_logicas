"""
Dada una lista de enteros, devolver los k números más frecuentes.
"""

from typing import List, Dict

def ingresar_lista()->List:
    fin = 0
    lista_numeros=[]
    while fin != 1:
        lista_numeros.append(int(input("Ingrese el numero que desea añadir a la lista: ")))
        fin = int(input("Si desea finalizar la carga ingrese 1, en caso contrario presione otro numero: "))    
        
    return lista_numeros

def ingresar_la_cantidad_de_retornos()->int:
    k = int(input("Ingrese la cantidad de numeros mas frecuentes que desea ver: "))
    return k

def buscar_mas_frecuentes(lista_numeros:List, k:int)->int:
    dict_frecuencia = {}
    for i in lista_numeros:
        if i in dict_frecuencia:
            dict_frecuencia[i] += 1
        else:
            dict_frecuencia[i] = 1
            
    
    list_k = sorted(dict_frecuencia.items(), key= lambda x:x[1], reverse=True)
    conjunto_retorno = set()
    i = 0
    while i < k:
        conjunto_retorno.add(list_k[i][0])
        i += 1
        
    return conjunto_retorno, dict_frecuencia

    
        
        
def mostrar(lista_numeros:List[int],conjunto_retorno:set, dict_frecuencia:Dict, tanda:int):
    print(f"La lista inicial es: {lista_numeros}\nLos numeros mas frecuentes son: {conjunto_retorno}\nLa frecuencia de los numeros es: {dict_frecuencia}\nEsta es la prueba numero {tanda} \nSi desea continuar cortar la prueba ingrese 1, caso contrario otro numero.")
    
def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total
    
def contacto_con_usuario():
    lista_numeros = ingresar_lista()
    k = ingresar_la_cantidad_de_retornos()
    return lista_numeros, k

def computo(lista_numeros:List, k:int)->int:
    conjunto_retorno, dict_frecuencia = buscar_mas_frecuentes(lista_numeros, k)
    return conjunto_retorno, dict_frecuencia

def resultado(lista_numeros:List[int], conjunto_retorno:set, dict_frecuencia:Dict, tanda:int):
    mostrar(lista_numeros, conjunto_retorno, dict_frecuencia, tanda)
    
def inicializar():
    fin_total = 0
    tanda = 1
    while fin_total != 1:
        lista_numeros, k = contacto_con_usuario()
        conjunto_retorno, dict_frecuencia = computo(lista_numeros, k)
        resultado(lista_numeros, conjunto_retorno, dict_frecuencia, tanda)
        fin_total = finaliza()
        tanda += 1
        
    
    
inicializar()