#Inicializacion de librerias
from ClassTablaS import *
import numpy as np
from MatrixExp6 import *

def leer_archivo(datos):
    """Lectura de los elementos del archivo"""
    
    #Declaracion de variables locales 
    global tabla,angulos
    contador = 0
    
    #Lectura de los archivos
    datos = open(datos, 'r')
    lineas = datos.readlines()
    
    #Lectura de los valores de las articulaciones
    while contador < len(lineas):
        linea = lineas[contador]
        temporal = linea.split(",")
        if temporal[0] == "Articulaciones":
            contador += 1
            while temporal[0] != "\n":
                
                w = [0,0,0]
                q = [0,0,0]
                linea = lineas[contador]
                art = linea.split(",")
                if temporal[0] == "Prismatica":
                    print(art[0])
                    v = [float(art[1]),float(art[2]),float(art[3])]
                    tabla.agregar_prismatica(v)
                else:
                    w = [float(art[0]),float(art[1]),float(art[2])]
                    q = [float(art[3]),float(art[4]),float(art[5])]
                    tabla.agregar(w,q)
                
                contador += 1
                temporal = lineas[contador].split(",")
            
            
        elif temporal[0] == "Angulos":
            contador += 1
            while contador < len(lineas):
                linea = lineas[contador]
                temporal = linea.split(",")
                angulos.append(float(temporal[0]))
                contador += 1
        else:
            contador += 1
        
    datos.close()


#Creacion de variables  
tabla = TablaS()
archivo = "datos.csv"
M = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
angulos = []


#Leer los elementos del archivo 
leer_archivo(archivo)


#Calculo de la cinematica directa
T=np.identity(4)
tam= tabla.tamano()

for i in range(0,tam):
    e = np.array(MatrixExp6(tabla.obtener(i,"S"),angulos[i]))
    T= np.dot(T,e)

T=np.dot(T,M)

#Impresion de la matriz T
print("La matriz T es:")
for i in range(0,4):
    for j in range(0,4):
        print(round(T[i][j],0),end="   ")
    print("")