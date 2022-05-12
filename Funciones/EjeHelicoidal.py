#Inicializacion de librerias 
import numpy as np 
import math as m

def ejeHelicoidal(w,v):
    """Calculo del eje helicoidal
    RETURN: LIST"""
    
    #Declaracion de variables locales
    modulo = m.magnitude(w)
    w1 = w[0]/modulo
    w2 = w[1]/modulo
    w3 = w[2]/modulo
    v1 = v[0]
    v2 = v[1]
    v3 = v[2]
    
    #Calcualo
    vector = np.array([w1,w2,w3,v1,v2,v3])
    
    return vector

