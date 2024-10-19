# value=3
# match value:
# case 1:
# Result = 'one'
# case 2:
# Result = 'two'
# case 3:
# result = 'three'
# case _:
# result= 'Default' 
#print(result)
print      ("BEM VINDO LENDA VIVA")
print ("-------------------------------")

total=0
Escolha=0
while(Escolha!=5):
 print("Cardapio: ")
 print(f'1- Calabresa Com Cebola - $59.90\n'
      f'2- Frango Com Reiqueijão - 87.80\n'
      f'3- Camarão Com Catupiry - $65,50 \n'
      f'4- Banana Com Chocolate - $59.90\n'
      f'5- Finalizar pedido')
 Escolha=int(input('Digite a opção escolhida (apenas números):'))

 match Escolha:
    case 1:
        print("Calabresa Com Cebola - $59.90")
        total+=59.9
    case 2:
        print("Frango Com Reiqueijão - 87.80")
        total+=87.8
    case 3:
        print("Camarão Com Catupiry - $65.50")
        total+=65.5
    case 4:
        print("Banana Com Chocolate - $59.90")
        total+=59.9
    case 5:
       print(f'total do pedido: R${total}')
    case _:
        print("escolha uma opção válida")