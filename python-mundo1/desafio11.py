#DESAFIO 11
#ler largura e altura de uma parede em metros, calcule a área e qnt de tinta necessária para pintar. 1L pinta 2m²
h = float(input('Digite a altura da parede em metros: '))
l = float(input('Digite a largura da parede em metros: '))
area = h*l
print('A área da parede é {0}m² e você precisará de {1} litros de tinta'.format(area, (area/2)))