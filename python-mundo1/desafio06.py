#DESAFIO 6
#ler um numero e mostrar o seu dobro, triplo e raiz quadrada
num = int(input('Digite um valor: '))
print('O dobro de {0} é: {1}\nO triplo de {0} é: {2}\nA raiz quadrada de {0} é: {3:.2f}'.format(num, (num*2), (num*3), (num**(1/2))))