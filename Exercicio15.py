# print      ("BEM VINDO LENDA VIVA")
# print ("-------------------------------")


# a=int(input('Digite o primeiro número: '))
# b=int(input('Digite o segundo  número: '))
# c=int(input('Digite o terceiro número: '))

# if(a==b==a==c):
#      print ('Os Valores 3 são iguais')
# elif(a>b and a>c):
#     print('O primeiro é o maior! ')
# elif(b>c):
#     print('O segundo é o maior! ')
# else:
#     print('O terceiro é o maior! ')  

a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))
c=int(input('Digite o terceiro número: '))

valores=[a,b,c]
valores.sort()
valores.reverese()
print(valores[0])