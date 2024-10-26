Num=[]
cont=0
for i in range(10):
    
    Num.append(int(input("Digite um número ")))
    if (Num[i]>10):
        cont+=1
        print(Num[i])
print(cont)