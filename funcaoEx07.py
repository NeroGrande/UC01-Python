print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

#construa uma pagina/programa onde o usuario digitara o nome, o telefone e a cidade de dez pessoas.
#O programa exibira na tela,O nome e o telefone das pessoas que moram em "Campo Grande".

def exbir_telefones_Campogrande(pessoas):
    
    print("telefones das pessoas que moram em campo grande : ")
    for pessoa in pessoas:
        nome, Telefone,cidade = pessoa
        if cidade.lower() == "Campo Grande":
            print(f'Nome: {nome}, Telefone: {Telefone}')
pessoas=[]
for i in range(10):
    print(f'\npessoa {i + 1}')
    nome= input('Digite o Nome: ')
    telfone= input('digite a cidade:')
    pessoas.append((nome,telfone,cidade))
    