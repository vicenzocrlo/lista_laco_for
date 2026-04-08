maior = 0
menor = 0
for numero in range(1, 6):
    num = int(input(f"Digite o {numero} número que deseja analisar: "))
    if num < menor or menor == 0:
            menor = num
    
    elif num > maior:
        maior = num

print(maior)
print(menor)
