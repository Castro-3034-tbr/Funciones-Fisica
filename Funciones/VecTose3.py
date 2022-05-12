#Iinicializacion de librerias
import numpy as np

def VecTose3(V):
    """Conversion de un vector giro en una matriz
    RETURN :LIST"""
    
    #Declaracion de variables locales
    wx=V[0]
    wy=V[1]
    wz=V[2]
    vx=V[3]
    vy=V[4]
    vz=V[5]

    #Calculo
    matriz = np.array([[0,-1*wz,wy,vx],
                        [wz,0,-1*wx,vy],
                        [-1*vy,vx,0,vz],
                        [0,0,0,0]])

    return matriz