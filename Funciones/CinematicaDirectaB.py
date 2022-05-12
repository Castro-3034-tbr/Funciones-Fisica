#Inicializacion de librerias 
import numpy as np 
from MatrixExp6 import *

def Crear_M():
    """Peticion de las cordenadas de una matriz de 3x3
    RETURN: LIST"""
    print("Peticion de la matriz M")
    # Declaracion de variables
    M= [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    #Peticion de las cordenadas de la matriz
    try:
        for i in range(0,4):
            for j in range(0,4):
                M[i][i] = float(input("Cordenada "+str(i+1)+" "+str(j+1)+": "))
    
        return M
    except :
        print("Error en la creacion de la matriz")

def pedir_angulos(tamaño):
    """Peticion de los angulos para cada alticulacion 
    RETURN : LIST"""
    
    #Declaracion de variables
    theta= []
    
    for i in range(0,tamaño):
        theta.append(np.deg2rad(float(input("Angulo "+str(i+1)+": "))))
    
    return theta


def Crear_Bmatrix(tamaño):
    """Creacion de una matriz la cual cuenta con los ejes elicoidales
    RETURN:LIST"""
    #Declaracion de variables
    
    try:
        
        Smatrix = []
        
        for i in range(0,tamaño):
            temporal = []
            print("Eje "+str(i+1))
            for j in range(0,6):
                temporal.append(float(input("--> ")))
        
            Smatrix.append(temporal)
        
        return Smatrix
    except:
        print("Error en la creacion de la matriz")

#Peticion de elementos por terminal 
try:
    M = Crear_M()
    tamaño = int(input("Numero de articulaciones: "))
    theta = pedir_angulos(tamaño)
    Bmatriz = np.array(Crear_Bmatrix(tamaño))

except:
    print("Error en la peticion de datos")


#Creacion de ma matriz transformacion 
T = np.array([[0,0,0,0]]*4)

T=np.dot(M,MatrixExp6(Bmatriz[0],theta[0]))

for i in range(1,tamaño):
    T= np.dot(T,MatrixExp6(Bmatriz[i],theta[i]))

print(T)

