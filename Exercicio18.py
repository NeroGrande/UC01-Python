print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

player1=input('Escolha sua opção enre Pedra, Papel e Tesoura:')
player2=input('Escolha sua opção enre Pedra, Papel e Tesoura')

if(player1==player2):
    print('Empate')

elif((player1=='pedra'and player2== 'Tesoura') or (player1=='Papel' and player2=='Pedra') or (player1=='Tesoura' and player2=='Papel')):
    print(f'Player 1 VENCEU!!!({player1} vence de{player2})')

else:
    print(f'Player2 VENCEU!!!({player2} vence de{player1})')