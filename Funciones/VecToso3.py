#Importacion de librerias 
import numpy as np


def VecToso3(vector):
    """Creacion de una matriz antisimetrica apartir de un vector 
    RETURN: LIST"""

    #Declaracion de variables locales
    vx = vector[0]
    vy = vector[1]
    vz = vector[2]
    
    #Crecion de la matriz asimetrica
    matriz = np.array([[0, -1*vz,vy],
                       [vz,0,-1*vx],
                       [-1*vy,vx,0]])

    
    return matriz
