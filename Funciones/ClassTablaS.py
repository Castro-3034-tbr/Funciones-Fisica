#incilizacion de librerias
import numpy as np

class TablaS():
    """Creacion de la tabla para la cinematica directa"""
    
    #Metodo constructor
    def __init__(self):
        self.Wi=[]
        self.Qi=[]
        self.Vi=[]
        self.Si=[]
        self.tamaño = 0
        
    #Metodo de añadir elementos
    def agregar(self,w,q):
        
        w = np.array(w)
        q = np.array(q)
        
        #Peticion de W
        self.Wi.append(w)
        
        #Peticion de Q
        self.Qi.append(q)
        
        #Creacion del vector V
        v = np.cross(q,w)
        self.Vi.append(v)
        
        #Creacion del vector S
        s = np.array([w[0],w[1],w[2],v[0],v[1],v[2]])
        self.Si.append(s)
        
        #Aumento del tamaño
        self.tamaño += 1
    
    #Metodo para poder añadir una articulacion prismatica 
    def agregar_prismatica(self,v):
        w = np.array([0,0,0])
        self.Wi.append(w)
        q = np.array([None,None,None])
        self.Qi.append(q)
        v = np.array(v)
        self.Vi.append(v)
        s = np.array([w[0],w[1],w[2],v[0],v[1],v[2]])
        self.Si.append(s)
        
        
    #Metodo de imprimir
    def imprimir(self,posicion):
        posicion = posicion-1
        cadena = "w = "+str(self.Wi[posicion])+ " q = "+str(self.Qi[posicion])+" V= "+str(self.Vi[posicion])+" S= "+str(self.Si[posicion])
        return cadena
    
    
    #Metodo para obtener un elemento de la tabla
    def obtener(self,posicion,clave):
        if clave == "W":
            return self.Wi[posicion]
        elif clave == "Q":
            return self.Qi[posicion]
        elif clave == "V":
            return self.Vi[posicion]
        elif clave == "S":
            return self.Si[posicion]
    
    #Metodo para obtener el numero de articulaciones
    def tamano(self):
        return self.tamaño
    

