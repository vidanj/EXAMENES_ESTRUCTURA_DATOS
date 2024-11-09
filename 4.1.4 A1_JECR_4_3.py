# Autor: JC Vid Anj.
# Grupo: TIDS4-2
# Fecha: 05/11/2024
'''
Escribir un método o función "Reemplazar" para las pilas al que se le den como argumentos dos valores: nuevo y viejo, y que funcione de forma que si 
el valor viejo aparece una o más veces en algún lugar de la pila, estos sean reemplazados por el valor nuevo.

 def replace(self, old_value, new_value):
     _______
     _______

'''

from MisFunciones_2024 import *
from stack_and_queue import Stack
from random import randint

# ------------- Funciones Extra -------------

def replace(pilaOrigen, old_value, new_value):
    pilaAux = Stack()
    
    for i in range(pilaOrigen.size()):
        if(pilaOrigen.peek() != old_value):
            pilaAux.push(pila.pop())
        else:
            pilaOrigen.pop()
            pilaAux.push(new_value)
    
    for i in range(pilaAux.size()):
        pilaOrigen.push(pilaAux.pop())
    
    return pilaOrigen


# ------------- Codigo Principal -------------
while True:
    
    pila = Stack()
    pilaHelp = Stack()
    CLS()

    for i in range(20):
        pila.push(randint(1,100))

    print("Listas iniciales:")    
    print("Pila",pila.all_items(), " <- Tope:",pila.peek())
    print()



    while True:
        
        valorViejo = leer_int("Valor a reemplazar: ")
        if (pila.all_items().__contains__(valorViejo)):
            # print("Existe!")
            valorNuevo = leer_int("Ingrese el nuevo valor: ")
            break
            
            # for i in range(pila.size()):
            #     if(pila.peek() != valorViejo):
            #         pilaHelp.push(pila.pop())
            #     else:
            #         pila.pop()
            #         pilaHelp.push(valorNuevo)
        
            # for i in range(pilaHelp.size()):
            #     pila.push(pilaHelp.pop())
            
        else:
            beep_error()
            print("La pila no contiene el valor",valorViejo)
            print()

    pila = replace(pila,valorViejo,valorNuevo)

    print()
    print("Pila",pila.all_items(), " <- Tope:",pila.peek())
    print()    

    
    continuar = input("\n¿Desea repetir el programa? ('Si' para confirmar): ")
    if(continuar == "" or continuar.upper()[0] != "S"   ): break
    
