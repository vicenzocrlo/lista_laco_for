num = int(input("Digite um número que deseja descobrir a tabuada ou se é múltiplo de 3: "))

multiplo =("")
for i in range(1,11):
    if num % 3 == 0:
        multiplo = ("Múltiplo de 3")
    else:
        tabuada = num * i 
        print(f"{num} x {i} = {tabuada}")

print(multiplo)

