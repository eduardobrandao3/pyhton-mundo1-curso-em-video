#DESAFIO 17
#ler comprimento dos catetos, calcule e mostre valor da hipotenusa

#from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjascente: '))
hip = ((co**2) + (ca**2))**(1/2)
print('O valor da hipotenusa é {:.2f}'.format(hip))

'''
h = math.hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(h))'''
