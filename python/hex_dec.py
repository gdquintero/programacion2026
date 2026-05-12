# Hexadecimal a decimal

# Lista con los digitos del sistema hexadecimal
key = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

hexadecimal = [7,5,"B","C","D",1,5]

# Variable para almacenar la suma
decimal = 0

# Cantidad de digitos del hexadecimal
k = len(hexadecimal)

# Sumatoria
for i in range(k):
    decimal += key.index(hexadecimal[i]) * (16 ** (k - i - 1))

# Resultado
print(decimal)