#DESAFIO 15
#pergunte quantidade de km rodados e quantidade de dias alugados. Calcule preço a pagar. Sabendo que custa R$60,00 por dia e R$0,15 por km

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
total = ((dias*60) + (km*0.15))
print('O total a pagar é R${:.2f}'.format(total))