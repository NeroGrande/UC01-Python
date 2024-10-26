print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

Nota1=float(input('Digite as notas escolares: '))
Nota2=float(input('Digite a segunda nota escolar: '))

media=(Nota1+Nota2)/2
print(f'A Média do aluno é: {media}')

if (media<4):
    print('Aluno Reprovado')
elif(media>7): 
    print('Aluno Aprovado Direto')
else:
    print ('Aluno em recuperação')
    Rec=float(input('Digite as Nota De Recuperação: '))
    if(Rec<5):
        print ('Reprovado Recuperação')    
    else:
        print('Aprovado Na Recuperação')

# if= Se(algo acontecer) 
#else= qualquer coisa que não tenha sido uma condição
#elif= condição do if nao foi verdadeira,mas se foi outra coisa
        