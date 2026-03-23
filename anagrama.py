"""
Devolver True si son anagramas (mismas letras, distinto orden).
"""
def ingresar_palabras():
    palabra_uno = input("Ingrese la primer palabra que desea verificar: ")
    palabra_dos = input("Ingrese la segunda palabra que desea verificar: ")
    if len(palabra_dos) != len(palabra_uno):
        return False
    resultado = verificar_anagrama(palabra_uno, palabra_dos)
    return resultado
    
    
def verificar_anagrama(palabra_uno:str, palabra_dos:str)->True:
    coincidencias = 0
    lista_dos = list(palabra_dos)
    for p_1 in range(len(palabra_uno)):
        if palabra_uno[p_1] in lista_dos:
            coincidencias += 1
            lista_dos.remove(palabra_uno[p_1])
                
    if coincidencias == len(palabra_uno):
        return True
    
    return False

resultado = ingresar_palabras()
print(resultado)