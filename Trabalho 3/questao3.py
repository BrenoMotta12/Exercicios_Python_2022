# Dado um país A, com 5000000 de habitantes e uma taxa de natalidade de
# 3% ao ano, e um país B com 7000000 de habitantes e uma taxa de natalidade
# de 2% ao ano, escrever um programa que seja capaz de calcular e mostrar o
# tempo necessário para que a população do país A ultrapasse a população do país B.

a = 5000000
b = 7000000
anos = 0

while b >= a:
    a += a * 0.03
    b += b * 0.02
    anos = anos + 1

print(f'Levara {anos} anos para a população A ultrapassar a população B')
