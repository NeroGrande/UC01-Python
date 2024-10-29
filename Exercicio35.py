print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

#construa uma pagina/programa onde o usúario digitará o nome e a media de
#dez alunos e o programa escreverá,na tela o nome de todos com a média acima ou igual a seis

def Media (n1,n2,n3,n4):
    media=(n1+n2+n3+n4)/4
    if(media>=7):
        return "APROVADO"
    elif(media<7 and media>4):
        return "RECUPERAÇÃO"
    else:
            return "REPROVADO"

notas=[]

#for i in range(4):
#     notas.append(float(input(f"Digite a {i+1} nota: ")))
#print(f'O aluno está: {Media (notas[0],notas[1],notas[2],notas[3] )}]')
def defineMedia(nome):
    notas=[]
     
    for i in range(4):
          notas.append(float(input(f'Digite a {i+1}nota:')))
    print(f'O aluno {nome} está:{Media(notas[0],notas[1],notas[2],notas[3])}')

for i in range(5):
     nomeAluno=input('Digite o nome do aluno: ')
     defineMedia(nomeAluno)

     