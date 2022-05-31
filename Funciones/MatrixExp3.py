#Importacion de librerias
import numpy as np
from VecToso3 import *
from rotV import *

def MatrixExp3(vector, angulo):
    """Calculo e la matriz exponencial para la rotacion correspodiente a un determinado eje unitario W y un angulo
    RETURN: LIST"""
    
    #Calculo de variables locales
    seno = np.sin(angulo)
    coseno = np.cos(angulo)
    asimetrica = VecToso3(vector)
    asimetrica2 = np.dot(asimetrica,asimetrica)
    
    #Calculo de la matriz
    matriz_rotacion =np.identity(3) + (seno*asimetrica) + np.dot((1-coseno),asimetrica2)   

    return matriz_rotacion
    

