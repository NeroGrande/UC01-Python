print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")
NOTA1=float(input("DIGITE A PRIMEIRA NOTA: "))
NOTA2=float(input("DIGITE A SEGUNDA NOTA: "))
NOTA3=float(input("DIGITE A TERCEIRA NOTA: "))
NOTA4=float(input("DIGITE A QUARTA NOTA: "))

MEDIA=(NOTA1+NOTA2+NOTA3+NOTA4)/4

print(f'MEDIA:{MEDIA}')

if(MEDIA<6):
    print('Aluno reprovado')
else:
    print('Aluno Aprovado')