'''DESAFIO 27
leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente'''

nome = str(input('Digite o nome completo: ')).strip()
dividido = nome.split()
tamDividido = len(dividido)
print('O primeiro nome é {} e o último nome é {}'.format(dividido[0], dividido[tamDividido - 1]))

