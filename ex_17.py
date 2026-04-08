print("====Calculadora de paridade dos números=====")

num = int(input("Digite o número que deseja verificar: "))

for numero in num:
    if numero % 2 == 0:
        par = numero / 2
        print(par)
    else:
        impar = numero * 3
        print(impar)
        