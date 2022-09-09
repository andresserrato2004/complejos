
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
    real = multiplicarcmplx(c1, conjugadocmplx(c1))
    img = multiplicarcmplx(c2, conjugadocmplx(c1))
    real = list(real)
    img = list(img)
    resultado = (real[0] / img[0], real[1] / img[0])
    return (resultado)


def modulocmplx(c1):
    mod = ((c1[0] ** 2) + (c1[1] ** 2)) ** 0.5
    return mod


def conjugadocmplx(c1):
    conjugado = (c1[0], -1 * c1[1])
    return (conjugado)


def carteapolar(c1):
    mod = modulocmplx(c1)
    mod = int(mod)
    tan = math.atan2(c1[0], c1[1])
    grados = math.degrees(tan)
    grados = int(grados)
    return (mod, grados)


def polaracarte(c1,c2):
    b = math.radians(c2)
    cx = c1 * math.cos(b)
    cy = c1 * math.sin(b)
    return (cx, cy)

def fase(c1):
    b = math.atan(c1[1] / c1[0])
    c = math.degrees(b)
    return (c)


 
