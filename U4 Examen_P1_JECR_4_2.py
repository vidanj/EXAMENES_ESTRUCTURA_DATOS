# Autor: JC Vid Anj.
# Grupo: TIDS4-2
# Fecha: 22/11/2024
'''
Elaborar un programa que cree dos colas de 20 números aleatorios entre el 1 y el 100, sin repetidos y las imprima. 
Después que muestre cuáles números coinciden en ambas colas.


'''

from MisFunciones_2024 import *
from stack_and_queue import Stack

# ------------- Codigo Principal -------------

CLS()
    
pila = Stack()
pila.push(0)
previo = pila.peek()
pila.push(1)
tope = pila.peek()

for i in range(17):
    pila.push(previo + tope)
    previo = tope
    tope = pila.peek()
    
    
    
print("A continuación se muestras los primeros 18 números de la sucesion de Fibonaccion: ")
print(pila.all_items())
print("El tope es ->",pila.peek())
    
pausa_final()
