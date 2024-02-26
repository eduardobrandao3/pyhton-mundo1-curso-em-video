#DESAFIO 18
#ler um angulo qualquer e mostrar o valor do seno, cosseno e tangente desse ângulo
from math import radians, sin, cos, tan 
angulo = float(input('Digite o valor do angulo em graus: '))
angRad = radians(angulo)
seno = sin(angRad)
cosseno = cos(angRad)
tang = tan(angRad)
print('O seno do angulo {0} vale {1:.2f}\nO cosseno do angulo {0} vale {2:.2f}\nA tangente do angulo {0} vale {3:.2f}'.format(angulo, seno, cosseno, tang))