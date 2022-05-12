#Inicializacion de librerias
from ClassTablaS import *
import numpy as np
from MatrixExp6 import *
from adjunta import *


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


def crear_T(i):
    """Creacion de la matriz T
    RETURN: LIST"""
    #Declaracion de variables locales
    global angulos
    T = np.identity(4)
    
    #Calculo
    for j in range(0,i):
        e = MatrixExp6(tabla.obtener(j,"S"),angulos[j])
        T = np.dot(T,e)
    
    return T

def crear_Jacobiana(tabla):
    """Creacion de la matriz Jacobiana
    RETURN: LIST"""
    
    #Definicion de variables locales
    J = [[tabla.obtener(0,"S")]]
    tam = tabla.tamano()
    
    #Creacion de la matriz
    for i in range(1,tam+1):
        Si = tabla.obtener(i,"S")
        T = crear_T(i)
        AdT = Adjunta(T)
        JI = np.dot(AdT,Si)
        J.append(JI)

    return J

#Creacion de variables  
tabla = TablaS()
archivo = "datos.csv"
angulos = []



#Leer los elementos del archivo 
leer_archivo(archivo)

J = crear_Jacobiana(tabla)

#Impresion de la matriz J
print("Matriz Jacobiana:")
print(J)
