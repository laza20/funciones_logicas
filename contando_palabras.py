"""
Mostrar la longitud del sub array mas largo.
"""
from typing import List, Dict, Any

def ingresar_frase()->str:
    frase = input("Ingrese la frase que desea contar: ")
        
    return frase

def separar_palabras(frase:str)->Any:
    lista_palabras = frase.split(" ")
    i=0
    diccionario_palabras = {}
    mayor = []
    mayor_repeticion = 0
    while i < len(lista_palabras):
        if lista_palabras[i].lower() not in diccionario_palabras:
            diccionario_palabras[lista_palabras[i].lower()] = 1
        else:
            diccionario_palabras[lista_palabras[i].lower()] += 1
            
        if diccionario_palabras[lista_palabras[i].lower()] > mayor_repeticion:
            mayor.clear()
            mayor.append(lista_palabras[i].lower())
            mayor.append(diccionario_palabras[lista_palabras[i].lower()])
            mayor_repeticion = diccionario_palabras[lista_palabras[i].lower()]
        i+=1
        
    return diccionario_palabras, mayor
    
        
def mostrar(dict_contabilizado:Dict, list_mayor:List,  frase:str, tanda:int):
    print(f"la frase: {frase}, tiene la siguiente organizacion en cuanto a preguntas repetidas: {dict_contabilizado}, la palabra que mas aparece es: {list_mayor}, esta es la prueba numero {tanda} si desea continuar cortar la prueba ingrese 1, caso contrario otro numero.")
    
def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total
    
    
def inicializar():
    fin_total = 0
    tanda = 1
    while fin_total != 1:
        frase = ingresar_frase()
        dict_contabilizado, list_mayor = separar_palabras(frase)
        mostrar(dict_contabilizado, list_mayor, frase, tanda)
        fin_total = finaliza()
        tanda += 1
        
    
    
inicializar()
    