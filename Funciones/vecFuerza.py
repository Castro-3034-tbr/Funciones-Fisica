#Incializacion de librerias 
import numpy as np

def vecFuerza(m,f):
    """Calculo del vector Fuerza Espacial 
    RETURN:LIST """
    
    #Declaracion de variables locales
    mx=m[0]
    my=m[1]
    mz=m[2]
    fx=f[0]
    fy=f[1]
    fz=f[2]
    
    #Calculo
    fuerza = np.array(mx,my,mz,fx,fy,fz)
    
    return fuerza