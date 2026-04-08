print("Digite 5 números para descobir qual deles é o maior e o menor")
maior = 0
menor = 0
for numero in range(1, 6):
    num = int(input(f"Digite o {numero}º número que deseja analisar: "))
    if num < menor or menor == 0:
            menor = num
    
    elif num > maior:
        maior = num

print(f"O maior número dentre os cinco é: {maior}")
print(f"O menor número dentre os cinco é: {menor}")
