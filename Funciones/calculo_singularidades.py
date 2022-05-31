#Inicializacion de librerias 
import numpy as np
import sympy as sp 
from ClassTablaS import *
from funciones_sympy import *


def leer_archivo(datos,tabla):
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
        
        w = [0,0,0]
        q = [0,0,0]
        linea = lineas[contador]
        art = linea.split(",")
        if temporal[0] == "Prismatica":
            v = [float(art[1]),float(art[2]),float(art[3])]
            tabla.agregar_prismatica(v)
        else:
            w = np.array([float(art[0]),float(art[1]),float(art[2])])
            q = np.array([float(art[3]),float(art[4]),float(art[5])])
            tabla.agregar(w,q)
            
        contador += 1
    
    print("Datos leidos")
    datos.close()



#Definimos variables locales
tabla = TablaS()
leer_archivo("datos2.csv",tabla)
t = sp.symbols("t0, t1, t2, t3, t4, t5")

#Calculo de la matriz R
R = getR_sympy(tabla,t)
print("Calculado R")

#Aplicamos rotaciones a los vectores 
qs=[]
ws=[]
Ri=R[0]

qs.append(sp.Matrix(tabla.obtener(0,"Q")))
ws.append(sp.Matrix(tabla.obtener(0,"W")))

for i in range(1,6):
    ws.append(Ri*sp.Matrix(tabla.obtener(i,"W")))
    qs.append(Ri*sp.Matrix(tabla.obtener(i,"Q"))+ws[i-1])
    Ri= Ri*R[i]

print("Aplicadas las rotaciones")

#Calculo de las velocidades lineales m los vectores giro y las matriz Jacobiana
vs = []
Ji = []
i= 0

vs.append(qs[i].cross(ws[i]))
Ji.append(ws[i].row_insert(3,vs[i]))
J= Ji[0]

for i in range(1,6):
    vs.append(qs[i].cross(ws[i]))
    Ji.append(ws[i].row_insert(3,vs[i]))
    J=J.col_insert(i,Ji[i])



print("Los valores para las configuraciones singulares son los siguientes:")
print(sp.solve(J.subs({t[1]:0, t[2]:0, t[3]:0}).det()))