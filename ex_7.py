print("==========Tabuada automática============")
num = int(input("Digite o número que deseja descobrir a tabuada: "))

for i in range(1, 11):
    tabuada = num * i
    print(f"{num} x {i} = {tabuada}")


