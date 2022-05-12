#Importacion de librerias 
import numpy as np

def so3ToVec(m):
    """Calculo del vector apartir de su matriz antisimetrica
    RETURN:LIST"""
    
    #Declaracion de variables locales
    vx = m[2][1]
    vy = m[0][2]
    vz = m[1][0]
    
    #Calculo
    vector = np.array([vx,vy,vz])
    
    return vector