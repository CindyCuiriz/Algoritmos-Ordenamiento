# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:14:38 2023

@author: jocelyn
"""

#ORDENAMIENTO BURBUJA con funciones

numeros_1=[45,17,23,67,21]
numeros_2=[4, 3, 1, 2]
#          0  1  2  3  4


#función de iteraciones, por si solo es ineficiente, no funciona (funny)
def  ordenamientoburbuja(arreglo):
    numero=len(arreglo)
    for i in range(numero):
        for j in range(numero-i-1):
            print(arreglo[i],arreglo[j])
            if arreglo[j] > arreglo[j+1]:
                temp = arreglo[j+1]
                arreglo[j+1]=temp
    return arreglo


'''
optimización con método swap

'''

def swap(arreglo,posicion_1,posicion_2):
    temp = arreglo[posicion_1]
    arreglo[posicion_1] = arreglo[posicion_2]
    arreglo[posicion_2]=temp

def  ordenamientoburbujaswap(arreglo):
    numero=len(arreglo)
    for i in range(numero):
        for j in range(numero-i-1):
            print(arreglo[i],arreglo[j])
            if arreglo[j] > arreglo[j+1]:
                swap(arreglo,j,j+1)
    return arreglo

test_1 = ordenamientoburbujaswap(numeros_1)
test_2 = ordenamientoburbujaswap(numeros_2)
print(test_1)      
print(test_2)


'''
todo en una sola linea de código:
'''
def  ordenamientoburbujashort(arreglo):
    numero=len(arreglo)
    for i in range(numero):
        for j in range(numero-i-1):
            print(arreglo[i],arreglo[j])
            if arreglo[j] > arreglo[j+1]:
                arreglo[j],arreglo[j+1]= arreglo[j+1],arreglo[j]   #aqui hacemos el intercambio
    return arreglo

test_1 = ordenamientoburbujashort(numeros_1)
test_2 = ordenamientoburbujashort(numeros_2)
print(test_1)      
print(test_2)   
