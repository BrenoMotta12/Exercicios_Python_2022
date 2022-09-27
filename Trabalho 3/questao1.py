# Faça um programa que leia vários inteiros positivos
# e mostre, no final, a soma dos números pares e a soma dos números ímpares.
# O programa para quando entrar um número maior que 1000

numeros_impares = 0
numeros_pares = 0
entrada = int(input('Digite um numero inteiro positivo (O programa encerra com numero maior que 1000): '))

while entrada <= 1000:
    if entrada % 2 == 0:
        numeros_pares += entrada
    else:
        numeros_impares += entrada
    entrada = int(input())

print(f'A soma dos numeros pares é: {numeros_pares}\n'
      f'A soma dos numeros impares é: {numeros_impares}')
