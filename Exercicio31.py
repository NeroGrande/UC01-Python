Num=[]
for i in range(8):
    
    Num.append(int(input("Digite um número ")))
    Num.sort()

print(f"O maior é: {Num[len(Num)-1]} e o menor é: {Num[0]}")