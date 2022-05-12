#inicializacion de librerias
import numpy as np
from math import *

def Rotx(theta):
    """Crea ka matriz de rotacion en x 
    RETURN :LIST"""

    #Creacion de la matriz 

    coseno = round(cos(theta),4)
    seno = round(sin(theta),4)
    

    matriz = np.array([[1,0,0],[0,coseno,-1*seno],[0,seno,coseno]])

    return matriz

def Roty(theta):
    """Crea ka matriz de rotacion en y
    RETURN:LIST"""

    #Creacion de la matriz 
    coseno = round(cos(theta),4)
    seno = round(sin(theta),4)

    matriz = np.array([[coseno,0,seno],[0,1,0],[-1*seno,0,coseno]])

    return matriz

def Rotz(theta):
    """Crea ka matriz de rotacion en z 
    RETURN :LIST"""
    #Cracion de la matriz
    coseno = round(cos(theta),4)
    seno = round(sin(theta),4)

    matriz = np.array([[coseno , -1*seno,0],[seno,coseno,0],[0,0,1]])
    return matriz