"""
El usuario ingresa un string, el cual en caso de que una letra no se repita, devuelve
la primera letra no repetida 
"""

def ingresar_palabra():
    palabra = input("Ingrese la palabra que desea verificar: ")
    resultado = verificar_caracter_repetido(palabra)
    print(resultado)

def verificar_caracter_repetido(palabra:str)->str:
    for s in range(len(palabra)):
        igualdad = 0
        for b in range(len(palabra)):
            if b == s:
                continue
            
            if palabra[s] == palabra[b]:
                igualdad += 1
            
            
        if igualdad == 0:
            return(palabra[s])
                
#ingresar_palabra()

