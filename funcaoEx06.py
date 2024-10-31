print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")
#
#
pessoa=[]
for i in range(5):
    nome=input('Digite seu nome: ')
    idade=int(input('Digite sua idade: '))
    pessoa.append({'nome':nome,'idade':idade})
def buscar():
    i=0
    menor=0
    while(i<5):
        if(pessoa[i]['idade']<pessoa[i+1][idade]):
            menor=1
        else:
            menor=1+1    
        i+=1
print(f'{pessoa[buscar()]}')