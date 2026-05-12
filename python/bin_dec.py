# Binario a decimal
binario = [1,1,0,0,0,0,0,0,1,1,1,0,0,1]

# Variable para almacenar la suma
decimal = 0

# Cantidad de digitos del binario
k = len(binario)

# Sumatoria
for i in range(k):
    decimal += binario[i] * (2 ** (k - i - 1))

# Resultado
print(decimal)