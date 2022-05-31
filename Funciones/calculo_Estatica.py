import numpy as np
from Matriz_Jacobiana import *


def calulo_torque(J,f):
    """ Calculo del torque en una articuacion mediante la matriz jacobiana
    RETURN: LIST """
    
    t = np.dot(np.transpose(J),f)
    
    return t


def calculo_fuerza(J,t):
    """Calculo de las fuerzas en una alticulacion mediante la matriz jacobiana
    RETURN: LIST"""
    
    inv = np.linalg.pinv(J)
    transpuesta = np.array(np.transpose(inv))
    print(transpuesta)
    
    f= np.dot(transpuesta,t)
    
    return f


def calculo_momento(f,d):
    """Calculo del momento de una fuerza en un eslabon 
    RETURN: FLOAT """
    
    M= f*d
    
    return M

J=crear_Jacobiana("datos.csv")
f = np.array([[1],[1],[1],[1],[1],[1]])
t = calulo_torque(J,f)


f1= calculo_fuerza(J,t)
for i in range(0,6):
    print("Articulacion: ",i," Fuerza: ",f1[i][0])

