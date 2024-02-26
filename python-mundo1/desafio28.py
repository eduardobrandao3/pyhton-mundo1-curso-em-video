'''DESAFIO 28
peça para o computador "pensar" em um nº de 0 a 5 e peça para o usuário tentar acertar
escreva se o usuário ganhou ou perdeu'''

from random import randint 
from time import sleep
num = randint(0, 5)
print('-='*30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-='*30)
escolha = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if num == escolha:
    print('Você escolheu o número {} e eu também.'.format(escolha))
    print('\033[32mParabéns! VOCÊ GANHOU!')
else:
    print('Você escolheu o número {} e eu escolhi o número {}'.format(escolha, num))
    print('\033[31mEu vencei!')