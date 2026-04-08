print("Descubra os números que são multiplos de 3 e 5 apatir do número de sua preferência")
num = int(input("Digite o número que você deseja comparar: "))

multiplos = 0
for numero in range(1,num +1):
    if numero % 3 == 0 and numero % 5 == 0:
        multiplos += 1


print(f"Múltiplos de 3 e 5: {multiplos}")


