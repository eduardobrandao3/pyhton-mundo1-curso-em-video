#DESAFIO 10
#ler qnt dinheiro q usuário tem na carteira e mostre quantos dólares ela pode comprar. considere US$1 = R$4,94
real = float(input('Quantos reais você tem? '))
dolar = real/4.94
print('Com R${0} você pode comprar US${1:.2f}'.format(real, dolar))
