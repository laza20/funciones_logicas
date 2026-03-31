"""
Imagina que estás en la terminal de Linux o Mac y tienes una ruta de carpetas. Tu objetivo es "simplificar" esa ruta.
Te van a dar un string que representa una ruta absoluta. En estas rutas:
Un punto solo . significa "el directorio actual" (no hace nada).
Dos puntos seguidos .. significa "subir un nivel" (volver a la carpeta anterior).
Las barras / separan las carpetas. Varias barras seguidas /// se deben tratar como una sola barra /.
Debes devolver la ruta simplificada que:
Siempre empiece con una sola barra /.
No termine en / (a menos que sea la raíz /).
No contenga . ni .. en el resultado final.
Ejemplos:
Entrada: "/home/" ➡️ Salida: "/home" (Le quitamos la barra del final).
Entrada: "/home//foo/" ➡️ Salida: "/home/foo" (Ignoramos la doble barra).
Entrada: "/a/./b/../../c/" ➡️ Salida: "/c"
Explicación a mano: Vamos a a. El . no hace nada. Vamos a b. El primer .. nos saca de b. El segundo .. nos saca de a (estamos en la raíz). Luego entramos a c.
"""

def ingresar_frase():
    return input("Ingrese la frase a verificar: ")


def simplificar_ruta(path: str) -> str:
    lista_path = path.split("/")
    stack = []
    for l in lista_path:
        
        if l == ".." and len(lista_path) != 0:
            stack.pop()
            continue     
        
        if l != "" and l != ".":
            stack.append(l)
        
    
    return "/" + "/".join(stack)
    
    
def inicializar():
    frase = ingresar_frase()
    resultado = simplificar_ruta(frase)
    print(resultado)


inicializar()