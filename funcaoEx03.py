print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")
#Crie um jogo de par ou impar onde o computador irá gerar um numero aleatório e o usuario irá digitar um número
#Após digitar um número.Após digitar o número, o programa irá utilizar um vetor para resolver 
#o jogo Se a soma dos números for par,o usuario vence.Se for impar,o computador vence.

import random
def game(numero):
    player2=random.randint(0,5)
    print(f'Player1: {numero} vs Player2: {player2}')
    if(numero+player2)%2==0:
        return 'PAR - Player1 Venceu'
    else:
        return 'ÍMPAR - Player2 Venceu'

print('Jogo - Par ou Ímpar')
print('Números permitidos - 0, 1, 2, 3, 4 ou 5 ')
print()
print('------------------------------------')
print()

jogadas=int(input('quantas vezes deseja jogar?: '))

for i in range (jogadas):
    player1=int(input('Insira sua jogada!: '))
    print(f'{game(player1)}')


