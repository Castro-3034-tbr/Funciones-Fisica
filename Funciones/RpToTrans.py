#Importacion de librerias
import numpy as np

def RpToTrans(matriz, posicion):
    """Creacion de la matriz de transformacion homogenena
    RETURN: LIST"""
    
    #Declaracion de variables locales 
    r11= matriz[0][0]
    r12 = matriz[0][1]
    r13 = matriz[0][2]
    r21 = matriz[1][0]
    r22= matriz[1][1]
    r23 = matriz[1][2]
    r31 = matriz[2][0]
    r32 = matriz[2][1]
    r33 = matriz[2][2]
    
    px = posicion[0]
    py = posicion[1]
    pz = posicion[2]
    
    matriz=np.array[[r11, r12, r13, px],
                    [r21, r22, r23, py],
                    [r31, r32, r33, pz],
                    [0,    0,   0,  1 ]]
    
    return matriz

