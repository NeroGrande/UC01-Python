frutas=["Maçã,Banana,Morango"]
frutas.append("Melão",)
frutas.append("Antero")
#Frutas.sort()
#frutas.reverse()

print(frutas)
for i in range(len(frutas)):
    if frutas [i] == "maçã":
        frutas.pop()
        print(frutas)
        