print("=====Soma dos dígitos======")
num = (input("Digite um número inteiro: "))

soma = 0
for digito in num: 

    if digito.isdigit():
        soma += int(digito)

print(f"A soma dos dígitos {num} é: {soma}")

