print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

#construa uma pagina/programa onde o usuário digitará sete números e o
#programa deverá colocar esses números dentro do vetor em ordem crescente.


num=[]

for i in range(7):
    num.append(int(input('Digite um número: ')))    
    num.sort()

print(f'{num} Ordenado.')

num.reverse()
print(f'{num} Desordenado.')