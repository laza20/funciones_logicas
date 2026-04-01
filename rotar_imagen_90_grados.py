"""
🏋️‍♂️ Ejercicio 8: Rotar una imagen 90 grados (LeetCode Medium)
Te van a dar una matriz cuadrada de n x n que representa una imagen (donde cada celda es un píxel).
Tu objetivo es rotar la imagen 90 grados en el sentido de las agujas del reloj.
La regla de oro de la entrevista: Tienes que rotar la matriz en el lugar (in-place). 
Esto significa que no puedes crear una nueva matriz vacía para ir copiando los números ahí. 
Tienes que modificar la misma matriz que te dan, usando memoria extra O(1).
Ejemplo:Entrada:
matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
Salida esperada (Rotada 90°):Python[
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
  ]
"""

from typing import List, Dict

def ingresar_tamaño()->List[List[int]]:
    fin_total = 0
    lista_retorno = []
    while fin_total != 1:
        lista_numeros = []
        fin_actual = 0
        while fin_actual != 1:
            lista_numeros.append(int(input("Ingrese el numero que desea añadir a la lista: ")))
            fin_actual = int(input("Si desea finalizar la carga de esta lista ingrese 1, en caso contrario presione otro numero: "))    
        lista_retorno.append(lista_numeros)
        fin_total = int(input("Si desea finalizar la carga ingrese 1, en caso contrario presione otro numero: "))    
        
    return lista_retorno


def invertir(tamaño:List[List[int]])->List[List[int]]:
    n = len(tamaño)
    for i in range(n):
        for j in range(i, n):
            tamaño[i][j], tamaño[j][i] = tamaño[j][i], tamaño[i][j]
            
    for fila in tamaño:
        fila.reverse()
        
        

    
def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total



def inicializar():
    fin_total = 0
    while fin_total != 1:
        tamaño= ingresar_tamaño()
        invertido = invertir(tamaño)
        print(f"Tamaño original: {tamaño}\nTamaño invertido: {invertido}")
        fin_total = finaliza()
        
inicializar()