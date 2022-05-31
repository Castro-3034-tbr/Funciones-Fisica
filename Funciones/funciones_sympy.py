import sympy as sp
import numpy as np


def VecToso3_sympy(w):
    """Conversion de un vector a 3x3"""
    m = sp.Matrix([[0,-w[2],w[1]], [w[2],0,-w[0]], [-w[1],w[0],0]])
    return m

def VecTose3_sympy(V): 
    """Conversion de un vector giro en un matriz 4x4 """
    return np.r_[np.c_[VecToso3_sympy([V[0], V[1], V[2]]), [V[3], V[4], V[5]]], np.zeros((1, 4))]

def so3ToVec_sympy(so3mat):
    """Conversion de una matriz 3x3 en un vector"""
    return np.array([so3mat[2][1], so3mat[0][2], so3mat[1][0]])

def se3ToVec_sympy(se3mat):
    """Conversion de un matriz en un vector 1x6"""
    return np.r_[[se3mat[2][1], se3mat[0][2], se3mat[1][0]],
[se3mat[0][3], se3mat[1][3], se3mat[2][3]]]

def getejes(): 
    """Obtencion de los vectores de cada eje"""
    w=[]
    w.append(np.array([0,0,1]))
    w.append(np.array([0,-1,0]))
    w.append(np.array([0,-1,0]))
    w.append(np.array([1,0,0]))
    w.append(np.array([0,-1,0]))
    w.append(np.array([1,0,0])) 
    return w

def getqs(): 
    """Obtencion de los vectores de cada eje"""
    
    q=[]; scalefactor=0.001
    L=np.array([103.0, 80.0, 210.0, 30.0, 41.5, 180.0, 23.7, -5.5])*scalefactor
    q.append(np.array([0,0,L[0]]))
    q.append(np.array([0,0,L[1]]))
    q.append(np.array([0,0,L[2]]))
    q.append(np.array([L[4],0,L[3]]))
    q.append(np.array([L[5],0,0]))
    q.append(np.array([L[6],0,L[7]]))
    return 

def getS(): 
    """Calculo de los vectores S"""
    #Calculo de W y Q
    w=getejes() 
    q=getqs()
    scalefactor=0.001
    
    L=np.array([103.0, 80.0, 210.0, 30.0, 41.5, 180.0, 23.7, -5.5])*scalefactor
    qs=[]; ws=[]
    qs.append(np.array(q[0]))
    ws.append(np.array(w[0]))
    for i in range(1,6,1):
        ws.append(np.array(w[i]))
        qs.append(np.array(q[i])+qs[i-1])

def getR_sympy(tabla,i,t):
    """Calculo de la matriz R con la formula de rodrigues en calculo symbolico"""
    
    #Definion de varaibles locales 
    R=[]
    
    #Calculo
    for i in range(0,6):
        wmat= VecToso3_sympy(tabla.obtener(i,"W"))
        ri = sp.eye(3)+sp.sin(t[i])*wmat+(1-sp.cos(t[i]))*(wmat*wmat)
        R.append(ri)
    
    return R

def getR2_sympy(w,ang): # Formula de Rodrigues para obtener matriz de Rotación
    wmat=VecToso3_sympy(w)
    return np.eye(3)+np.sin(ang)*wmat+(1.-np.cos(ang))*np.dot(wmat,wmat)

def getT_sympy(orientation,r):
    """Calculo de a matriz Transformacion Homogenea
    RETURN: LIST"""
    
    #Definicion de variables locales
    i=np.array([1,0,0]); j=np.array([0,1,0]); k=np.array([0,0,1])
    
    #Calculo
    Ri=getR2_sympy(i,orientation[0]); Rj=getR2_sympy(j,orientation[1]); Rk=getR2_sympy(k,orientation[2])
    R=np.matmul(Rk,np.matmul(Rj,Ri))
    aux=np.array([[0,0,0,1]])
    
    return np.r_[np.c_[R,r],aux]

def MatrixExp6_sympy(se3mat):
    """Comversion de un vector giro en una matriz 4x4"""
    
    #Definicion de variables locales
    se3mat = np.array(se3mat) 
    v=se3mat[0: 3, 3] 
    omgmattheta=se3mat[0: 3, 0: 3] 
    omgtheta = so3ToVec_sympy(omgmattheta) 
    
    #Calculo
    if (np.linalg.norm(omgtheta))<1.e-6: 
        return np.r_[np.c_[np.eye(3), v], [[0, 0, 0, 1]]] 
    else: # caso general
        theta = np.linalg.norm(omgtheta)
        omgmat = omgmattheta / theta 
        G_theta=np.eye(3)*theta+(1-np.cos(theta))*omgmat+(theta-np.sin(theta))*np.dot(omgmat,omgmat)
        R=np.eye(3)+np.sin(theta)*omgmat+(1.-np.cos(theta))*np.dot(omgmat,omgmat)
        return np.r_[np.c_[R,np.dot(G_theta,v)/theta],[[0, 0, 0, 1]]]

def MatrixLog3_sympy(R): 
    """Calculo de la matriz logaritmo de una matriz de rotacion"""
    #Calculo
    acosinput = (np.trace(R) - 1) *0.5
    if np.trace(R) >= 3: return np.zeros((3, 3))
    elif np.trace(R) <= -1:
        if abs(1 + R[2][2])>1.e-6:
            omg = (1.0 / np.sqrt(2 * (1 + R[2][2]))) * np.array([R[0][2], R[1][2], 1 + R[2][2]])
        elif abs(1 + R[1][1])>1.e-6: omg = (1.0 / np.sqrt(2 * (1 + R[1][1]))) * np.array([R[0][1], 1 + R[1][1], R[2][1]])
        else: omg = (1.0 / np.sqrt(2 * (1 + R[0][0]))) * np.array([1 + R[0][0], R[1][0], R[2][0]])
        return VecToso3_sympy(np.pi * omg)
    else:
        theta = np.arccos(acosinput)
        return (theta*0.5)/np.sin(theta) * (R-np.array(R).T)

def MatrixLog6_sympy(T): 
    """Calculo de la matriz logartimo de una matriz de transformacion homogenea"""
    
    #Definicion de variables locales
    R=T[0: 3, 0: 3]; p = T[0: 3, 3] 
    omgmat = MatrixLog3_sympy(R) 
    
    # Calculo
    if np.array_equal(omgmat, np.zeros((3, 3))): 
        return np.r_[np.c_[np.zeros((3, 3)),p],[[0, 0, 0, 0]]]
    else:
        omgvec= so3ToVec_sympy(omgmat) 
        omgmat=omgmat/np.linalg.norm(omgvec) 
        theta = np.linalg.norm(omgvec)
        invG_theta=np.eye(3)/theta-omgmat*0.5+(1.0/theta-0.5/np.tan(theta*0.5))*np.dot(omgmat,omgmat)
        v=np.dot(invG_theta,p)
        return np.r_[np.c_[omgmat,v],[[0, 0, 0, 0]]]*theta 

def CinematicaDirecta_sympy(M,tabla,t):
    """Calculo de la cinematica directa """
    T=np.eye(4)
    for i in range(0,6,1): 
        print(VecTose3_sympy(tabla.obtener(i,"S")*t[i]))
        T=np.dot(T,MatrixExp6_sympy(VecTose3_sympy(tabla.obtener(i,"S")*t[i])))
    return np.dot(T,M)

def Adjunta_sympy(T):
    """Calculo de la matriz Adjunta de una matriz de transformacion homogenea"""
    R=T[0: 3, 0: 3]; p = T[0: 3, 3]
    return np.r_[np.c_[R, np.zeros((3, 3))], np.c_[np.dot(VecToso3_sympy(p), R), R]]

def Jacobiana_sympy(tabla,theta):
    """Calculo de la matriz Jacobiana"""
    
    #Definicion de variables locales
    t=sp.symbols("t0, t1, t2, t3, t4, t5")
    
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