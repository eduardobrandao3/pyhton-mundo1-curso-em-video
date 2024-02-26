'''DESAFIO 25
Crie um programa q leia o nome de uma pessoa e diga se ela tem "SILVA" no nome'''

nome = str(input('Digite seu nome completo: '))
print('{} tem "SILVA" no nome: {}'.format(nome, ('SILVA' in nome.upper())))