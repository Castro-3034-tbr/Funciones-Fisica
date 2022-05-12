
#Inacializamos las librerias
import numpy as np

def RotV(v,theta):
    """Cracion de la matriz generica de rotacion de un angulo theta entorni a cualquier eje
    RETURN: LISTA"""

    #Creamos la matriz
    c = np.cos(theta)
    s = np.sin(theta)
    vx = v[0]
    vy = v[1]
    vz = v[2]

    matriz =np.array([[c+vx*vx*(1-c), vx*vy*(1-c)-vz*s, vx*vz*(1-c)+vy*s],
                      [vy*vx*(1-c)+vz*s ,c+vy*vy*(1-c),vy*vz*(1-c)-vx*s],
                      [vx*vz*(1-c)-vy*s, vy*vz*(1-c)+vx*s, c+vz*vz*(1-c)]])

    return matriz