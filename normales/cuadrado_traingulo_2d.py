
def formar_figura():
    while True:
        contador = 0
        figura = input("ingrese la figura que desea representar: ")
        tamaño = int(input("ingrese el tamaño de la figura: "))
        
        if figura.lower() == "cuadrado":
            print("*"*tamaño)
            tamaño_vertical = tamaño - 2
            espacio = tamaño_vertical - 2
            for t in range(tamaño_vertical):
                print("*"," "*espacio,"*")
            print("*"*tamaño)
            contador = 1
            
        if figura.lower() == "triangulo":
            print("*"*tamaño)
            espacio = 1
            tamaño_interno = tamaño - espacio * 2
            for t in range(tamaño-2):
                print(" "*(espacio-1), "*"*tamaño_interno, " "*espacio)
                espacio += 1
                contador_interno = t
                
                if tamaño_interno == 1:
                    break
                
                if tamaño_interno != 1:
                    tamaño_interno = tamaño - espacio * 2
                    
                if tamaño / 2 == t:
                    tamaño_interno = 1
                    contador_interno += 1
            
        if contador == 0:
            print("No se ingreso una opcion valida")
        
            
        fin = figura = input("Desea finalizar (SI/NO): ")
        if fin.upper() == "SI":
            break







formar_figura()