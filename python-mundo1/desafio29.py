'''DESAFIO 29
leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada km acima do limite'''

vel = float(input('Digite a velocidade do carro em km/h: '))
if vel > 80:
    print('\033[31mVocê foi multado! O valor da multa é: R${:.2f}\033[m'.format((vel-80)*7))
print('\033[32mTenha um bom dia! Dirija com segurança!')
