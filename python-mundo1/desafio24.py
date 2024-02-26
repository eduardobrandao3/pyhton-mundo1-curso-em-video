'''DESAFIO 24
Leia nome de uma cidade e diga se ela começa ou não com nome "SANTO"'''

nome = str(input('Digite o nome da cidade: ')).strip()
dividir = nome.split()
print('O nome da cidade começa com "SANTO": {}'.format('SANTO' in dividir[0].upper()))
