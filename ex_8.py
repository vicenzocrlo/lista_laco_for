soma = 0

for nota in range(1, 6):
    notas = float(input(f"Digite a sua nota {nota}: "))
    soma +=notas
    media = soma / 5
print(f"A média das suas notas é: {media}")


