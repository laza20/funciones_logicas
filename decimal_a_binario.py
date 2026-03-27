"""
Transformar de decimal a binario
"""
from typing import List, Dict, Any
import re

def ingresar_numero()->int:
    num = int(input("Ingrese el numero que desea transformar: "))
        
    return num


    

def trasformar(numero_decimal:int)->List:
    if numero_decimal == 0:
        return 0
    
    if numero_decimal == 1:
        return 1
    
    lista_bin = []

    while numero_decimal > 0:
        resultado = numero_decimal % 2
        lista_bin.append(resultado)
        numero_decimal = numero_decimal // 2
            
    
    lista_bin.reverse()
    binario_numerico = int(''.join(map(str, lista_bin)))
        
    return binario_numerico
    
        
def mostrar(numero_decimal:int, numero_binario:int, tanda:int):
    print(f"El numero {numero_decimal} en binario representa: {numero_binario} esta es la prueba numero {tanda} si desea continuar cortar la prueba ingrese 1, caso contrario otro numero.")
    
def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total
    
    
def inicializar():
    fin_total = 0
    tanda = 1
    while fin_total != 1:
        numero_decimal = ingresar_numero()
        numero_binario = trasformar(numero_decimal)
        mostrar(numero_decimal, numero_binario, tanda)
        fin_total = finaliza()
        tanda += 1
        
    
    
inicializar()