num = int(input("Digite o número que você deseja verificar se é primo ou não: "))

primo = True
if num <= 1:
    primo = False

else:
    for numero in range(2,num):
        if num % numero == 0:
            primo = False
            break

if primo:
    print(f"O número {num} é primo!")
else:
    print(f"O número {num} não é primo!")


