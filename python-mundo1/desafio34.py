'''DESAFIO 34
Pergunte o salário de um funcionário e calcule o valor do seu aumento
para salários superiores a 1250 calcule aumento de 10% para os inferiores ou iguais o aumento é de 15%'''

salario = float(input('Digite seu salário: R$'))
cores = {'limpa':'\033[m', 'verde':'\033[32m', 'vermelho':'\033[31m'}
if salario > 1250:
    novoSal = 1.1*salario
    aumento = 10
else:
    novoSal = 1.15*salario
    aumento = 15
print('Seu salario antes era {5}R${0:.2f}{3} e com o aumento de {4}{1}%{3} passa a ser {4}R${2:.2f}{3}'.format(salario, aumento, novoSal, cores['limpa'], cores['verde'], cores['vermelho']))