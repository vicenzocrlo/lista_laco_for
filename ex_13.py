num = int(input("Digite o número que deseja somar: "))

par = 0
impar = 0 
for numero in range(1, num +1):
    if numero % 2 ==0:
        par += numero
    else:
        impar += numero

print(f"A soma dos números pares até {num} é: {par}")
print(f"A soma dos números impares até {num} é: {impar}")

