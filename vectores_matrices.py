import libreria_complejos as LC
import math

def suma_vc(v1, v2):
    a = len(v1)
    b = len(v1[0])
    filas = [(0,0)]*b
    suma = [filas]*a
    for i in range(a):
        filas =  [(0,0)]*b
        suma[i] = filas
        for j in range(b):
            suma[i][j] = LC.sumacmplx(v1[i][j],v2[i][j])
    return suma  

def inverso_aditivo_v (v1):
    a = len(v1)
    b = [(0,0)]*a
    for i in range(a):
        b[i] = LC.multiplicarcmplx((-1,0),v1[i])
    return b 

def multi_escalar_v(v1):
    escalar = int(input("escalar"))
    e = escalar 
    a = len (v1)
    b = [(0,0)] * a 
    for i in range(a):
        b[i] = LC.multiplicarcmplx ((e,0),v1[i])
    return b

def suma_mc(m1, m2):
    a = len(m1)
    b = len(m1[0])
    filas = [(0,0)]*b
    suma = [filas]*a
    for i in range(a):
        filas =  [(0,0)]*b
        suma[i] = filas
        for j in range(b):
            suma[i][j] = LC.sumacmplx(m1[i][j],m2[i][j])
    return suma  

def inverso_aditivo_mc(m1):
    a = len(m1)
    b = len(m1[0])
    filas = [(0,0)] * b
    inverso = [filas] * a
    for i in range (a):
        filas = [(0,0)] * b
        inverso[i] = filas
        for j in range(b):
            inverso[i][j] = LC.multiplicarcmplx((-1,0),m1[i][j])
    return inverso

def multi_escalar_m(m1):
    escalar = int (input("escalar ="))
    e = escalar
    a = len(m1)
    b = len(m1[0])
    filas = [(0,0)] * b
    multiE = [filas] * a
    for i in range(a):
        filas = [(0,0)] * a
        multiE[i] = filas

        for j in range(b):
            multiE[i][j] = LC.multiplicarcmplx((e,0),m1[i][j])
    return multiE

def traspuesta_mv(mv):
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

def conjugada_mv (mv):
    a = len(mv)
    b = len(mv[0])
    filas = [(0,0)] * b
    conjugada = [filas] * a
    for i in range(a):
        filas = [(0,0)] * a
        conjugada[i] = filas 
        for j in range(b):
            conjugada[i][j] = LC.conjugadocmplx(mv[i][j])
    return conjugada

def adjunta_mv(mv):
    a = len (mv)
    b = len(mv[0])
    filas = [(0,0)] * b
    adjunta = [filas] * a
    c= conjugada_mv(traspuesta_mv(mv))
    for i in range(a):
        filas = [(0,0)] * b
        adjunta[i] = filas
        for j in range(b):
            adjunta[i][j] = mv[i][j]
    return adjunta

def producto_matrices(m1,m2):
    a = len(m1)
    b = len(m2)
    c = [[(0,0)for i in range (b)] for i in range(a) ]
    for i in range (a):
        for j in range (b):
            for k in range(a):
                a[i][j] = LC.sumacmplx(c[i][j],LC.multiplicarcmplx(m1[i][k],m2[k][j]))

    return a 

def accion_M_V(m1,v1):
    a = len (m1)
    b = [(0,0)] * a
    for i in range (a):
        for j in range (a):
            a[i] = LC.sumacmplx(a[i],LC.multiplicarcmplx(m1[i][j],v1[j]))
    
    return a 

def productoint_2v(v1,v2):
    a = len(v1)
    b = (0,0)
    c = [(0,0)] * a
    for i in range (a):
        c[i] = LC.multiplicarcmplx(LC.conjugadocmplx(v1[i],v2[i]))
        b = LC.sumacmplx (c[i],b)
    
    return b

def norma_V(v1):
    a = len(v1)
    b = (0,0)
    for i in range (a):
        b = LC.sumacmplx(LC.multiplicarcmplx(v1[i],v1[i]),b)
    b = LC.modulocmplx(b)
    return b 

def distacia_2v(v1,v2):
    a = len (v1)
    b = 0 
    for i in range (a):
        b = b + (LC.modulocmplx(LC.restacmplx(v1[i],v2[i])))**2
    b = math.sqrt(b)
    return b

def matriz_unitaria(m1):
    a = len(m1)
    b = [[(0,0)for i in range (a)]for i in range (a)]
    c = [[(0,0)for i in range (a)]for i in range (a)]
    for i in range (a):
        b = producto_matrices(adjunta_mv(m1),m1)
    for i in range (a):
        c [i][i] =(1,0)
    d = a ==c
    return d


def matriz_hermitania(m1):
    a = len(m1)
    b = [[(0,0)for i in range (a)]for i in range (a)]
    b = adjunta_mv(m1)
    c = a == m1
    return c

def producto_tensor_v(v1,v2):
    a = len(v1)
    b = len(v2)
    c = a * b
    return c 
