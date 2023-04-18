# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:46:19 2023

@author: jocelyn
"""

'''
ORDENAMIENTO POR SELECCIÓN
INTERCAMBIO DE POSICIONES (POKER)
SELECCIONAS EL NUMERO MENOR Y SE CAMBIA POR LA POSICIÓN ACTUAL
ORGANIZAS VALOR POR VALOR 
'''

numeros_1=[89,7,73,68,23,59,66]
numeros_2=[8,4, 3,6, 1, 2]
#          0  1  2  3  4

def ordenamientoseleccion(arreglo):
    n = len(arreglo)
#    print(n) #contamos cuantos valores tiene el array
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arreglo[min] > arreglo[j]:
                min= j
        #intercambio de los arreglos utilizando variable de salvamento
        temp = arreglo[i]
        arreglo[i]=arreglo[min]
        arreglo[min] = temp
    return arreglo
test_1 = ordenamientoseleccion(numeros_1)
test_2 = ordenamientoseleccion(numeros_2)
print(test_1)      
print(test_2)

#version un poco más corta con intercambio de variable en una sola linea

def ordenamientoseleccionshorter(arreglo):
    n = len(arreglo)
#    print(n) #contamos cuantos valores tiene el array
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arreglo[min] > arreglo[j]:
                min= j
        arreglo[i],arreglo[min] = arreglo[min],arreglo[i]
    return arreglo
            

test_1 = ordenamientoseleccionshorter(numeros_1)
test_2 = ordenamientoseleccionshorter(numeros_2)
print(test_1)      
print(test_2)