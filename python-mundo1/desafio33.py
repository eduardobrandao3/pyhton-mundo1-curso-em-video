'''DESAFIO 33
leia 3 números e mostre qual é o maior e qual é o menor'''

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
maior = n1
menor = n1
if (n2 > n3) and (n2 > n1):
    maior = n2
if (n3 > n2) and (n3 > n1):
    maior = n3
if (n2 < n3) and (n2 < n1):
    menor = n2
if (n3 < n2) and (n3 < n1):
    menor = n3

print('Os números digitados foram: {}, {} e {}\nO maior é {}\nO menor é {}'.format(n1, n2, n3, maior, menor))
