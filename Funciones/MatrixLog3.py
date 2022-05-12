#Iniciailizacion de librerias
import numpy as np 
import math as m

def MatrixLog3(R):
    """Calculo del eje unitario y el angulo de rotacion a partir de una matriz
    RETURN : LIST"""
    
    #Declaracion de variables locales
    traza = np.trace(R)

    #Calculo 
    if traza >= 3:
        angulo = 0
        eje_rotacion = None
        

    elif traza <= -1:
        angulo = m.pi
        radical3 = 2*(1+R[2][2])
        radical2 = 2*(1+R[1][1])
        radical1 = 2*(1+R[0][0])
        if  radical3>= 0 :
            fraccion= 1/(radical3)
            matriz = np.array([R[0][2],R[1][2],1+R[2][2]])
            eje_rotacion = np.dot(fraccion,matriz)
        elif  radical2>= 0 :
            fraccion= 1/(radical2)
            matriz = np.array([R[0][1],1+R[1][1],R[2][1]])
            eje_rotacion = np.dot(fraccion,matriz)
        
        elif  radical1>= 0 :
            fraccion= 1/(radical1)
            matriz = np.array([1+R[0][0],R[1][0],R[2][0]])
            eje_rotacion = np.dot(fraccion,matriz)

        
        

    else:
        angulo = np.arccos(0.5*(traza-1))
        seno= 1/(2*np.sin(angulo))
        R = np.array(R)
        matriz= (R- R.T)
        
        eje_rotacion = np.dot(seno,matriz)
        

    return angulo,eje_rotacion

