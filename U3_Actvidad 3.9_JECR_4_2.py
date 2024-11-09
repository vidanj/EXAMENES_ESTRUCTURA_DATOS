# Autor: JC Vid Anj
# Grupo: TIDS4-2
# Fecha: 29/10/2024
'''
Un programa que permita crear un arreglo con 20 números SIN REPETIR entre el 1 y el 100. 
Los números los podrá introducir el usuario mediante el teclado o bien se pueden generar aleatorios de manera automática.

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
    CLS()
    print("          Programa 3.9 de Arreglos")
    print("┌──────────── Menú de Opciones ────────────┐")
    print(" 1) Crear arreglo automatico")
    print(" 2) Ingresar valores manualmente")
    print(" 3) Salir")
    
    arreglo = np.empty(20,dtype=int)
    opcion = leer_int("\nIntroduzca la opción deseada: ")
    
    match opcion:
        case 1:
            #Automatico
            for i in range(arreglo.__len__()):
                random = np.random.randint(1,101)
                while arreglo.__contains__(random):
                    random = np.random.randint(1,101)
                arreglo[i] = random
            
            print("Arreglo generado")
            print(arreglo)
            pausa("\nPresione una tecla para continuar...")
            
        case 2:
            #Manual
            for i in range(arreglo.__len__()):
                while True:
                    numero = leer_int_mayor0(f"[{i+1}] Ingrese un valor entre 1 y 100: ")
                    if numero > 100:
                        beep_error()
                        print("Error! Debe ser un numero entre 1 y 100. Intente de nuevo.\n")
                    elif arreglo.__contains__(numero):
                        beep_error()
                        print("Error! No puede haber numeros repetidos en el arreglo. Intente de nuevo.\n")
                    else:
                        break
                
                CLS()
                arreglo[i] = numero
            
            print("Arreglo generado")
            print(arreglo)
            pausa("\nPresione una tecla para continuar...")
            
        case 3:
            break
        case _:
            beep_error()
            pausa("Error! La opción no es correcta. Intente de nuevo.") 
    
   
    
    
        


        