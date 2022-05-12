#Inicializacion de librerias
import numpy as np 

def se3ToVec(matriz):
    """Calculo del vector giro apartir de la matriz 
    RETUR: LIST"""

    #Inicializacion de variables locales
    wx=matriz[2][1]
    wy=matriz[0][2]
    wz=matriz[1][0]
    vx=matriz[0][3]
    vy=matriz[1][3]
    vz=matriz[2][3]

    #Calculo
    vector = np.array([wx,wy,wz,vx,vy,vz])

    return vector