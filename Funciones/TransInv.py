#Iinicializacion de librerias
import numpy as np
from TransToRp import *

def TransInv(T):
    """Calculo de la matriz inversa de una matriz de transformacion homogenea
    RETURN :LIST"""
    
    #Declacion de variables locales 
    R, p = TransToRp(T)
    RT = R.T
    RTp= np.dot((-1*RT),p)

    #Calculo 
    matriz =  np.array([[RT[0][0],RT[0][1],RT[0][2],RTp[0]],
                        [RT[1][0],RT[1][1],RT[1][2],RTp[1]],
                        [RT[2][0],RT[2][1],RT[2][2],RTp[2]],
                        [0,0,0,1]])
    
    return matriz
