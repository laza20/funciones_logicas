"""
retorna la cadena mas larga sin repetirse de un input
"""

def ingresar_palabras():
    palabra = input("Ingrese la palabra que desea verificar: ")
    resultado = verificar_cadena(palabra)
    print(resultado)


def verificar_cadena(palabra:str):
    conjunto = set()
    mayor_conjunto = set()
    mayor_conteo = 0
    contador = 0
    i = 0
    j = 0
    while i < len(palabra):
        letra = palabra[i]
        if letra in conjunto:
            j += 1
            i = j
            if len(conjunto) > len(mayor_conjunto):
                mayor_conteo, contador, mayor_conjunto = _actualizar_conjunto(
                    contador, mayor_conjunto, conjunto)
        else: 
            contador += 1
            conjunto.add(letra)
            
        if len(palabra)  == i + 1 and len(conjunto) > len(mayor_conjunto):
            mayor_conteo, contador, mayor_conjunto = _actualizar_conjunto(
                contador, mayor_conjunto, conjunto)
        i += 1
        
    return mayor_conteo
        
def _actualizar_conjunto(contador:int, mayor_conjunto:set, conjunto:set):
    mayor_conteo = contador
    mayor_conjunto = conjunto
    contador = 0
    return mayor_conteo, contador, mayor_conjunto

        
ingresar_palabras()