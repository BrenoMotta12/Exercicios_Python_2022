import random
import string

caracteres = string.ascii_letters + string.digits
tamanho_senha = int(input('Digite o número de caracteres desejado para sua senha: '))
senha = ''
for i in range(tamanho_senha):
    senha += random.choice(caracteres)

print(''.join(senha))
