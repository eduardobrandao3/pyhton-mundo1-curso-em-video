'''DESAFIO 32
leia um ano qualquer e mostre se ele é bissexto'''

from datetime import date
ano = int(input('Digite o ano, se quiser o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if (((ano%100) != 0) and ((ano%4) == 0)) or ((ano%400) == 0):
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} NÃO é bissexto'.format(ano))


