print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

#Construa um programa/pagina onde o usuario digitará dois numeros,utilizando passagens de parâmetros,
#dentro da função, irá calcular a soma desses dois numeros:

def soma(a,b):
    return a + b 

#entrada do usuario:
n1=float(input('Digite o primeiro número:'))
n2=float(input('Digite o segundo número:'))

resultado = soma(n1 , n2)
print('A soma dos números é:',{resultado})