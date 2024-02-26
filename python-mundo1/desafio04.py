#DESAFIO 4
#usuário digita algo, fale o tipo primitivo e informações sobre
entrada = input('Digite algo: ')
print('Tipo primitivo: {}'.format(type(entrada)))
print('É um numero: {}'.format(entrada.isnumeric()))
print('É alfabeto: {}'.format(entrada.isalpha()))
print('Está tudo em maiúsculo: {}'.format(entrada.isupper()))
print('Está tudo em minúsculo: {}'.format(entrada.islower()))
print('É espaço: {}'.format(entrada.isspace()))
print('É alfa-numérico: {}'.format(entrada.isalnum()))
print('Está capitalizada: {}'.format(entrada.istitle()))

