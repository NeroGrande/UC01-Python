print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")
#Construa um programa/pagina onde o usuário ira digitar seu nome e cidade de onde esta digitando essas informações passarão para uma função,
#e caso a cidade seja 'Rio De Janeiro', a resposta alem do nome da pessoa,escreverá 'Seja bem vindo à Cidade Maravilhosa'. Caso contrário,exibrá 
#apenas o nome e a cidade digitada (utilizar passagem de parametros)

def saudacao(nome, cidade):
    if cidade.lower() == 'rio de janeiro':
        return (f'Óla,{nome}! Seja bem-vindo à cidade maravilhosa.')
    else:
        return (f'Óla,{nome}!Você esta em {cidade}.')

User=input('Digite seu nome: ')
City_User=input('Digite sua cidade: ')

mensagem=saudacao(User,City_User)
print(mensagem)