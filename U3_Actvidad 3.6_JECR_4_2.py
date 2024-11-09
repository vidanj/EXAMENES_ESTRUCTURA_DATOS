# Autor: JC Vid Anj.
# Grupo: TIDS4-2
# Fecha: 25/10/2024
'''
Elaborar un programa en Python que permita capturar nombre y calificación de 8 personas ficticias, en dos arreglos, por ejemplo:

'''
from MisFunciones_2024 import *
import numpy as np

# ------------- Funciones -------------
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
            
def leer_float_mayor0(msj: str):
    ''' Leer un valor entero flotante que 0. '''
    while True:
        try:
            numero = float(input(msj))
            if( numero > 0):
                return float(numero)
            else:
                beep_error()
                print("Error! Debe ser un flotante mayor a 0. Intente de nuevo.\n")
        except:
            beep_error()
            print("Error! Debe dar un flotante. Intente de nuevo.\n")


# ------------- Codigo Principal -------------
while True:
    CLS()

    cantidad_estudiantes = leer_int_mayor0("Ingrese la cantidad de alumnos a calificar: ")
    
    array_estudiante = np.empty(cantidad_estudiantes, dtype=object) # Para que soporte strings en un arreglo de numpy.
    array_calif = np.empty(cantidad_estudiantes,dtype=float)
    
    for c in range(cantidad_estudiantes):
        array_estudiante[c] = input(f"\nIntroduzca el nombre del estudiante {c+1}: ")
        while True:
            array_calif[c] = leer_float_mayor0(f"Introduzca la calificación del estudiante {array_estudiante[c]}:")
            if( array_calif[c] > 100):
                beep_error()
                print("Error! La calificación no puede ser mayor que 100. Intente de nuevo.\n")
            else: break
    
    calif_promedio = sum(array_calif) / cantidad_estudiantes
    calif_maxima = array_calif.max()
    calif_minima = array_calif.min()
    
    aprobados = 0
    reprobados = 0
    for i in range(array_calif.size):
        if (array_calif[i] >= 70):
            aprobados += 1
        else:
            reprobados += 1
    
    CLS()
    
    print("Listado de alumnos")
    print("="*30)

    for j in range(array_estudiante.size):
        # print(nombres[x], "->",calificaciones[x])
        print(f"{array_estudiante[j][0:20]:<23} ->{array_calif[j]:>5}")
    
    print("="*30)
    
    print()
    print(f"Calificacion promedio:  {calif_promedio:>5.2f}")
    print(f"Calificacion máxima:    {calif_maxima:>5}")
    print(f"Calificacion mínima:    {calif_minima:>5}")
    print(f"Cantidad de aprobados:  {aprobados:>5}")
    print(f"Cantidad de reprobados: {reprobados:>5}")
    print()
    
    print("Alumnos con la calificación máxima")
    print("="*30)
    for k in range(array_estudiante.size):
        if (array_calif[k] == calif_maxima):
            print(array_estudiante[k])
    print("="*30)
    print()
    
    print("Alumnos con la calificación mínima")
    print("="*30)
    for k in range(array_estudiante.size):
        if (array_calif[k] == calif_minima):
            print(array_estudiante[k])
            
    print("="*30)
    
    if(str(input("\n¿Desea repetir el programa? ('Si' para confirmar): ").upper()[0]) != "S"): break