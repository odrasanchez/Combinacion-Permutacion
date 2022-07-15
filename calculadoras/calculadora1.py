# Librerias utilizadas
import math
from itertools import product


# Definicion de la funcion Main, aquí se encuentra la solicitud de datos y llamado de funciones
def main():
    op = int(input("Bienvenido, seleccione la operacion a trabajar: \n1. Combinacion ordinaria\n2. Permutacion SIN REPETICION\n3. Permutacion CON REPETICION\n\n"))

    if op == 1:
        n = int(input('Ingrese el valor de n: '))
        m = int(input('Ingrese el valor de m: '))
        # Condicional solicitado por la formula
        if m > n:
            return print("El valor no es valido, ya que n debe ser mayor que m")
        # Llamando a la funcion con las variables recibidas
        operations_comb(n, m)

    elif op == 2:
        n = int(input('Ingrese el valor de n: '))
        k = int(input('Ingrese el valor de k: '))
        # Condicional solicitado por la formula
        if k > n:
            return print("El valor no es valido, ya que n debe ser mayor que k")
        # Llamando a la funcion con las variables recibidas
        operations_permu(n, k)
        
    elif op == 3:
        r = int (input('Ingrese el valor de repeticion:'))
        cadena = input('Ingrese la cadena a usar, sin espacios ni coma:')
        if r == 0:
            return print("El valor no es valido, es una cadena vacía")
        # Llamando a la funcion con las variables recibidas
        opertations_permuPR(cadena,r)
        
    else:
        # Condicional del menu
        print("La opcion no es valida")



    
# Formato de combinaciones
def final_format (n, m, resul):
    print(f"""
                            {n}!
          {n}C{m} = ------------------ = {resul}
                     {m}! ({n} - {m})!
          """)
          
# Formato de permutacion sin repeticion
def format_permut (n, k, resul):
    print(f"""
            {n}        {n}!
          P {k} = ------------------ = {resul}
                    ({n} - {k})!
          """)


# COMBINACIONES
def operations_comb (n, m):
    n_factorial = n
    m_factorial = m
    n_m_factorial = n-m
    
    # La condicion nos permite indicar que las variables son iguales
    if n == m:
        return final_format(n, m, 1.0)
    
    # Nos permite generar la multiplicacion factorial desde 1 hasta n 
    for i in range(1,n):
        n_factorial *= i
    
    # Nos permite generar la multipliacion factorial desde 1 hasta m
    for i in range(1,m):
        m_factorial *= i
    
    # Nos permite generar la multiplicación del factorial desde 1 hasta (n-m)
    for i in range(1, n - m):
        n_m_factorial *= i
    
    # Finalmente realizamos las operaciones basicas de division y multiplicacion
    resul = n_factorial / (m_factorial * n_m_factorial)
    
    # Funcion para formato en pantalla
    final_format(n, m, resul)




# Funcion de permutaciones SIN REPETICION usando librerias 
def operations_permu(n, k):
    if n == k:
        resul = math.factorial(n)
       
    else : 
        resul = math.factorial(n) / math.factorial(n - k)
    
    # Funcion para formato en pantalla
    format_permut (n, k, resul)
    
    
# Funcion de permutaciones CON REPETICION usando librerias
def opertations_permuPR(cadena, r):
    caracteres = list(cadena)
    permutaciones = []
    
    for i in product(caracteres, repeat = r):
        permutaciones.append(i)
    
    print("Cantidad de permutaciones: %i" %len(permutaciones))
    print(permutaciones)
       
    
    
# Esta linea indica si todo lo que se realiza se encuentra dentro del main
# para la ejecucion del programa
if __name__ == '__main__':
    main()
