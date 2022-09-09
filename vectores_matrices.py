import libreria_complejos as LC
import math

def adicion_vc(v1,v2):  #vn = vector No
    """
    La función recibe 2 vectores de números complejos y retorna su suma componente a componente.
    """
    return adicion_mc(v1,v2)
def inverso_aditivo_vc(v1):
    """
    La función recibe un vector de números complejos y multiplica por (-1) la parte real y la parte imaginaria de cada uno de los complejos que conforman el vector.
    """
    return inverso_ad_mc(v1)
def mult_escalar_vc (e,v1): #e = escalar
    """
    La función recibe un número escalar complejo y un vector de números complejos, luego retorna el producto o multiplicación de dicho escalar por cada una de las componentes del vector recibido.
    """
    v1 = mult_escalar_mc(e,v1)
    return v1

def adicion_mc(m1,m2):  # mn = matriz No
    """
    La función recibe dos matrices del mismo tamaño y devuelve su suma componente a componente.
    """
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        rta = crear_matriz(m1,m2)
        for i in range(len(m1)): #filas de la matriz compleja 1
            for j in range(len(m2[0])):# columnas de la matriz compleja 2
                rta[i][j]= LC.sumacmplx(m1[i][j],m2[i][j])
        return   rta
    else:
        return "no se puede realizar el producto de las matrices revise el tamaño de las matrices"

def inverso_ad_mc(m1):
    """
    La función recibe una matriz de números complejos y multiplica por (-1) la parte real y la parte imaginaria de cada una de las posiciones que conforman la matriz original.
    """
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j]=[m1[i][j][0] * -1, m1[i][j][1] * -1]
    return m1

def mult_e_mc(e,m1): #e = escalar
    """
    La función recibe un número escalar complejo y una matriz de números complejos, luego retorna el producto o multiplicación de dicho escalar por cada una de las posiciones de la matriz recibida.
    """
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j]= LC.multiplicarcmplx(m1[i][j],e)
    return m1

def traspuesta_mv(mv1): #mv = matriz o vector No
    """
    La función recibe una matriz o un vector de números complejos, y retorna su transpuesta.
    """
    rta = crear_matriz1(len(mv1[0],len(mv1)))
    for i in range (len(mv1[0])):
        for j in range (len(mv1)):
            rta [i][j]=mv1[j][i]
    return rta
def conjugada_mv(mv1):
    """
    La función recibe un vector o una matriz de números complejos, y retorna su conjugado(a).
    """
    for i in range(len(mv1)):
        for j in range(len(mv1[0])):
            mv1[i][j]= LC.conjugadocmplx(mv1[i][j])
    return mv1

def adjunta_mv(mv1):
    """
    La función recibe un vector o una matriz de números complejos, y retorna su adjunta.
    """
    rta = traspuesta_mv(mv1)
    rta = conjugada_mv(rta)
    return rta

def producto_mc(m1,m2):
    """
    La función recibe dos matrices del mismo tamaño y devuelve su suma componente a componente.
    """
    if len(m1[0])== len(m2):
        rta = crear_matriz(m1,m2)
        for i in range(len(m1)): #filas de la matriz compleja 1
            for j in range(len(m2[0])):# columnas de la matriz compleja 2
                for k in range(len(m1[0])):
                    rta[i][j] = LC.sumacmplx(rta[i][j],LC.multiplicarcmplx(m1[i][k],m2[k][j]))
        return  rta
    else:
        return "no se puede realizar el producto de las matrices revise el tamaño de las matrices"

def accion_m_v(m1,v1):

    return producto_mc(m1,v1)

def producto_interno_v(v1,v2):

    rta = producto_mc(adjunta_mv(v1),v2)
    return rta

def norma_v(v1):
    rta = producto_interno_v(v1,v1)
    rta1 = math.sqrt(rta[0][0][0])
    return  rta1

def distancia_2v(v1,v2):
    rta = adicion_vc(v1,inverso_aditivo_vc(v2))
    rta1 = norma_v(rta)
    return rta1
def