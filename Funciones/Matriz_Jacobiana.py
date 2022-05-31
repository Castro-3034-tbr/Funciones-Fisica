#Inicializacion de librerias
from ClassTablaS import *
import numpy as np
from MatrixExp6 import *
from adjunta import *


def leer_archivo(datos,tabla,angulos):
    """Lectura de los elementos del archivo"""
    
    #Declaracion de variables locales 
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


def crear_T(i,angulos,tabla):
    """Creacion de la matriz T
    RETURN: LIST"""
    #Declaracion de variables locales
    T = np.identity(4)
    
    #Calculo
    for j in range(0,i):
        e = MatrixExp6(tabla.obtener(j,"S"),angulos[j])
        T = np.dot(T,e)
    
    return T

def transformar(lista):
    
    temp=[]
    for i in lista:
        temp.append([i])
    
    return temp

def crear_Jacobiana(nombre_archivo):
    """Creacion de la matriz Jacobiana
    RETURN: LIST"""
    
    
    #Definicion de variables locales
    #Creacion de variables  
    tabla = TablaS()
    angulos = []
    
    #Leer los elementos del archivo 
    leer_archivo(nombre_archivo,tabla,angulos)
    
    Ji= list(tabla.obtener(0,"S"))
    J =np.array([[Ji[0]],[Ji[1]],[Ji[2]],[Ji[3]],[Ji[4]],[Ji[5]]])
    tam = tabla.tamano()
    #Creacion de la matriz
    for i in range(1,tam+1):
        Si = tabla.obtener(i,"S")
        T = crear_T(i,angulos,tabla)
        AdT = Adjunta(T)
        JI = np.dot(AdT,Si)
        JI = transformar(JI)
        J = np.append(J,JI,axis=1)
    
    return J


if __name__ == "__main__":
    J = crear_Jacobiana("datos.csv")

    #Impresion de la matriz Jacobiana
    print(J)