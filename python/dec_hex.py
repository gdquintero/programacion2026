# Decimal a hexadecimal

# Lista con los digitos del sistema hexadecimal
key = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

decimal = 123456
hexadecimal = []

while decimal > 0:
    # Vamos agregando los restos en binario al dividir entre 16
    hexadecimal.append(key[decimal % 16])
    decimal //= 16

# Cambiar orden
hexadecimal.reverse()

# Imprimir resultado
print(f"El numero en binario es {hexadecimal}")
