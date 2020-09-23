
import numpy as np
import torch
pi=np.pi
e=np.e

def ackley(xy,lib):

    x, y = xy[0], xy[1]
    return (-20 * lib.exp(-0.2 * lib.sqrt(0.5 * (x*x + y*y))) -
            lib.exp(0.5 * (lib.cos(2.0*pi*x) + lib.cos(2*pi*y))) + e + 20)


def bartels_conn(xy,lib):

    x, y = xy[0], xy[1]
    return lib.abs(x**2 + y**2 + x*y) + lib.abs(lib.sin(x)) + lib.abs(lib.cos(y))


def beale(xy,lib):

    x, y = xy[0], xy[1]
    return ((1.500 - x + x*y)**2 +
            (2.250 - x + x*y**2)**2 +
            (2.625 - x + x*y**3)**2)


def booth(xy,lib):

    x, y = xy[0], xy[1]
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2


def branin(xy,lib):

    a = 1
    b = 5.1 / (4 * pi**2)
    c = 5 / pi
    r = 6
    s = 10
    t = 1/(8*pi)
    x, y = xy[0], xy[1]
    return a * (y - b*x**2 + c*x - r)**2 + s*(1-t)*lib.cos(x) + s


def bukin_n6(xy,lib):

    x, y = xy[0], xy[1]
    return 100 * lib.sqrt(lib.abs(y-0.01*x**2)) + 0.01*lib.abs(x+10)


def camel_hump_3(xy,lib):

    x, y = xy[0], xy[1]
    return 2.0*x**2 - 1.05*x**4 + (x**6 / 6.0) + x*y + y**2


def camel_hump_6(xy,lib):


    x, y = xy[0], xy[1]
    a = (4-(2.1*x**2)+(x**4)/3.0) * x**2
    b = x*y
    c = (-4+(4*y**2)) * y**2
    return a + b + c




def cross_in_tray(xy,lib):

    x, y = xy[0], xy[1]
    return -0.0001*(lib.abs(lib.sin(x)*lib.sin(y)*lib.exp(lib.abs(100-(lib.sqrt(x**2 + y**2)/pi))))+1)**0.1


def drop_wave(xy,lib):

    x, y = xy[0], xy[1]
    return -(1 + lib.cos(12 * lib.sqrt(x**2 + y**2))) / (0.5 * (x**2 + y**2) + 2)


def easom(xy,lib):

    x, y = xy[0], xy[1]
    return -lib.cos(x)*lib.cos(y)*lib.exp(-((x-pi)**2 + (y-pi)**2))


def eggholder(xy,lib):

    x, y = xy[0], xy[1]
    return (-(y+47)*lib.sin(lib.sqrt(lib.abs((x/2.0) + (y+47)))) -
            x*lib.sin(lib.sqrt(lib.abs(x-(y+47)))))


def goldstein_price(xy,lib):

    x, y = xy[0], xy[1]
    return ((1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)) *
            (30 + (2*x-3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2)))





def himmelblau(xy,lib):

    x, y = xy[0], xy[1]
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2


def holder_table(xy,lib):

    x, y = xy[0], xy[1]
    return -lib.abs(lib.sin(x)*lib.cos(y)*lib.exp(lib.abs(1-(lib.sqrt(x**2 + y**2)/pi))))


def levi_n13(xy,lib):

    x, y = xy[0], xy[1]
    return lib.sin(3.0*pi*x)**2 + (x-1)**2 * (1+lib.sin(3.0*pi*y)**2) + (y-1)**2 * (1+lib.sin(2.0*pi*y)**2)


def matyas(xy,lib):

    x, y = xy[0], xy[1]
    return 0.26*(x**2 + y**2) - 0.48*x*y


def mccormick(xy,lib):

    x, y = xy[0], xy[1]
    return lib.sin(x+y) + (x-y)**2 - 1.5*x + 2.5*y + 1


def schaffer_n2(xy,lib):

    x, y = xy[0], xy[1]
    return 0.5 + (lib.sin(x**2 - y**2)**2 - 0.5)/(1+0.001*(x**2+y**2))**2


def schaffer_n4(xy,lib):
 
    x, y = xy[0], xy[1]
    return 0.5 + (lib.cos(lib.sin(lib.abs(x**2 - y**2)))**2 - 0.5)/(1+0.001*(x**2 + y**2))**2


def rosenbrock(xy,lib):
    x, y = xy[0], xy[1]
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


def rastrigin(xy, lib):
    x, y = xy[0], xy[1]
    A = 10
    f = (
        A * 2
        + (x ** 2 - A * lib.cos(x * pi * 2))
        + (y ** 2 - A * lib.cos(y * pi * 2))
    )
    return f
