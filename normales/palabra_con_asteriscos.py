def palabra_con_ast():
    frase = input("ingrese la frase: ")
    lista_palabras = frase.split()
    palabra_mas_larga = ""
    for l in lista_palabras:
        if len(l) >= len(palabra_mas_larga):
            palabra_mas_larga = l
    
    print("*"*(len(palabra_mas_larga)+4))
    for palabra in lista_palabras:
        diferencia_entre_tamaños = len(palabra_mas_larga) - len(palabra) 
        if diferencia_entre_tamaños != 0:
            dif = (" "*round(diferencia_entre_tamaños))
        else:
            dif = ("")
        print(f"* {palabra} {dif}*")
        
    print("*"*(len(palabra_mas_larga)+4))
palabra_con_ast()
                

            
        