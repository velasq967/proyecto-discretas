"""
Discrete Mathematics and Its Applications
---------------------------------------------------
Members: Santiago Angulo, Samuel Velasquez, Emerson Perea
Class: A
"""
import math

def main():
    Continuar = True
    while Continuar:
        print("Selecciona lo que quieres hacer: \n" \
        "1) Evaluar caso(s)\n"\
        "2) Salir \n")
        Opcion = int(input("ingresa un numero:"))
        if Opcion == 2:
            Continuar = False
            break
        elif Opcion == 1:
            Valid = False
            while Valid == False:
                Casos = int(input("cuandos casos quieres evaluar? (1- 1000) \n"))
                if Casos <= 1000:
                    Valid = True
                    break
                else:
                    print("input no valido, digite de nuevo\n")
            

            for i in range(Casos):
                N = int(input("ingresa el tamaño del tablero (recuerda colocar un numero entre el 1 y el 25)\n"))
                Queens = []
                if N >= 1 and N <= 25:
                    for j in range(N):
                        print("ingrese las coordenadas de la reina #", j+1 ,"\n(digite X: -1 y Y: -1 para terminar las reinas)\n")
                        Valid = False
                        End_case = False
                        while Valid == False:
                            CoordenadaX = int(input("ingresa la coordenada X: \n"))
                            CoordenadaY = int(input("ingresa la coordenada Y: \n"))
                            if (CoordenadaX <= N and CoordenadaX >= 0) and (CoordenadaY <= N and CoordenadaY >= 0):
                                Valid = True
                                break
                            elif CoordenadaX == -1 and CoordenadaY == -1:
                                Valid = True
                                End_case = True
                            else:
                                print("este input no es valido, intente otra vez")
                        #Coordenadas_input = int(input("Recuerda introducir dos numeros enteros separados por una coma y un espacio (ej: 1, 1)"))
                        #Coordenadas = Coordenadas_input.split(", ")
                        if End_case == True:
                            break
<<<<<<< HEAD
<<<<<<< HEAD
                        if CoordenadaX >= 1 and CoordenadaY >= 1:
                            Queenj_coords = [CoordenadaX, CoordenadaY]
                            Queens.append(Queenj_coords)
                        print(Queens)
=======
=======
>>>>>>> 3b832ad24cf5eef38bac06cccb0358f929e5d172
                        if CoordenadaX >= 0 and CoordenadaY >= 0:
                            queenj_coords = [CoordenadaX, CoordenadaY]
                            queens.append(queenj_coords)
                        print(queens)
                        
                    nQueens_result = nQueens(queens)
                    print (nQueens_result)   
                    
<<<<<<< HEAD
>>>>>>> 3b832ad24cf5eef38bac06cccb0358f929e5d172
=======
>>>>>>> 3b832ad24cf5eef38bac06cccb0358f929e5d172
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

<<<<<<< HEAD
def configurations(N):
=======
def configurations():
>>>>>>> 3b832ad24cf5eef38bac06cccb0358f929e5d172
    """
    funcion que evalua cuantas posibles configuraciones (subconjuntos) 

    parametros:
    N: numero entero que representa el tamaño del tablero

    """
    return (N**(2*N))
    
print(configurations(8))
main()