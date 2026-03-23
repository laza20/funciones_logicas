"""
La suma de los numero ingresados da como resultado un valor determinado 
(puede ser cualquier suma con los numeros ingresados)
"""
from typing import List

def ingrese_numeros_lista()->List:
    fin = "x"
    lista_numeros = []
    while fin == "x":
        lista_numeros.append(int(input("Ingrese el numero que desea agregar a la lista: ")))
        fin = input("si desea continuar con el ingreso presione (x), en caso contrario presione otra letra: ")
        
    return lista_numeros

def ingresar_resultado()->int:
    verificar_resultado = int(input("ingrese el numero que desea verificar: "))
    return verificar_resultado

def verificador(lista_numeros:List, verificar_resultado:int)->bool:
    resultado = 0
    lista_resultados = {0}
    for n in lista_numeros:
        resultado += n
        if resultado - verificar_resultado in lista_resultados:
            print(resultado)
            print(resultado - verificar_resultado)
            return True
        
        lista_resultados.add(resultado)

    
    return False
        
        
        
                
            
        

def inicializar():
    lista_numeros = ingrese_numeros_lista()
    verificar_resultado = ingresar_resultado()
    resultado = verificador(lista_numeros, verificar_resultado)
    print(resultado)
    
    
inicializar()