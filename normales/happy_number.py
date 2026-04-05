
"""
Ejercicio 10: El problema de la Vida Infinita o "Happy Number" (LeetCode Easy)
Te van a dar un número entero positivo n. 
Tu objetivo es determinar si ese número es un Número Feliz (Happy Number).
¿Cómo se sabe si un número es feliz?
Reemplazas el número por la suma de los cuadrados de sus dígitos.Repites el proceso.
Si en algún momento el resultado llega a ser 1, el número es feliz y el proceso se detiene.
Si el proceso entra en un bucle infinito que nunca llega a 1, el número no es feliz.
Devuelve True si el número es feliz, y False si no lo es.
Ejemplo 1:
Entrada: n = 19
Proceso:1^2 + 9^2 = 1 + 81 = 82
8^2 + 2^2 = 64 + 4 = 68
6^2 + 8^2 = 36 + 64 = 100
1^2 + 0^2 + 0^2 = 1 + 0 + 0 = 1
¡Llegamos al 1! Salida: True
Ejemplo 2:
Entrada: 
n = 2
Proceso: Si empiezas con 2, 
la secuencia te llevará a 4, 16, 37, 58, 89, 145, 42, 20, y de vuelta al 4... 
¡Nunca llegará a $1$ y se quedará dando vueltas para siempre!
Salida: False
"""

def ingresar_numero()->int:
    return (int(input("Ingrese el numero a verificar: ")))


def buscar_numero_feliz(numero:int)->bool:   
    resultados = set()
    feliz = numero
    while feliz != 1:
        if feliz > 9:
            digitos = [int(d) for d in str(feliz)]
            feliz = sum(d ** 2 for d in digitos)
        else:
            feliz = feliz * feliz
        
        if feliz in resultados:
            return False
        
        resultados.add(feliz)
        
    return True
        
        
def finaliza():
    fin_total = int(input("Si desea finalizar la prueba ingrese 1, caso contrario ingrese otro numero: "))
    return fin_total



def inicializar():
    fin_total = 0
    while fin_total != 1:
        print(f"True: Numero feliz, False: numero no feliz")
        numero = ingresar_numero()
        feliz = buscar_numero_feliz(numero)
        print(f"Resultado del numero: {numero} es : {feliz}")
        fin_total = finaliza()
        
inicializar()


