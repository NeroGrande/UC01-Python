print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

peso=float(input('Digite o sue peso: '))
altura=float(input('Digite Sua Altura:'))

imc=(peso/altura)

if (imc>25):
    print('GORDÂO')
else:
    print('Magrinho')