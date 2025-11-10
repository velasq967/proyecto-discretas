"""
Discrete Mathematics and Its Applications
---------------------------------------------------
Members: Santiago Angulo, Samuel Velasquez, Emerson Perea
Class: A
"""
import math

def main():
    global Queens
    Casos = int(input())
    for i in range(Casos):
        N = int(input())
        Queens = []
        if N >= 1 and N <= 25:
            for j in range(N):
                Valid = False
                End_case = False
                while Valid == False:
                    Coordenadas_input = input()
                    Coordenadas = Coordenadas_input.split(", ")
                    CoordenadaX = int(Coordenadas[0])
                    CoordenadaY = int(Coordenadas[1])
                    if (CoordenadaX <= N and CoordenadaX >= 0) and (CoordenadaY <= N and CoordenadaY >= 0):
                        Valid = True
                        break
                    elif CoordenadaX == -1 and CoordenadaY == -1:
                        Valid = True
                        End_case = True
                    else:
                        print("este input no es valido, intente otra vez")
                if End_case == True:
                    break
                if CoordenadaX >= 0 and CoordenadaY >= 0:
                    Queenj_coords = [CoordenadaX, CoordenadaY]
                    Queens.append(Queenj_coords)

            nQueens_result = nQueens(Queens)
            print(f"case {i+1}:")
            print(f"Satisfies {N} - Queen(s) problem? -> {nQueens_result}")
            print(f"Posible configurations for {len(Queens)}-queen(s):", configurations(len(Queens)))
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
            
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return False
            
    return True

def configurations(N):
    """
    funcion que evalua cuantas posibles configuraciones (subconjuntos) 

    parametros:
    N: numero entero que representa el tamaño del tablero

    """
    n = N*N
    config_totales = math.comb(n, N)
    if config_totales > 10**10:
        Config_totales = sn_format(config_totales)
        return (Config_totales)
    else:
        return (config_totales)
    
def sn_format(number):
    """
    Funcion que convierte un numero a notacion cientifica

    Parametros:
    number: numero entero o flotante a convertir
    """
    signo = "-" if number < 0 else ""
    n_abs = abs(number)
    e = math.floor(math.log10(n_abs))
    mantisa_int = round(n_abs / 10**(e - 4)) # keeps first 5 digits
    mantisa_str = str(mantisa_int)
    if len(mantisa_str) > 5:
        mantisa_str = mantisa_str[:5]
        e += 1
    return f"{signo}{mantisa_str[0]}.{mantisa_str[1:]} x 10^{e}"

main()