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
                        if CoordenadaX >= 1 and CoordenadaY >= 1:
                            Queenj_coords = [CoordenadaX, CoordenadaY]
                            Queens.append(Queenj_coords)
                        print(Queens)
                else:
                    print("input invalido, repita porfavor")
                       
                        

def nQueens(Tablero, Queens, Lista_Coords):
    #TODO
    """
    Funcion que determina si una configuracion de N reinas en un tablero N x N es valida

    Parametros: 

    """

    return False

def configurations(N):
    """
    funcion que evalua cuantas posibles configuraciones (subconjuntos) 

    parametros:
    N: numero entero que representa el tamaño del tablero

    """
    return (N**(2*N))
    
print(configurations(8))
main()