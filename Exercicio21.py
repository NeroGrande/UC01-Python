print      ("BEM VINDO LENDA VIVA")
print ("-------------------------------")

# Função para completar a contagem até 100
def completar_ate_100(numero):
    # Verifica se o número é menor que 100
    if numero < 100:
        # Laço for que vai do número digitado até 100 (incluindo 100)
        for i in range(numero, 101):
            print(i)  # Exibe o número atual
    else:
        # Exibe uma mensagem se o número for maior ou igual a 100
        print("Por favor, digite um número menor que 100.")

# Solicita ao usuário para digitar um número
try:
    numero = int(input("Digite um número menor que 100: "))  # Converte o valor de entrada para inteiro
    completar_ate_100(numero)  # Chama a função para completar a contagem até 100
except ValueError:
    # Exibe uma mensagem de erro se o usuário não digitar um número válido
    print("Por favor, digite um número válido.")