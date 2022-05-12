#Importacion de librerias
import numpy as np 

def vecGiro(w,v):
    """Construccion del vector giro
    RETURN:LIST"""
    #Declaracion de variables locales
    w1 = w[0]
    w2 = w[1]
    w3 = w[2]
    v1 = v[0]
    v2 = v[1]
    v3 = v[2]
    
    #Calcualo
    vector = np.array([w1,w2,w3,v1,v2,v3])
    
    return vector