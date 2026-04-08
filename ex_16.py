print("=====Contagem de Múltiplos de 3 a 5=====")
num = int(input("Digite o número que você deseja comparar: "))

multiplos_3 = 0
multiplos_5 = 0
for numero in range(1,num +1):
    if numero % 3 == 0 and numero % 5 == 0:
        multiplos_3 += 1
        multiplos_5 += 1

    elif numero % 3 == 0:
        multiplos_3 += 1

    elif numero % 5 == 0:
        multiplos_5 += 1

print(f"Múltiplos de 3: {multiplos_3}")
print(f"Múltiplos de 5: {multiplos_5}")

