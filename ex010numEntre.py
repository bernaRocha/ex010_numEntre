#Faça um programa que receba dois números inteiros
# e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite o outro número: "))

for x in range(num1, num2):
    print(x, end='  ')
