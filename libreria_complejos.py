
import math


def sumacmplx(c1, c2):
    real = c1[0] + c2[0]
    img = c1[1] + c2[1]
    return [real, img]


def restacmplx(c1, c2):
    real = c1[0] - c2[0]
    img = c1[1] - c2[1]
    return [real, img]


def multiplicarcmplx(c1, c2):
    real = c1[0] * c2[0] + (-1 * c1[1] * c2[1])
    img = c1[0] * c2[1] + c1[1] * c2[0]
    return [real, img]


def divisioncmplx(c1, c2):
    real = (c1[0]*c2[0] + c1[1]*c2[1])/(c2[0]**2 + c2[1]**2)
    img = (c1[1]*c2[0] - c1[0] * c2[1])/c2[0]**2 + c2[1]**2)
    
   
    return (real, img)



def modulocmplx(c1):
    mod = ((c1[0] ** 2) + (c1[1] ** 2)) ** 0.5
    return mod


def conjugadocmplx(c1):
    conjugado = (c1[0], -1 * c1[1])
    return (conjugado)


def carteapolar(c1):
    modulo = (c1[0]**2+c1[1]**2)**0.5
    return (mod, grados)


def polaracarte(c1,c2):
    b = math.radians(c2)
    cx = c1 * math.cos(b)
    cy = c1 * math.sin(b)
    return (cx, cy)

def fase(c1):
    b = math.atan(c1[1] / c1[0])
   
    return (b)
if __name__=="__main__":
    c1 = (3.5, 5.7)
    c2 = (2.80, 4.76)
    print(sumacomplx(c1,c2))
    print(restacmplx(c1,c2))
    print(multiplicarcmplx(c1,c2))
    print(divisioncmplx(c1, c2))
    print(modulocmplx(c1))
    print(conjugadocmplx(c1))
    print(carteapolar(c1))
    print(polaracarte(c1,c2))
    print(fase(c1))
    

 
