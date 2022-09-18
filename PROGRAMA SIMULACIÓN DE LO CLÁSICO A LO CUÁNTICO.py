import math 


def sumacmplx(c1, c2):
    real = c1[0] + c2[0]
    img = c1[1] + c2[1]
    return [real, img]

def multiplicarcmplx(c1, c2):
    real = c1[0] * c2[0] + (-1 * c1[1] * c2[1])
    img = c1[0] * c2[1] + c1[1] * c2[0]
    return [real, img]


def llena(a):

    b = a.split(" ")
    c = len(a)

    for i in range (c):
        b[i] = tuple(b[i])
    return a 

def crear_matriz(a):
    b = []
    for i in range(a):

        v1 = input("coloque el vector ",i,)# deje un espacio entre los numeros 

        b.append(llena(v1))

    return b 

def traspuesta_mv(mv):  # genera la matriz transpuesta de una matriz  

    a = len(mv)
    b = len(mv[0])
    filas = [(0,0)] * b
    traspuesta = [filas] * a 
    for i in range (a):
        filas = [(0,0)] * b
        traspuesta[i] = filas
        for j in range (b):
            traspuesta[i][j] = mv[j][i]
    return traspuesta

def accion_M_V(m1,v1):
    a = len (m1)
    b = [(0,0)] * a
    for i in range (a):
        for j in range (a):
            a[i] = sumacmplx(a[i],multiplicarcmplx(m1[i][j],v1[j]))
    
    return a

def M_v (m1,v1):

    a = []
    b = 0

    while b<len (m1[0]):
        a.append([])
        c =  0 
        
        while c < len (v1):
            d = 0 

            resultado = 0 

            while d < len (m1):
                resultado = resultado + m1[d][b]* v1 [c][d]

                d += 1
            a[b].append(resultado)
            c += 1
        b += 1
    return traspuesta_mv (a)

def accion_M_V(m1,v1):
    a = len (m1)
    b = [(0,0)] * a
    for i in range (a):
        for j in range (a):
            a[i] = sumacmplx(a[i],multiplicarcmplx(m1[i][j],v1[j]))
    
    return a 
def estado(a,b):
    ve= [0 for i in range(0,b+a+1)]
    ve [0] = 1
    return ve


def clic_cuantico(m1,a,c): #m1 = matriz a = arrglo c = clic
    a = [a]
    
    while c :
        a = accion_M_V(m1 , a)
        c -= 1
    return a[0]

def clic_clasico(m1,a,c):
    a = [a]
    
    while c :
        a = M_v(m1 , a)
        c -= 1
    return a[0]

def matrizdoble(v1,a,b):


    c = llena(c)

    m = [[0 for i in range(0,b+a+1)]for j in range(0,b+a+1)]

    e = 1

    while e < a :
        m[0][i]=c[e-1]

        e+=1

    for d in range (a+1, len(m)):
        for f  in range()
