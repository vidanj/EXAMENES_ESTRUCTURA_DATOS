# Autor: JC Vid Anj.
# Grupo: TIDS4-2
# Fecha: 22/11/2024
'''
En matemáticas, la sucesión de Fibonacci es la siguiente sucesión infinita de números naturales:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, …

La sucesión comienza con los números 0 y 1, y a partir de estos, cada término es la suma de los dos anteriores, es la relación de recurrencia que la define.

Elaborar un programa que mediante el uso de una estructura de pila genere e imprima los primeros 18 números de la Sucesión de Fibonacci:

'''

from MisFunciones_2024 import *
from stack_and_queue import Queue
from random import randint

# ------------- Clase Extra -------------

class Queue(Queue): #Extension de la clase Queue (Hereda todos sus parametros y metodos)
    
    def contains(self, var):
        if (self.__items.__contains__((var))):
            return True

# ------------- Codigo Principal -------------

while True:
    CLS()
    
    cola = Queue()
    cola2 = Queue()
    colaComun = Queue()

    for i in range(20):
        random = randint(1,100)
        while cola.contains(random):
                random = randint(1,100)
        cola.enqueue(random)
        
    for i in range(20):
        random = randint(1,100)
        while cola2.contains(random):
                random = randint(1,100)
        cola2.enqueue(random)
        if cola.contains(random): colaComun.enqueue(random)
        
    print("Datos de la cola 1")    
    print(cola.all_items())
    print("Primero en la cola 1:", cola.first())
    print("Último en la cola 1:", cola.last())
    
    print("\nDatos de la cola 2")    
    print(cola2.all_items())
    print("Primero en la cola 2:", cola2.first())
    print("Último en la cola 2:", cola2.last())

    print("\nElementos comunes: ")
    print(colaComun.all_items())
    
    continuar = input("\n¿Desea repetir el programa? ('Si' para confirmar): ")
    if(continuar == "" or continuar.upper()[0] != "S"   ): break
