#Inicializacion de librerias
import numpy as np
from ClassTablaS import *
from MatrixExp6 import *
from MatrixLog6 import *
from adjunta import *



def leer_datos(datos):
    """Lectura de los elementos del archivo"""
    
    #Declaracion de variables locales 
    global tabla
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

def imprimir(matriz):
    """Impresion de una matriz"""
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],end=" ")
        print()

#Definicion de varaibles globales
tabla= TablaS()

semilla =[]
xyz = []
ev = 0
ew=0
Tsb =[]
M= []
contador = 0 #Contador de iteraciones

#Lectura de los datos 

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



#Poner un tope de bucle de 50 veces para evitar bucles infinitos
while True:
    #Calculo de la matriz T
    Tsb=np.identity(4)
    tam= tabla.tamano()

    for i in range(0,tam):
        e = np.array(MatrixExp6(tabla.obtener(i,"S"),Semilla[i]))
        Tsb= np.dot(Tsb,e)

    Tsb=np.dot(Tsb,M)
    
    
    #Calculo de la matriz de transformacion de S a D
    Tbd = np.dot(np.linalg.inv(Tsb),Tsd)
    
    if np.trace(Tbd) == 4:
        print("La solucion correcta es la Semilla: ",Semilla)
        break
    
    #Calculamos el vector giro
    Sb,angulo= MatrixLog6(Tbd)
    
    #Calculo de Ss
    Ss= np.dot(Adjunta(Tsb),Sb)
    
    ws= np.array([Ss[0],Ss[1],Ss[2]])
    vs= np.array([Ss[3],Ss[4],Ss[5]])
    
    if np.linalg.norm(ws) > ew and np.linalg.norm(vs) > ev:
        print("La solucion correcta es la matriz de transformacion: ",imprimir(Tbd))
        break
    else: 
        #Calculo de los  siguientes angulos 
        for i in range(0,len(Semilla)):
            jacobiana = crear_Jacobiana(tabla,Semilla)
            angulo = Semilla[i] + np.dot(np.linalg.inv(jacobiana),Ss)
            Semilla[i]=angulo
    