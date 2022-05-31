matriz =[[0,1,0,1,1,1],[0,1,0,1,1,1],[0,1,0,1,1,1]]
matriz2 =[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

import numpy as np

#Transposicion de la matriz
print(len(matriz))
print(len(matriz[0]))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz2[j][i] = matriz[i][j]

print(matriz2)

v= np.array([0,1,1,1,13,3])
matriz3 = np.transpose(matriz)
f= np.dot(v,matriz3)
print(f)