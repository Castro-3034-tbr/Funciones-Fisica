import sympy as sp
import numpy as np
from ClassTablaS import * 
from funciones_sympy import *

def leer_datos_directa(datos):
    """Lectura de los elementos del archivo"""
    
    #Declaracion de variables locales 
    tabla = TablaS()
    contador = 0
    
    #Lectura de los archivos
    datos = open(datos, 'r')
    lineas = datos.readlines()
    
    #Lectura de los valores de las articulaciones
    while contador < len(lineas):
        linea = lineas[contador]
        art = linea.split(",")
        w = [float(art[0]),float(art[1]),float(art[2])]
        q = [float(art[3]),float(art[4]),float(art[5])]
        tabla.agregar(w,q)
        contador += 1
        
    datos.close()
    return tabla



def main():
    #Lectura de datos
    semilla = np.array([0.1,0.1,0.1,0.1,0.1,0.1])
    thetalist = np.array(semilla).copy()
    
    xyz = np.array([0.193, 0.143, 0.344])
    
    L=np.array([103.0, 80.0, 210.0, 30.0, 41.5, 180.0, 23.7, -5.5])
    M=np.array([[1,0,0,L[6]+L[5]+L[4]],[0,1,0,0],[0,0,1,L[0]+L[1]+L[2]+L[3]+L[7]],[0,0,0,1]])
    
    tabla = leer_datos_directa("datos2.csv")
    
    ew = 10e-6
    ev = 10e-6
    
    
    #Calculo de la matriz de trasnformacion homogenea 
    Tsd = getT_sympy(semilla,xyz)
    print("Calculada la matriz de transformacion homogenea")
    
    #Calculamos la Cinematica directa 
    Tsb = CinematicaDirecta_sympy(M,tabla,thetalist)
    
    #Calculo de la matriz Tbd
    Tbd = np.dot(np.linalg.inv(Tsb),Tsd)
    
    #Calculo del vector Giro 
    Vb = MatrixLog6_sympy(Tbd)
    
    #Calculo del vector giro en {s}
    Vs = np.dot(Adjunta_sympy(Tsb), se3ToVec_sympy(Vb))
    
    #Calculo 
    while  (np.linalg.norm([Vs[0], Vs[1], Vs[2]]) > ew or np.linalg.norm([Vs[3], Vs[4], Vs[5]]) > ev) and contador < 50:
        J = Jacobiana_sympy(tabla,thetalist)
        J=np.array(J.tolist()).astype(np.float64)
        thetalist = thetalist + np.dot(np.linalg.pinv(J), Vs)
        i = i + 1 #Contador de iteraciones
        Tsb = CinematicaDirecta_sympy(M, tabla, thetalist) 
        Vb = MatrixLog6_sympy(np.dot(np.linalg.inv(Tsb), Tsd))  
        Vs = np.dot(Adjunta_sympy(Tsb), se3ToVec_sympy(Vb))
        print (Vs) 
    
    #Reduccion de los angulos para que pertenecan al reguimen de giro
    angulos_limites=[[-3.054,3.054,np.pi],[-1.571,0.6405,np.pi],[-1.396,1.571,np.pi],[-3.054,3.054,np.pi],[-1.745,1.745,np.pi],[-2.574,2.574,np.pi]]

    for i in range(0,len(thetalist)):
        while  thetalist[i]<= angulos_limites[i][0] or thetalist[i]> angulos_limites[i][1]:
            if thetalist[i]> angulos_limites[i][1]:
                thetalist[i]-= angulos_limites[i][2]
            else:
                thetalist[i]+=angulos_limites[i][2]
                

if __name__=="__main__" :
        main()