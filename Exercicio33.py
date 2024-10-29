print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

# constua uma página/programa onde o usuario digitara sete números e o
# programa escreverá, na tela,quantos deles são pares e quantos são impares.

impar=0
par=0
num=[]

for i in range(7):
    num.append(int(input('Digite um número: ')))
    if (num[i]%2==0):
        par +=1
    else:
        impar +=1

print(f'Número Par: {par}')
print(f'Número Impar: {impar}')