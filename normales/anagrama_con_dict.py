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
    dict_uno = {}
    dict_dos = {}
    for p_1, p_2 in zip(palabra_uno, palabra_dos):
        if p_1 in dict_uno:
            dict_uno[p_1] += 1
        else:
            dict_uno.update({p_1 : 1})
            
        if p_2 in dict_dos:
            dict_dos[p_2] += 1
        else:
            dict_dos.update({p_2 : 1})
    
    if dict_dos == dict_uno:
        return True
        
    return False
            

resultado = ingresar_palabras()
print(resultado)