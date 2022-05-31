#Inicializacion de librerias 
import numpy as np 
import math as m
from VecToso3 import *
from MatrixExp3 import *

def MatrixExp6(S,theta):
    """Calculo de la matriz exponencial de un vector giro en representacion matricial 
    RETURN: LIST"""
    
    #Declaracion de variables locales
    w= [S[0],S[1],S[2]]
    v = [S[3],S[4],S[5]]
    
    modulow = np.linalg.norm(w)
    moduloV = np.linalg.norm(v)

    
    #Calculo de la matriz exponencial
    if modulow ==1:
        e = MatrixExp3(w,theta)
        vo = np.dot((np.identity(3)*theta)+((1-np.cos(theta))*VecToso3(w))+ (theta-np.sin(theta))*np.dot(VecToso3(w),VecToso3(w)),v)
        matriz = np.array([[e[0][0],e[0][1],e[0][2],vo[0]],
                           [e[1][0],e[1][1],e[1][2],vo[1]],
                           [e[2][0],e[2][1],e[2][2],vo[2]],
                           [0,0,0,1]])
    
    elif modulow == 0 and moduloV == 1:
        matriz = np.array([[1,0,0,v[0]*theta],[0,1,0,v[1]*theta],[0,0,1,v[2]*theta],[0,0,0,1]])
    
    return matriz

