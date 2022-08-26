
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


def main():
    "los datos deben entrar como tuplas y estar separados por espacios y cada numero complejo tiene que estar separado por enter y el ultimo valor pedido es el signo"
    "para ingresar una suma el signo que se debe colocar es  +"
    "para ingresar una resta el signo que se debe colocar es -"
    " para ingresar una multiplicacion el signno que se debe colocar es *" \
    "para ingresar una divicion el signo que se debe colocar es /  "
    "para ingresar  el modulo el signo que se debe colocar es mod"
    "para ingresar conjugado el signo que se debe colocar es conj"
    "para ingresar  carteapolar el signo que se debe colocar es polar"
    "para ingresar polaracarte el signo que se debe colocar es carte"
    "para ingresar la fase el signo que se debe colocar es  fase"
    num1 = [int(x) for x in stdin.readline().strip().split()]
    num2 = [int(x) for x in stdin.readline().strip().split()]
    signo = str(stdin.readline().strip())

    if signo == "+":
        resultado = sumacmplx(num1, num2)
        print(str(resultado[0]) + "+" + str(resultado[1]) + "i")

    elif signo == "-":
        resultado = restacmplx(num1, num2)
        print(str(resultado[0]) + "+" + str(resultado[1]) + "i")

    elif signo == "*":
        resultado = multiplicarcmplx(num1, num2)
        print(str(resultado[0]) + "+" + str(resultado[1]) + "i")

    elif signo == "/":

        if num2[0] == 0 and num2[1] == 0:
            print("Division imposible")
            main()

        else:
            resultado = divisioncmplx(num1, num2)
            print(resultado)

    elif signo == "mod":
        mod1 = modulocmplx(num1)
        mod2 = modulocmplx(num2)
        print(str(mod1), "i")
        print(str(mod2), "i")

    elif signo == "conj":
        resultado1 = conjugadocmplx(num1)
        resultado2 = conjugadocmplx(num2)
        print(resultado1)
        print(resultado2)

    elif signo == "polar":
        resultado1 = carteapolar(num1)
        resultado2 = carteapolar(num2)
        print(str(resultado1[0]) + "+" + "e^i(" + str(resultado1[1]) + ")")
        print(str(resultado2[0]) + "+" + "e^i(" + str(resultado2[1]) + ")")

    elif signo == "carte":
        resultado1 = polaracarte(num1)
        resultado2 = polaracarte(num2)
        print(str(resultado1[0], resultado1[1]))
        print(str(resultado2[0],resultado2[1]))
    elif signo == "fase":
        resultado1 = fase(num1)
        resultado2 = fase(num2)
        print(resultado1)
        print(resultado2)


main()
