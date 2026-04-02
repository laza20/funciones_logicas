from typing import List

def carga_interna(lista:str)->List[List[int]]:
        lista_retorno = []
        fin_actual = 0
        while fin_actual != 1:
            lista_numeros = []
            lista_numeros.append(int(input(f"Ingrese el numero que desea añadir a la {lista}: ")))
            fin_actual = int(input("Si desea finalizar la carga de esta lista ingrese 1, en caso contrario presione otro numero: "))   
            lista_retorno.append(lista_numeros)
        
        return lista_retorno

def ingresar_tamaño()->List[List[int]]:
    lista_uno = carga_interna("primer lista") 
    lista_dos = carga_interna("segunda lista") 
    return lista_uno, lista_dos

def sumar_listas(lista_uno:List[List[int]], lista_dos:List[List[int]])->List[int]:
        if len(lista_uno) > len(lista_dos):
            tamaño = len(lista_uno)
        else:
            tamaño = len(lista_dos)
        suma = 0
        resto = 0
        lista_suma = []
        i = 0
        while i < tamaño:
            valor1 = lista_uno[i][0] if i < len(lista_uno) else 0
            valor2 = lista_dos[i][0] if i < len(lista_dos) else 0
            suma = valor1 + valor2 + resto
            if suma >= 10:
                digitos = [int(d) for d in str(suma)]
                lista_suma.append(digitos[1])
                resto = digitos[0]
            else:
                lista_suma.append(suma)
                resto = 0
                
            i += 1
            
        if resto != 0:
            lista_suma.append(resto)

        return lista_suma
            
        
        

def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total
    
def inicializar():
    fin_total = 0
    while fin_total != 1:
        lista_uno, lista_dos = ingresar_tamaño()
        lista_retorno = sumar_listas(lista_uno, lista_dos)
        print(lista_retorno)
        fin_total = finaliza()
        
inicializar()