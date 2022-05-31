#Inicializacion de librerias 
import numpy as np 
from MatrixExp6 import *
from MatrixLog3 import *
from VecToso3 import *
from so3ToVec import so3ToVec
from VecToso3 import *

def G_1(w,theta):
    """Calculo de la expresion G-1
    RETURN FLOAT"""
    g = ((1/theta)*np.identity(3)) - ((1/2)* VecToso3(w)) + ((1/theta - 1/2 * (1/np.tan(theta/2)))*np.dot(VecToso3(w),VecToso3(w)))
    return g


def MatrixLog6(T):
    """Calculo de la matriz logaritmo de una matriz de transformacion homogenea
    RETURN: LIST"""
    #Obtencion de la matriz de rotacion de la matriz de transformacion
    R = T[0:3,0:3]
    p = T[0:3,3]
    
    #Obtencion del vector giro
    angulo,w = MatrixLog3(R)
    w = so3ToVec(w)
    v = np.dot(G_1(w,angulo), p) 
    S = np.array([w[0],w[1],w[2],v[0],v[1],v[2]])
    
    
    print(w)
    print(angulo)
    print(v)
    
    return S,angulo



