import numpy as np
import os 

# Limpiar pantalla
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def leer_vector(n):

    # Definiendo un vector nulo de dimension n 
    x = np.zeros(n)

    for i in range(n):
        x[i] = float(input(f"Componente {i+1}: "))

    return x

def leer_matriz(m,n):
    # Definiendo la matriz de m filas y n columnas

    matriz = np.zeros((m,n))

    for i in range(m):
        for j in range(n):
            matriz[i,j] = float(input(f"Componente {i+1,j+1}: "))

    return matriz

def producto_punto(x,y,n):
    res = 0

    for i in range(n):
        res += x[i] * y[i]

    return res

def producto_cruz(x,y):
    res = np.zeros(3)
    res[0] = x[1] * y[2] - x[2] * y[1]
    res[1] = x[2] * y[0] - x[0] * y[2]
    res[2] = x[0] * y[1] - x[1] * y[0]

    return res

def norm2(x,n):
    res = 0

    for i in range(n):
        res += x[i]**2

    return np.sqrt(res)

def norm1(x,n):
    res = 0

    for i in range(n):
        res += np.abs(x[i])

    return res

def norm_inf(x,n):
    res = np.abs(x[0])

    for i in range(1,n):
        aux = np.abs(x[i])

        if res < aux:
            res = aux
    
    return res

def producto_matricial(A,B,m,n,p):
    res = np.zeros((m,p))

    for i in range(m):
        for j in range(p):
            res[i,j] = producto_punto(A[i,:],B[:,j],n)

    return res

# Menus
def mostrar_menu_principal():
    limpiar()
    print("\n====== MENU PRINCIPAL ======")
    print("1. Operaciones aritmeticas")
    print("2. Operaciones con vectores")
    print("3. Operaciones con matrices")
    print("0. Salir")
    print("===========================")

def mostrar_menu_operaciones_aritmeticas():
    limpiar()
    print("\n====== Operaciones aritmeticas ======")
    print("1. Adicion de dos numeros")
    print("2. Multiplicacion de dos numeros")
    print("3. Potencia de un numero")
    print("0. Volver al menu principal")
    print("===========================")

def mostrar_menu_operaciones_vectores():
    limpiar()
    print("\n====== Operaciones con vectores ======")
    print("1. Adicion de dos vectores")
    print("2. Producto punto de dos vectores")
    print("3. Producto cruz de dos vectores")
    print("4. Norma 2 de un vector")
    print("5. Norma 1 de un vector")
    print("6. Norma infinito de un vector")
    print("0. Volver al menu principal")
    print("===========================")

def mostrar_menu_operaciones_matrices():
    limpiar()
    print("\n====== Operaciones con matrices ======")
    print("1. Adicion de dos matrices")
    print("2. Multiplicacion de dos matrices")
    print("3. Transpuesta de una matriz")
    print("0. Volver al menu principal")
    print("===========================")

# Operaciones aritmeticas
def menu_aritmetica():
    while True:
        mostrar_menu_operaciones_aritmeticas()
        op = int(input("Elije una opcion: "))

        if op == 1:
            a = float(input("Numero 1: "))
            b = float(input("Numero 2: "))  

            print(f"La adicion es {a + b}")
            input("\nPresiona Enter para continuar...")

        elif op == 2:
            a = float(input("Numero 1: "))
            b = float(input("Numero 2: "))

            print(f"La multiplicacion es {a * b}")
            input("\nPresiona Enter para continuar...")

        elif op == 3:
            a = float(input("Base: "))
            b = float(input("Exponente: "))

            print(f"{a} elevado a la {b} es {a ** b}")
            input("\nPresiona Enter para continuar...")

        elif op == 0:
            break

        else: 
            print("Opcion no valida")
            input("\nPresiona Enter para continuar...")

# Operaciones con vectores
def menu_vectores():
    while True:
        mostrar_menu_operaciones_vectores()

        op = int(input("Elije una opcion: "))

        if op == 1:
            n = int(input("Escribe la dimension: "))

            print("\nComponentes del primer vector")
            x = leer_vector(n)

            print("\nComponentes del segundo vector")
            y = leer_vector(n)

            print(f"La adicion es {x + y}")
            input("\nPresiona Enter para continuar...")

            del x
            del y

        elif op == 2:
            n = int(input("Escribe la dimension: "))

            print("\nComponentes del primer vector")
            x = leer_vector(n)

            print("\nComponentes del segundo vector")
            y = leer_vector(n)

            print(f"\nEl producto punto es {producto_punto(x,y,n)}")
            input("\nPresiona Enter para continuar...")

            del x
            del y

        elif op == 3:

            print("\nComponentes del primer vector")
            x = leer_vector(3)

            print("\nComponentes del segundo vector")
            y = leer_vector(3)

            cross = producto_cruz(x,y)

            print(f"\nEl producto cruz es {cross}")
            input("\nPresiona Enter para continuar...")

            del x
            del y
            del cross

        elif op == 4:
            n = int(input("Escribe la dimension del vector: "))
            
            print("\nComponente del vector")

            x = leer_vector(n)

            print(f"La norma euclidiana es {norm2(x,n)}")
            input("\nPresiona Enter para continuar...")

            del x

        elif op == 5:
            n = int(input("Escribe la dimension del vector: "))
            
            print("\nComponente del vector")

            x = leer_vector(n)

            print(f"La norma 1 es {norm1(x,n)}")
            input("\nPresiona Enter para continuar...")

            del x

        elif op == 6:
            n = int(input("Escribe la dimension del vector: "))
            
            print("\nComponente del vector")

            x = leer_vector(n)

            print(f"La norma infinito es {norm_inf(x,n)}")
            input("\nPresiona Enter para continuar...")

            del x

        elif op == 0:
            break

        else:
            print("Opcion no valida")
            input("\nPresiona Enter para continuar...")

def menu_matrices():
    while True:
        mostrar_menu_operaciones_matrices()

        op = int(input("Elije una opcion: "))

        if op == 1:
            m = int(input("Escribe m: "))
            n = int(input("Escribe n: "))
            p = int(input("Escribe p: "))

            print("\nComponentes de la primera matriz")
            A = leer_matriz(m,n)

            print("\nComponentes de la segunda matriz")
            B = leer_matriz(n,p)

            print(f"La adicion es\n \n{A + B}")
            input("\nPresiona Enter para continuar...")

            del A
            del B

        # elif op == 2:
        #     n = int(input("Escribe la dimension: "))

        #     print("\nComponentes del primer vector")
        #     x = leer_vector(n)

        #     print("\nComponentes del segundo vector")
        #     y = leer_vector(n)

        #     print(f"\nEl producto punto es {producto_punto(x,y,n)}")
        #     input("\nPresiona Enter para continuar...")

        #     del x
        #     del y

        # elif op == 3:

        #     print("\nComponentes del primer vector")
        #     x = leer_vector(3)

        #     print("\nComponentes del segundo vector")
        #     y = leer_vector(3)

        #     cross = producto_cruz(x,y)

        #     print(f"\nEl producto cruz es {cross}")
        #     input("\nPresiona Enter para continuar...")

        #     del x
        #     del y
        #     del cross
  

        elif op == 0:
            break

        else:
            print("Opcion no valida")
            input("\nPresiona Enter para continuar...")

        

# Menu principal
while True:
    mostrar_menu_principal()
    op = int(input("Elije una opcion: "))

    if op == 1:
        menu_aritmetica()

    elif op == 2:
        menu_vectores()

    elif op == 3:
        menu_matrices()

    elif op == 0:
        limpiar()
        print("Hasta luego !!!")
        break
    
    else:
        print("Opcion no valida. Intenta de nuevo")
        input("\nPresiona Enter para continuar...")