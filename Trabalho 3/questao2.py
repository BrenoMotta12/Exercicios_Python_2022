# Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
# Dada a massa inicial, em gramas, fazer um programa em Python que calcule o tempo
# necessário para que essa massa se torne menor que 0,5 grama. O programa deve escrever
# na tela a massa inicial, a massa final e o tempo calculado em horas, minutos e segundos.

massa_inicial = float(input('Digite o peso(gramas) do material: '))
massa = massa_inicial
tempo = 0


while massa >= 0.5:
    massa = massa / 2
    tempo += 50

segundos = tempo
segundos = segundos % (24 * 3600)
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print(f'A massa inicial foi de {massa_inicial:.0f} gramas\n'
      f'A massa final foi de {massa:.2f} gramas\n'
      f'O tempo necessário foi de {horas}h {minutos}m {segundos}s\n')
