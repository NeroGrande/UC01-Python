#                     inicializa a soma
lista=[]
soma=0
#                    loop para pedir 10 numeros 
for i in range(10):
    lista.append(int(input("Digite um Número: ")))

#                   Soma os números digitados 
    soma+=lista[i] 
#                     exibe a soma e calcula a média 
print(f'Soma:{soma}, Média:{soma/len(lista)}')
