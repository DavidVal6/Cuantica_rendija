""""HECHO POR:
 -DAVID EDUARDO VALENCIA
 -LEONARDO
 - ANDRES AJIACO
 CNYT , COMPETENCIA RENDIJA
 """


import math
from sys import stdin
import numpy as np

def accion(m1,estado0):
    xn = np.dot(m1,estado0)
    return(xn)


def filas(m):
    return (len(m))


def columnas(m):
    return len(m[0])


def main():
    m1 = [[0,0,0,0,0,0,0,0],[0.5,0,0,0,0,0,0,0],[0.5,0,0,0,0,0,0,0],[0,0.3,0,1,0,0,0,0],[0,0.3,0,0,1,0,0,0],[0,0.3,0.3,0,0,1,0,0],[0,0,0.3,0,0,0,1,0],[0,0,0.3,0,0,0,0,1]]
    estado = [1,0,0,0,0,0,0,0]
    ticks_totales = stdin.readline().strip()
    ticks_totales = int(ticks_totales)

    for i in range(ticks_totales):
        estado = accion(m1, estado)
        print(estado)

main()
