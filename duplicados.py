"""
El usuario ingresa una serie de numeros y en caso de haber duplicados se devuelve 
True
en caso contrario
False
"""
from typing import List

def ingresar_numeros()->List[int]:
    lista_numeros = []
    while True:
        numero = int(input("Ingrese un numero: "))
        lista_numeros.append(numero)
        final = input("""En caso de que desee finalizar la carga de numeros ingrese F,
        en caso contrario, ingrese cualquier otro resultado: """)
        if final.capitalize() == "F":
            resultado = verificar_duplicados(lista_numeros)
            print(lista_numeros)
            print(resultado)
            break
            
    
def verificar_duplicados(lista_numeros:List[int])->bool:
    for n in range(len(lista_numeros)):
        for m in range(n+1, len(lista_numeros)):
            if lista_numeros[m] == lista_numeros[n]:
                return True
            
    return False


ingresar_numeros()
