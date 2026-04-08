print("\nEscolha 10 números para verificar se é positivo, negativo ou zero")
zero = 0
positivo = 0 
negativo = 0
for numero in range(1, 11):
    num = float(input(f"Digite o seu {numero}º número: "))

    if num == 0:
        zero += 1
    elif num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1

print(f"Os seus números correspondem à: {positivo} positivos, {negativo} negativos e {zero} zeros")
