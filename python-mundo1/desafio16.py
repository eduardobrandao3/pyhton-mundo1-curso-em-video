'''DESAFIO 16
ler numero real e mostre na tela a sua porção inteira
ex.: digite um numero: 6.127
o numero 6.127 tem a parte inteira 6'''

from math import trunc

num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))
