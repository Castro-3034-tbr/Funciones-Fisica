#Inacializamos librerias
from Hechos.rotV import *
import numpy as np

def normalizar_vector(vector):
    """Normalizacion de un vecotor
    RETURN:LIST"""
    
    #Calculo del modulo 
    suma = 0
    for i in range(len(vector)):
        suma += vector[i]*vector[i]
    
    modulo = np.sqrt(suma)
    
    #Normalizacion
    for i in range(len(vector)):
        vector[i] = vector[i]/modulo
    
    return vector


def rotacion(vector,eje,angulo):
    """Rotacion de un vector respecto con un eje con un angulo
    RETURN: LIST"""

    #Declaramos variables localas
    eje_normalizado = normalizar_vector(eje)
    matriz_rotacion = RotV(eje_normalizado,angulo)

    #Calculamos el vector rotado
    vector_rotado = np.dot(matriz_rotacion,vector)

    return vector_rotado