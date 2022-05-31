#Inicializacion de librerias
from matplotlib import projections
import matplotlib.pyplot as plt
from sympy import im
import numpy as np
from Matriz_Jacobiana import *

import matplotlib.cm as cm


def Get6sphere(npoints):
    """Calculo de npoints puntos en 6 dimensiones
    RETURN: LIST"""
    #Defenicion de varaibles locales
    x=[]
    sphere=[]
    
    #Calculo
    for i in range(0,6): 
        x.append(np.random.uniform(-1,1,npoints))
    x=np.array(x)
    for i in range(0,npoints): 
        sphere.append(x[:,i]/np.linalg.norm(x[:,i]))
    
    
    return sphere


#Calculo de varaibles  
J = crear_Jacobiana("datos.csv")
puntos = np.array(Get6sphere(10000))

#Multiplicacion de la matriz jacobiana por las coordenadas
fig = plt.figure()

#Calculo de los vectores giro
giro =[] 
for punto in puntos:
    giro.append(np.dot(J,punto))
giro = np.array(giro)


#Impresion en un grafico 3D
w0= giro[:,0]
w1= giro[:,1]
w2= giro[:,2]
v0= giro[:,3]
v1= giro[:,4]
v2= giro[:,5]


ax=plt.axes(projection='3d')
ax.scatter(w0,w1,w2,c=w0,cmap='hsv')
ax.set_xlabel('X', fontweight ='bold')
ax.set_ylabel('Y', fontweight ='bold')
ax.set_zlabel('Z', fontweight ='bold')
ax.set_title('Elipsoide de Velocidad Angular')

plt.figure()
ax=plt.axes(projection='3d')
ax.scatter(v0,v1,v2,c=v0,cmap='hsv')
ax.set_xlabel('X', fontweight ='bold')
ax.set_ylabel('Y', fontweight ='bold')
ax.set_zlabel('Z', fontweight ='bold')
ax.set_title('Elipsoide de Velocidad Lineal')
plt.show()
