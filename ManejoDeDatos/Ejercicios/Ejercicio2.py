'''
1. 
Deben hacer un programa que al correrlo imprima lo siguiente:
"   *   " 
"  ***  "  
" ***** "  
"*******"  
"   *   "  
"   *   " 
Un "pino" o "árbol de navidad" hecho de "*". 
La base del triángulo debe tener 7 "*" de largo, la punta y la base estar al centro. 
Esto hecho con lo que hemos visto, de preferencia sólo poner un print(x) en el programa, y que sea "x" lo que vaya cambiando.

2. 
El siguiente paso es comprobar que el programa funcione si cambias el 7 a otro número como 9 u 11, por ejemplo. 

'''

# Fila = n
n = 6

# Tronquito
j = n-2

for i in range(0, n):
    if i >= 0 and i < j:
        print(" " * (n-i-1) + "*" * (2*i+1))
    else:
        print(" " * (n-1) + "*")

# HACER CORRECCIONES






