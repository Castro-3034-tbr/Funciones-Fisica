#Inicilizacion de librerias 
import sympy as sp 
import matplotlib.pyplot as plt
import numpy as np


#DEclaracion de varaibles simbolicas
t1=sp.var("t1")
t2=sp.var("t2")
L1=sp.var("L1")
L2=sp.var("L2")

a=-L1*sp.sin(t1)-L2*sp.sin(t1+t2)
b=L1*sp.cos(t1)+L2*sp.cos(t1+t2)
c=-L2*sp.sin(t1+t2)
d=L2*sp.cos(t1+t2)

m=sp.Matrix([[a,c],[b,d]])


#Creacion de las cordenadas de un circulo
cordenadas = []

for i in range(0,360):
    x = sp.cos(i*sp.pi/180)
    y = sp.sin(i*sp.pi/180)

    cordenadas.append([x,y])

plt.figure(figsize=(4,4))
for i in range(0,len(cordenadas)):
    plt.plot(cordenadas[i][0],cordenadas[i][1],'ko')
plt.title("0")
plt.grid()


#Matriz Jacobiana J1
plt.figure(figsize=(4,4))
J1= (m.subs({t1:0, t2:(sp.pi/4), L1:1, L2:1}))
print(J1)
J1T= np.transpose(np.array(J1,dtype=float))
print(J1T)
J1T = np.linalg.inv(J1T)
solucion = []

for i in cordenadas:
    solucion.append(np.dot(J1T,i))

for i in range(0,len(cordenadas)):
    plt.plot(solucion[i][0],solucion[i][1],'ko')
plt.title("J1")
plt.grid()


#Matriz Jacobiana J2
plt.figure(figsize=(4,4))
J2= (m.subs({t1:0, t2:(3*sp.pi/4), L1:1, L2:1}))
J2T= np.transpose(np.array(J2,dtype=float))
J2T = np.linalg.inv(J2T)
solucion2 = []

for i in cordenadas:
    solucion2.append(np.dot(J2T,i))

for i in range(0,len(cordenadas)):
    plt.plot(solucion2[i][0],solucion2[i][1],'ko')

plt.title("J2")
plt.grid()

#Matriz Jacobiana J3
plt.figure(figsize=(4,4))
J3= (m.subs({t1:0, t2:0, L1:1, L2:1}))
J3T= np.transpose(np.array(J3,dtype=float))
J3T = np.linalg.inv(J3T)
solucion2 = []

for i in cordenadas:
    solucion2.append(np.dot(J3T,i))

for i in range(0,len(cordenadas)):
    plt.plot(solucion2[i][0],solucion2[i][1],'ko')
plt.title("J3")
plt.grid()


plt.show()
