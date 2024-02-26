'''DESAFIO 22
ler nome completo de uma pessoa e mostre:
nome com todas as letras maiusculas
nome com todas as letras minusculas
quantas letras ao todo sem considerar espaços
quantas letras tem o primeiro nome'''

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas: {}'.format(nome.lower()))
dividir = nome.split()
juntar = ''.join(dividir)
tamanho = len(juntar)
print('Total caracteres sem contar espaços: {}'.format(tamanho))
print('A quantidade de letras do primeiro nome é {}'.format(len(dividir[0])))
