# Autor: JC Vid Anj
# Grupo: TIDS4-2
# Fecha: 09/11/2024
'''
le das al programa un número n y te crea una matriz como se ve en los ejemplos, luego pasa esos números a un arreglo (todo eso con numpy) 
y después imprime todo.


'''
from MisFunciones_2024 import *
import numpy as np

# ------------- Funciones Extra -------------
def leer_int_mayor0(msj: str):
    ''' Leer un valor entero mayor que 0. '''
    while True:
        try:
            numero = int(input(msj))
            if( numero > 0):
                return int(numero)
            else:
                beep_error()
                print("Error! Debe ser un entero mayor a 0. Intente de nuevo.\n")
        except:
            beep_error()
            print("Error! Debe dar un número entero. Intente de nuevo.\n")

# ------------- Codigo Principal -------------

CLS()

while True:
    
    dimensionesM = leer_int_mayor0(f"Ingrese el tamaño de la matriz deseada: ")
    dimensionA = dimensionesM*dimensionesM
    
    matriz = np.empty((dimensionesM,dimensionesM), dtype=int)
    
    for i in range(dimensionesM):
        for j in range(dimensionesM):
            matriz[i,j] = i+1
    
    print("Matriz: ")
    print(matriz)
    print()
    arreglo = np.empty(dimensionA,dtype=int)
    cont = 0
    
    while cont < (dimensionA):
        for i in range(dimensionesM):
            for j in range(dimensionesM):
                arreglo[cont] = matriz[i,j]
                cont += 1
    
    print("Arreglo: ")
    print(arreglo)
    
    continuar = input("\n¿Desea repetir el programa? ('Si' para confirmar): ")
    if(continuar == "" or continuar.upper()[0] != "S"   ): break
    
