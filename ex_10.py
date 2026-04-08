print("======Calculadora de Fatorial=====")
numero = int(input("Digite o número que deseja calcular o fatorial: "))

fatorial = numero

for i in range(numero-1,1,-1):
    fatorial *= i
    print(f"{numero} x {i}")
print(f"O valor de {numero} fatorial é: {fatorial}")