#DESAFIO 20
#mesmo professor do desafio 19 agora quer sortear a ordem de apresentação. Leia nome dos 4 alunos e sorteie a ordem de apresentação

from random import shuffle
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))
