"""
Discrete Mathematics and Its Applications
---------------------------------------------------
Members: Santiago Angulo, Samuel Velasquez, Emerson Perea
Class: A
"""

def main():
    continuar = True
    while continuar:
        print("Selecciona lo que quieres hacer: \n" \
        "1) Evaluar caso(s)\n"\
        "2) Salir \n")
        opcion = int(input("ingresa un numero:"))
        if opcion == 2:
            continuar = False
            break
        elif opcion == 1:
            valid = False
            while valid == False:
                casos = int(input("cuandos casos quieres evaluar? (1- 1000) \n"))
                if casos <= 1000:
                    valid = True
                    break
                else:
                    print("input no valido, digite de nuevo\n")
            

            for i in range(casos):
                N = int(input("ingresa el tamaño del tablero (recuerda colocar un numero entre el 1 y el 25)\n"))
                queens = []
                if N >= 1 and N <= 25:
                    for j in range(N):
                        print("ingrese las coordenadas de la reina #", j+1 ,"\n(digite X: -1 y Y: -1 para terminar las reinas)\n")
                        valid = False
                        end_case = False
                        while valid == False:
                            CoordenadaX = int(input("ingresa la coordenada X: \n"))
                            CoordenadaY = int(input("ingresa la coordenada Y: \n"))
                            if (CoordenadaX <= N and CoordenadaX >= 0) and (CoordenadaY <= N and CoordenadaY >= 0):
                                valid = True
                                break
                            elif CoordenadaX == -1 and CoordenadaY == -1:
                                valid = True
                                end_case = True
                            else:
                                print("este input no es valido, intente otra vez")
                        #Coordenadas_input = int(input("Recuerda introducir dos numeros enteros separados por una coma y un espacio (ej: 1, 1)"))
                        #Coordenadas = Coordenadas_input.split(", ")
                        if end_case == True:
                            break
                        if CoordenadaX >= 0 and CoordenadaY >= 0:
                            queenj_coords = [CoordenadaX, CoordenadaY]
                            queens.append(queenj_coords)
                        print(queens)
                        
                    nQueens_result = nQueens(queens)
                    print (nQueens_result)   
                    
                else:
                    print("input invalido, repita porfavor")
                       
                        

def nQueens(Lista_Coords):
    """
    Funcion que determina si una configuracion de N reinas en un tablero N x N es valida
    Retorna True si ninguna reina amenaza a otra, False en caso contrario
    
    Parametros:
    Lista_Coords: lista de coordenadas [x,y] de las reinas
    """
    reinas = [(coordenada[0], coordenada[1]) for coordenada in Lista_Coords]
    
    for i in range(len(reinas)):
        x1, y1 = reinas[i]
        for j in range(i + 1, len(reinas)):
            x2, y2 = reinas[j]
            
            if x1 == x2:
                print("La configuración no es válida")
                return False
            
            if y1 == y2:
                print("La configuración no es válida")
                return False
            
            if abs(x1 - x2) == abs(y1 - y2):
                print("La configuración no es válida")
                return False
    
            print("La configuración es válida")
    
        return True
    
    
    return True

def configurations():
    """
    funcion que evalua cuantas posibles configuraciones (subconjuntos) 
    """
    #TODO
    pass

main()