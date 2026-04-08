num = (input("Digite um número inteiro de sua preferência: "))

soma = 0

for digito in num: 

    if digito.isdigit():
        print(num)
        soma += int(digito)

print(f"A soma dos dígitos {num} é: {soma}")

