"""
Dado una cadena encontrar la sub cadena mas larga (sin repetir caracteres)
"""
from typing import List, Dict, Any
import re

def ingresar_frase():
    return input("Ingrese la frase a verificar: ")


def encontrar_indices(frase:str)->int:
    longitud_sub_cadena = 0
    dict_longuitudes = {}
    i = 0
    posicion_inicial = 0
    for i in range(len(frase)):

        if frase[i] in dict_longuitudes.keys():
            posicion_inicial = max(posicion_inicial, dict_longuitudes[frase[i]] + 1)

        dict_longuitudes[frase[i]] = i
        long = i - posicion_inicial + 1
        
        if long > longitud_sub_cadena:
            longitud_sub_cadena = long
            

    return longitud_sub_cadena

    
        
        
def mostrar(frase_inicial:str, longitud_sub_cadena:int, tanda:int):
    print(f"La frase inicial es: {frase_inicial}\nLa longitud de la sub cadena mas larga es: {longitud_sub_cadena}\nEsta es la prueba numero {tanda} \nSi desea continuar cortar la prueba ingrese 1, caso contrario otro numero.")
    
def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total
    
def contacto_con_usuario()->str:
    frase = ingresar_frase()
    return frase

def computo(frase:str)->int:
    longitud_sub_cadena = encontrar_indices(frase)
    return longitud_sub_cadena

def resultado(frase:str, longitud_sub_cadena:int, tanda:int):
    mostrar(frase, longitud_sub_cadena, tanda)
    
def inicializar():
    fin_total = 0
    tanda = 1
    while fin_total != 1:
        frase = contacto_con_usuario()
        longitud_sub_cadena = computo(frase)
        resultado(frase, longitud_sub_cadena, tanda)
        fin_total = finaliza()
        tanda += 1
        
    
    
inicializar()