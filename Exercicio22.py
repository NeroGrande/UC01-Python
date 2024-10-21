print      ("BEM VINDO LENDA VIVA")
print ("-------------------------------")

# Função para completar a contagem de números pares até 100
def completar_pares_ate_100(numero):
    if numero < 100:
        # Percorre o intervalo do número digitado até 100
        for i in range(numero, 101):
            # Verifica se o número é par
            if i % 2 == 0:
                print(i)  # Exibe o número se for par
    else:
        # Exibe uma mensagem se o número for maior ou igual a 100
        print("Por favor, digite um número menor que 100.")

# Solicita ao usuário para digitar um número
try:
    numero = int(input("Digite um número menor que 100: "))  # Converte o valor de entrada para inteiro
    completar_pares_ate_100(numero)  # Chama a função para completar a contagem de números pares até 100
except ValueError:
    # Exibe uma mensagem de erro se o usuário não digitar um número válido
    print("Por favor, digite um número válido.")