#!/usr/bin/env python
import numpy as np
import sympy as sp

# Funcion que convierte un eje de rotacion en matriz antisimetrica 3x3 (so3)
def VecToso3(w): 
    return sp.Matrix([[0,-w[2],w[1]], [w[2],0,-w[0]], [-w[1],w[0],0]])

# Definimos ejes de rotacion de las articulaciones en la posicion cero del robot
w=[]
w.append(np.array([0,0,1]))
w.append(np.array([0,-1,0]))
w.append(np.array([0,-1,0]))
w.append(np.array([1,0,0]))
w.append(np.array([0,-1,0]))
w.append(np.array([1,0,0]))

# Definimos los eslabones
scalefactor=0.001 # para cambiar las unidades a metros
L=np.array([103.0, 80.0, 210.0, 30.0, 41.5, 180.0, 23.7, -5.5])*scalefactor

# Definimos los vectores que van del centro de cada eje al centro del siguiente
q=[]
q.append(np.array([0,0,L[0]]))
q.append(np.array([0,0,L[1]]))
q.append(np.array([0,0,L[2]]))
q.append(np.array([L[4],0,L[3]]))
q.append(np.array([L[5],0,0]))
q.append(np.array([L[6],0,L[7]]))

# Coordenadas de las articulaciones
t=sp.symbols("t0, t1, t2, t3, t4, t5")

# Calculamos las matrices de rotacion a partir de los ejes w, utilizando la formula de Rodrigues
R=[]
for i in range(0,6,1):
    wmat=VecToso3(w[i])
    R.append(sp.eye(3)+sp.sin(t[i])*wmat+(1-sp.cos(t[i]))*(wmat*wmat))

# Aplicamos rotaciones a los vectores q y w para llevarlos a la configuracion deseada
qs=[]; ws=[]; Ri=R[0]
qs.append(sp.Matrix(q[0]))
ws.append(sp.Matrix(w[0]))
for i in range(1,6,1):
    ws.append(Ri*sp.Matrix(w[i]))
    qs.append(Ri*sp.Matrix(q[i])+qs[i-1])
    Ri=Ri*R[i]

# Calculamos las velocidades lineales, los vectores giro correspondientes y la matriz Jacobiana
vs=[]; Ji=[]
i=0
vs.append(qs[i].cross(ws[i]))
Ji.append(ws[i].row_insert(3,vs[i]))
J=Ji[0]

for i in range(1,6,1):
    vs.append(qs[i].cross(ws[i]))
    Ji.append(ws[i].row_insert(3,vs[i]))
    J=J.col_insert(i,Ji[i])


print("Los valores para las configuraciones singulares son los siguientes:")
print(sp.solve(J.subs({t[1]:0, t[2]:0, t[3]:0}).det()))