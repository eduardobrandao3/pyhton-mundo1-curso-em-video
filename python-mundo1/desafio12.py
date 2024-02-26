#DESAFIO 12
#ler preço de um produto e mostrar novo preço com 5% de desconto
preço = float(input('Digite o preço do produto: R$'))
print('O produto que custava R${0} com o desconto de 5% passa a custar R${1:.2f}'.format(preço, (preço*0.95)))