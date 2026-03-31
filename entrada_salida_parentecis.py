"""
EJERCICIO: “VALID PARENTHESES”
Enunciado
Dada una cadena que contiene solo estos caracteres:
( ) { } [ ]
determinar si la cadena es válida
¿Qué significa válida?
Cada apertura tiene su cierre correspondiente
Se cierran en el orden correcto
"""

def ingresar_frase():
    return input("Ingrese la frase a verificar: ")

def verificador(cadena:str):
    parejas = {
        ")": "(", 
        "]": "[",
        "}": "{"
    }
    stack = []
    for i in cadena:
        if i in ["(", "{", "["]:
            stack.append(i)
        else:
            if not stack or stack[-1] != parejas[i]:
                return False
            stack.pop()
            
    return len(stack) == 0
            


def inicializar():
    frase = ingresar_frase()
    resultado = verificador(frase)
    print(resultado)


inicializar()