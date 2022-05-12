#Inicializacion de librerias 
import numpy as np
from TransToRp import *
from VecToso3 import *


def Adjunta(T):
    """Representacion de la matriz adjunta de una matriz de transformacion homogenea
    RETURN: LIST"""

    #Declacion de variables locales 
    R, p = TransToRp(T)
    
    Rp= np.dot(VecToso3(p),R)

    #Calculo 
    matriz =  np.array([[R[0][0],R[0][1],R[0][2],0,0,0],
                        [R[1][0],R[1][1],R[1][2],0,0,0],
                        [R[2][0],R[2][1],R[2][2],0,0,0],
                        [Rp[0][0],Rp[0][1],Rp[0][2],R[0][0],R[0][1],R[0][2]],
                        [Rp[1][0],Rp[1][1],Rp[1][2],R[1][0],R[1][1],R[1][2]],
                        [Rp[2][0],Rp[2][1],Rp[2][2],R[2][0],R[2][1],R[2][2]]])
    
    return matriz


