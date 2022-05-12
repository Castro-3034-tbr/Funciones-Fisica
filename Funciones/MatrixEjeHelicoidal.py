#Incializacion de librerias 
import numpy as np

def MatrixEjeHelicoidal(S):
    """Calculo de la matriz del eje helicoidal
    RETURN:LIST """
    
    #Declaracion de variables locales
    wx = S[0]
    wy = S[1]
    wz= S[2]
    vx=S[3]
    vy=S[4]
    vz=S[5]
    
    #Calculo
    matriz = np.array([[0,-1*wz,wy,vx],[wz,0,-1*wx,vy],[-1*wy,wx,0,vz],[0,0,0,0]])
    
    return matriz
