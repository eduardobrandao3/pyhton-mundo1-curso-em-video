'''DESAFIO 26
Leia uma frase e mostre quantas vezes aparece a letra "A" em que posição ela aparece pela primeira vez e em que posição ela parece pela ultima vez'''

frase = str(input('Digite uma frase: ')).strip()
qntA = frase.upper().count('A')
print('A letra "A" aparece {} vezes'.format(qntA))
print('A letra "A" aprece pela primeira vez na posição {}'.format(frase.upper().find('A') + 1))
print('A letra "A" aparece pela última vez na posição {}'.format(frase.upper().rfind('A') + 1))

