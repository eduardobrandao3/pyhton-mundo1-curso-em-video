'''DESAFIO 31
Pergunta a distancia de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
e R$0,45 para viagens mais longas'''

dist = float(input('Digite a distância da viagem em km: '))
if dist <= 200:
    preco = 0.5*dist
else:
    preco = 0.45*dist
print('O valor da passagem é R${:.2f}'.format(preco))

