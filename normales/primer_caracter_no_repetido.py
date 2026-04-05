"""
Retornar el primer caracter no repetido de una frase.
"""
import re

def ingresar_frase()->str:
    return input("Ingrese la frase a testear: ")


    

def retornar_primer_letra_no_repetida(frase:str)->str:
    dic_letras = {}
    frase_formateada = re.sub(r'[^a-zA-Z0-9]', '', frase)
    for i in frase_formateada:
        if i in dic_letras:
            dic_letras[i] += 1
        else:
            dic_letras[i] = 1
            
    
    for i in frase_formateada:
        if dic_letras[i] == 1:
            return i
    
    return "Todas las letras estan repetidas."
    
        
        
        

    
        
def mostrar(frase:str, letra_no_repetida:str, tanda:int):
    print(f"La frase es: {frase}, la primer letra no repetida: {letra_no_repetida},  esta es la prueba numero {tanda} si desea continuar cortar la prueba ingrese 1, caso contrario otro numero.")
    
def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total
    
    
def inicializar():
    fin_total = 0
    tanda = 1
    while fin_total != 1:
        frase = ingresar_frase()
        primer_letra = retornar_primer_letra_no_repetida(frase)
        mostrar(frase, primer_letra, tanda)
        fin_total = finaliza()
        tanda += 1
        
    
    
inicializar()