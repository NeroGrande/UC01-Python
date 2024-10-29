print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

#Construa um programa onde o usúario digitará a sua idade.Se a idade for menor de 18 anos,
#programas infantis. Caso seja maior de idade,entrará em uma outra função com lista de carros e seus respectivos preços.

def ProgramasInfantis():
    print('lista de programas ')
    lista1=('Peppa Pig','Chaves', 'Pantera Cor De Rosa', 'Tom e Jerry')
    print(lista1)
    return
def Carros():
    lista2=['Jeep Regade - 120.000 ', 'Amarok - r$350.000', 'Hb20 - R$100.000', 'Mobi - R$70.000']
    print(lista2)
idade=input('Digite sua idade: ')
if idade>18:
    print(type("Maior de idade."))
else:
    ProgramasInfantis()