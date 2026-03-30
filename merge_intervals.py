"""
Dado un array de intervalos devolver los intervalos convinados.
ej:
intervals = [[1,3],[2,6],[8,10],[15,18]]
devolver los intervalos combinados:
[[1,6],[8,10],[15,18]]
"""

from typing import List, Dict

def ingresar_intervalos()->List:
    fin = 0
    lista_intervalos = []
    lista_intermedia = []
    while fin != 1:
        lista_intermedia = []
        while len(lista_intermedia) < 2:
            lista_intermedia.append(int(input("Agrege numeros al intervalo: ")))
        lista_intervalos.append(lista_intermedia)
        fin = int(input("Si desea finalizar la carga ingrese 1, en caso contrario presione otro numero: "))    
        
    
    return lista_intervalos


def convinar_intervalos(lista_intervalos:List[List])->int:
    lista_intervalos.sort(key=lambda x: x[0])
    intervalos_convinados = [lista_intervalos[0]]
    for i, j in lista_intervalos[1:]:
        ultimo = intervalos_convinados[-1][1]
        if i <= ultimo:
            intervalos_convinados[-1][1] = j
        else:
            intervalos_convinados.append([i,j])
        

    return intervalos_convinados

    
def mostrar(lista_intervalos:List[List], intervalos_convinados:List[List], tanda:int):
    print(f"La lista inicial es: {lista_intervalos}\nLa lista de los intervalos convinados: {intervalos_convinados}\nEsta es la prueba numero {tanda}.")
    
def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total
    
def contacto_con_usuario():
    lista_intervalos = ingresar_intervalos()
    return lista_intervalos

def computo(lista_intervalos:List[List])->List[List]:
    intervalos_convinados = convinar_intervalos(lista_intervalos)
    return intervalos_convinados

def resultado(lista_intervalos:List[List], intervalos_convinados:List[List], tanda:int):
    mostrar(lista_intervalos, intervalos_convinados, tanda)
    
def inicializar():
    fin_total = 0
    tanda = 1
    while fin_total != 1:
        lista_intervalos = contacto_con_usuario()
        intervalos_convinados = computo(lista_intervalos)
        resultado(lista_intervalos, intervalos_convinados, tanda)
        fin_total = finaliza()
        tanda += 1
        
    
    
inicializar()