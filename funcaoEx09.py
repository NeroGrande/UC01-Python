print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

#CONSTRUA UMA PAGINA/PROGRAMA ONDE O USUARIO DIGITARÁ O NOME E O BAIRRO DE DEZ PESSOAS. 
#O PROGRAMA EXIBIRA O NOME E BAIRRO DAS PESSOAS EM ORDEM ALFABETICA.
def coletar_dados_alunos():
    alunos = []
    for i in range(5):
        print(f"\nAluno {i + 1}")
        nome = input("Digite o nome do aluno: ")
        while True:
            try:
                media = float(input("Digite a média do aluno (0 a 10): "))
                if 0 <= media <= 10:
                    alunos.append((nome, media))
                    break
                else:
                    print("Média inválida! Digite um valor entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Digite um número para a média.")
    
    return alunos
def exibir_alunos(alunos):
    print("\nLista de alunos e suas médias:")
    for aluno in alunos:
        nome, media = aluno
        print(f"Nome: {nome}, Média: {media}")
alunos = coletar_dados_alunos()
exibir_alunos(alunos)
