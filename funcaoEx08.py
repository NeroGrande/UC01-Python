print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")
#CONSTRUA UMA PAGINA/PROGRAMA ONDE O USUARIO DIGITARA O NOME E O BAIRRO DE DEZ PESSOAS.
#O PROGRAMA EXIBIRA O NOME E BAIRRO DAS PESSOASEM ORDEM ALFABETICA

def exibir_ordem_alfabeica(pessoas):
    pessoas_ordenadas=sorted(pessoas, key=lambda pessoa: pessoa[0])
    print('\n Pessoas em ordem alfabética: ')
    for pessoa in pessoas_ordenadas:
        nome, bairro= pessoa
        print(f'Nome: {nome}, Bairro:{bairro}')
pessoas = []

for i in range(10):
    print(f'\n pessoa {i + 1}')
    nome = input('Digite o Nome:')
    bairro=input('Digite Seu Bairro')
    pessoas.append((nome, bairro))

    exibir_ordem_alfabeica(pessoas)