import random

print("===== Jogo de Adivinhação =====")

numero_secret = random.randint(1,10)

for chances in range(1,4):
    tent_1 = int(input("Digite o seu primeiro chute de um número entre 1 a 10, você tem 3 tentativas: "))
    if tent_1 < numero_secret:
        print(f"Tente outra vez, o número secreto é maior que {tent_1}")
    elif tent_1 > numero_secret:
        print(f"Tente outra vez, o número secreto é menor que {tent_1} ")
    elif tent_1 == numero_secret:
        print(f"Parabéns! Você acertou o número, ele corresponde a {numero_secret}")

