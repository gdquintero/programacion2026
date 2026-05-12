# Decimal a binario 

n = 123

# Lista que almacena los digitos 0 y 1
binario = []

while n > 0:
    # Vamos agregando los restos en binario al dividir entre 2
    binario.append(n % 2)
    n //= 2

# Cambiando el orden de la lista
binario.reverse()

# Imprimiendo resultado
print(f"El numero en binario es {binario}")