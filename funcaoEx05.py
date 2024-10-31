print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

#Construa uma pagina onde o usuário digitará o nome e a média de dez alunos e o programa escrevá,
#na tela, o nome de todos alunos com a media acima ou igual a seis.

alunos=[]
medias=[]
for i in range(10):
    alunos.append(input(f'Digite o nome do {i+1} aluno:'))
    medias.append(input(f'Digite a média do {i+1} aluno:'))
def retornamaiores():
    for i in range(10):
        if(medias[i]>=6):
            print(f'aluno {alunos[i]} com média {medias[i]} ')
