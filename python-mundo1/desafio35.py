'''DESAFIO 35
Leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo'''

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('As retas {}, {} e {} \033[1;32mPODEM\033[m formar um triângulo'.format(r1, r2, r3))
else: 
    print('As retas {}, {} e {} \033[1;31mNÃO\033[m podem formar um triângulo'.format(r1, r2, r3))