# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 22:01:04 2023

@author: jocelyn
"""

'''

ordenamiento por inserción directa
Es más eficiente que método burbuja y método de selección, es un punto medio
utiliza apuntadores para ver dónde hacer los intercambios
mejora rendimiento, pero es ineficiente por tener for's anidados
(similar a selección)

'''

numeros_1=[89,7,73,68,23,59,66]
numeros_2=[8,4, 3,6, 1, 2]
#          0  1  2  3  4

def ordenamientoinsercion(arreglo):
    n = len(arreglo)
    for i in range(1,n):
        key=arreglo[i]
        j=i-1
        while j>=0 and key < arreglo[j]:
            arreglo[j+1] = arreglo[j]
            j -= 1
        arreglo[j+1] = key
        
    return arreglo
            

test_1 = ordenamientoinsercion(numeros_1)
test_2 = ordenamientoinsercion(numeros_2)
print(test_1)      
print(test_2)