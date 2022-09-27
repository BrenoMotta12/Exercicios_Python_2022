# ATIVIDADE 1: Faça um programa que receba três valores e os imprima na tela em ordem
# decrescente depois em ordem crescente.

numeros = input('Digite 3 valores separados por virgula(ex: 1,2,3): ')
lista_numeros = numeros.split(',')

lista_numeros.sort(reverse=True)
print(f'Números em ordem decrescente: {"-".join(lista_numeros)}')

lista_numeros.sort()
print(f'Números em ordem crescente: {"-".join(lista_numeros)}')


# ATIVIDADE 2: Faça um programa que receba o dia e o mês e informe o próximo dia,
# por exemplo você recebeu dia 30 e mês 3, você imprimirá na tela 31. Um segundo
# exemplo: você recebeu valor d dia 30 e de mês 4, o próximo dia é 1, que seria 01/05.
# (Ignore o fato de haver anos bissextos)

dia = int(input("Informe o dia: "))
mes = int(input("informe o mês: "))

if dia == 31 and mes in [1, 3, 5, 7, 8, 10, 12] \
        or dia == 30 and mes in [4, 6, 9, 11] \
        or dia == 28 and mes == 2:
    if mes == 12:
        print('Amanhã é dia 1/1')
    else:
        print(f'Amanhã é dia 1/{mes + 1}')
else:
    print(f'Amanhã é dia {dia+1}/{mes}')


# ATIVIDADE 3: Resolva o problema anterior considerando o fato de haver anos bissextos.
dia = int(input("Informe o dia: "))
mes = int(input("informe o mês: "))

if mes == 2:
    ano = input('O ano é bissexto?(S ou N): ')
    if ano.upper() == 'S':
        if dia == 29:
            print('Amanha é dia 1/3')
        else:
            print(f'Amanha é dia {dia+1}/2')
    else:
        if dia == 28:
            print('Amanha é dia 1/3')
        else:
            print(f'Amanha é dia {dia+1}/2')
else:
    if dia == 31 and mes in [1, 3, 5, 7, 8, 10, 12] \
            or dia == 30 and mes in [4, 6, 9, 11]:
        if mes == 12:
            print('Amanhã é dia 1/1')
        else:
            print(f'Amanhã é dia 1/{mes+1}')
    else:
        print(f'Amanhã é dia {dia+1}/{mes}')
