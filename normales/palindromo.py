"""
🏋️‍♂️ Ejercicio 6: Validar Palíndromo considerando caracteres alfanuméricos (LeetCode Easy)
El EnunciadoSe te va a dar un string s. 
Debes determinar si es un palíndromo (se lee igual al derecho y al revés).
La dificultad: 1. El string puede tener mayúsculas, minúsculas, espacios y signos de puntuación 
(como comas, puntos, etc.).
2. Para saber si es palíndromo, debes ignorar los espacios y los signos de puntuación, 
y no debes hacer diferencia entre mayúsculas y minúsculas.
3. Regla de oro de la entrevista: No debes crear un nuevo string "limpio" usando memoria extra 
O(n). 
Debes resolverlo comparando los caracteres directamente sobre el string original usando dos punteros.
Ejemplos:
Entrada: s = "A man, a plan, a canal: Panama"
Explicación: Si quitamos las comas, los dos puntos y los espacios, y pasamos todo a minúsculas, 
nos queda "amanaplanacanalpanama". 
Al revés se lee igual.
Salida: True
Entrada: s = "race a car"Explicación: Limpio quedaría "raceacar". 
Al revés se lee "racaecar". 
No son iguales.
Salida: False
"""
from typing import List

def ingresar_frase()->str:
    frase = input("Ingrese la frase que desea contar: ")
        
    return frase


def es_palindromo(frase: str) -> bool:
    i = 0
    j = len(frase) - 1
    
    while i < j:
        if not frase[i].isalnum():
            i += 1
            continue
            
        if not frase[j].isalnum():
            j -= 1
            continue
            
        if frase[i].lower() != frase[j].lower():
            return False
        
        i += 1
        j -= 1
        
    return True

def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total

def inicializar():
    fin_total = 0
    while fin_total != 1:
        frase = ingresar_frase()
        palindromo = es_palindromo(frase)
        print(palindromo)
        fin_total = finaliza()
        
    
    
inicializar()
