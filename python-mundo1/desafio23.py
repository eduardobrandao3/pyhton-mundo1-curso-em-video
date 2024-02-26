'''DESAFIO 23
Leia um numero de 0 a 9999 e mostre na tela cada um dos dígitos separados'''


#USANDO MATEMÁTICA
n = int(input('Digite um numero entre 0 e 9999: '))
milhar = n//1000
Rmilhar = n%1000
centena = Rmilhar//100
Rcentena = Rmilhar % 100
dezena = Rcentena // 10
Rdezena = Rcentena % 10
unidade = Rdezena 
print('unidade: {}'.format(unidade))
print('dezena: {}'.format(dezena))
print('centena: {}'.format(centena))
print('milhar: {}'.format(milhar))
