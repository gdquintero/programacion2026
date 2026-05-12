import numpy as np
import os 

# Limpiar pantalla
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def mostrar_menu_operaciones_vectores():
    limpiar()
    print("\n====== Operaciones con vectores ======")
    print("1. Adicion de dos vectores")
    print("2. Producto punto de dos vectores")
    print("3. Producto cruz de dos vectores")
    print("4. Norma 2 de un vector")
    print("0. Volver al menu principal")

def mostrar_menu_operaciones_matrices():
    limpiar()
    print("\n====== Operaciones con matrices ======")
    print("1. Adicion de dos matrices")
    print("2. Multiplicacion de dos matrices")
    print("3. Transpuesta de una matriz")
    print("0. Volver al menu principal")

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

# Menu vectores
def menu_vectores():
    while True:
        mostrar_menu_operaciones_vectores()

        op = int(input("Elije una opcion: "))

        if op == 1:
            n = int(input("Escribe la dimension de los vectores: "))
            x = np.zeros(n)
            y = np.zeros(n)

            print("\nEscribe cada componente del primer vector")

            for i in range(n):
                x[i] = float(input(f"x_{i}: "))

            print("\nEscribe cada componente del segundo vector")

            for i in range(n):
                y[i] = float(input(f"y_{i}: "))

            print(f"La adicion es {x + y}")
            input("\nPresiona Enter para continuar...")

        elif op == 2:
            n = int(input("Escribe la dimension de los vectores: "))
            x = np.zeros(n)
            y = np.zeros(n)

            print("\nEscribe cada componente del primer vector")

            for i in range(n):
                x[i] = float(input(f"x_{i}: "))

            print("\nEscribe cada componente del segundo vector")

            for i in range(n):
                y[i] = float(input(f"y_{i}: "))

            print(f"El producto punto es {np.dot(x,y)}")
            input("\nPresiona Enter para continuar...")

        elif op == 3:
            n = int(input("Escribe la dimension de los vectores: "))
            x = np.zeros(n)
            y = np.zeros(n)

            print("\nEscribe cada componente del primer vector")

            for i in range(n):
                x[i] = float(input(f"x_{i}: "))

            print("\nEscribe cada componente del segundo vector")

            for i in range(n):
                y[i] = float(input(f"y_{i}: "))

            print(f"El producto cruz es {np.cross(x,y)}")
            input("\nPresiona Enter para continuar...")

        elif op == 4:
            n = int(input("Escribe la dimension del vector: "))
            x = np.zeros(n)
            print("\nEscribe cada componente del primer vector")

            for i in range(n):
                x[i] = float(input(f"x_{i}: "))

            print(f"La norma euclidiana es {np.linalg.norm(x)}")
            input("\nPresiona Enter para continuar...")

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

    elif op == 0:
        limpiar()
        print("Hasta luego !!!")
        break
    
    else:
        print("Opcion no valida. Intenta de nuevo")
        input("\nPresiona Enter para continuar...")