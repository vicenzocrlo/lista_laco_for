print("Vamos realizar uma contagem totalmente personalizada? Escolha as seguintes opções abaixo: \n")

inicio = int(input("Digite o número de início da contagem: "))
fim = int(input("Digite o número de fim da contagem: "))
passo = int(input("Digite o incremento/passo da contagem: "))

for i in range(inicio, fim + 1, passo):
    print(i)