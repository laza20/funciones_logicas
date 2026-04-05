"""
Ejercicio 9: Fusionar Intervalos de Tiempo (LeetCode Medium)
El Enunciado
Imagínate que estás programando la agenda de una sala de reuniones. Te van a dar una lista de intervalos de tiempo donde cada intervalo es un par de números: [inicio, fin].
Tu objetivo es fusionar (unir) todos los intervalos que se superpongan (que se pisen en el tiempo) y devolver una lista con los intervalos finales completamente limpios.
Ejemplos:
Entrada: intervalos = [[1, 3], [2, 6], [8, 10], [15, 18]]
Salida: [[1, 6], [8, 10], [15, 18]]
Explicación: Como los intervalos [1, 3] y [2, 6] se pisan (la segunda reunión empieza a las 2, antes de que termine la primera a las 3), los unimos en un solo gran intervalo que va desde el 1 hasta el 6. Los demás no se pisan con nadie, así que quedan igual.
Otro ejemplo: intervalos = [[1, 4], [4, 5]]
Salida: [[1, 5]]
Explicación: Se tocan justo en el 4, así que los unimos.
"""

from typing import List, Dict

def ingresar_intervalos()->List[List[int]]:
    fin_total = 0
    lista_retorno = []
    while fin_total != 1:
        lista_numeros = []
        lista_numeros.append(int(input("Ingrese el principio del intervalos: ")))
        lista_numeros.append(int(input("Ingrese el fin del intervalos: ")))
        lista_retorno.append(lista_numeros)
        fin_total = int(input("Si desea finalizar la carga ingrese 1, en caso contrario presione otro numero: "))    
        
    return lista_retorno


def conbinar(intervalos_primarios:List[List[int]])->List[List[int]]:
    if not intervalos_primarios:
        return []
    
    lista_ordenada = sorted(intervalos_primarios)
    intervalos_combinados = []
    for i in lista_ordenada:
        if not intervalos_combinados:
            intervalos_combinados.append(i)
            continue

        if intervalos_combinados[-1][1] >= i[0]:
            intervalos_combinados[-1][1] = max(intervalos_combinados[-1][1], i[1])
        else:
            intervalos_combinados.append(i)
            
    return intervalos_combinados
        
        
def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total



def inicializar():
    fin_total = 0
    while fin_total != 1:
        intervalos_primarios = ingresar_intervalos()
        intervalos_combinados = conbinar(intervalos_primarios)
        print(f"Intervalos convinado: {intervalos_combinados}")
        fin_total = finaliza()
        
inicializar()