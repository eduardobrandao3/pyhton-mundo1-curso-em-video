#DESAFIO 19
#um professor quer sortear um dos seus quatro alunos. Leia os nomes e faça um sorteio
from random import choice
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
listaAlunos = [aluno1, aluno2, aluno3, aluno4]
sorteado = choice(listaAlunos)
print('O aluno sorteado para apagar o quadro foi: {}'.format(sorteado))