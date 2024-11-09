# Autor: Campuzano Rangel Jesús Efrén
# Grupo: TIDS4-2
# Fecha: 01/11/2024
'''
Elabore un programa que introduzca 10 números en una lista y que mediante el uso de una pila los ponga en la lista de 
vuelta en orden inverso al que tenían. 
Imprimir la lista final.

'''

from MisFunciones_2024 import *
from stack_and_queue import Stack
from random import randint

listanum = []
pila = Stack()

CLS()

for i in range(10):
    listanum.append(randint(1,100))

print("Lista inicial:")    
print(listanum)
print()

for j in range(listanum.__len__()):
    pila.push(listanum[j])
    
listanum.clear()

for k in range(pila.size()):
    listanum.append(pila.pop())

# for j in range(listanum.__len__(),0,-1):
#     pila.push(listanum[j-1])
    
print("Lista invertida:")
print(listanum)

pausa()
    