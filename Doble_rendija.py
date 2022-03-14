""""HECHO POR:
 -DAVID EDUARDO VALENCIA
 -LEONARDO
 - ANDRES AJIACO
 CNYT , COMPETENCIA RENDIJA
 """
from sys import stdin
import math
import numpy as np

def probabilidad(num1,num2):
    operacion = (math.sqrt(num1**2+num2**2))**2
    return operacion

def accion(estado,rendija):
    """Este hallara la accione entre la matriz de adyacencia y el vector de estado de la rendija"""
    return(np.dot(rendija,estado))


def main():
    ticks = stdin.readline().strip()
    ticks = int(ticks)
    # Para rendija se uso la naturaleza de los complejos en python para facilitar la escritura de la matriz
    rendija = [[0,0,0,0,0,0,0,0],[1/math.sqrt(2),0,0,0,0,0,0,0],[1/math.sqrt(2),0,0,0,0,0,0,0], [0,-1/math.sqrt(6)+1j/math.sqrt(6),0,1,0,0,0,0],[0,-1/math.sqrt(6)-1j/math.sqrt(6),0,0,1,0,0,0],[0,1/math.sqrt(6)-1j/math.sqrt(6),-1/math.sqrt(6)+1j/math.sqrt(6),0,0,1,0,0],[0,0,-1/math.sqrt(6)-1j/math.sqrt(6),0,0,0,1,0],[0,0,1/math.sqrt(6)-1j/math.sqrt(6),0,0,0,0,1]]
    estado = [1,0,0,0,0,0,0,0]
    for i in range(ticks):
        estado = accion(estado, rendija)
    for i in range(len(estado)):
        print("Posicion:",i)
        a = estado[i].real
        b = estado[i].imag
        print("La probabilidad es:\n", probabilidad(a,b)*100, "%")
    for i in range(len(estado)):
        print("{:.2f}".format(estado[i]),",")
    print()
main()