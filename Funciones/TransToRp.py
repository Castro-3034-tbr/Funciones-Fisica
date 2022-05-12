#Incializacion de librerias
import numpy as np

def TransToRp(T):
    """Conversion de una matriz de transformacion homogenea en una matriz de rotacion y en un vector posición
    RETURN: LIST"""
    
    #Declaracion de variables locales
    r11= T[0][0]
    r12 = T[0][1]
    r13 = T[0][2]
    r21 = T[1][0]
    r22= T[1][1]
    r23 = T[1][2]
    r31 = T[2][0]
    r32 = T[2][1]
    r33 = T[2][2]
    
    px = T[0][3]
    py = T[1][3]
    pz = T[2][3]

    #Calculo
    matriz=np.array([[r11, r12, r13],
                    [r21, r22, r23],
                    [r31, r32, r33]])
    
    vector =  np.array([px,py,pz])

    return matriz, vector

