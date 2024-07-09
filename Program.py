# Autor: Evilyn Feitosa 
# Date: 09/07/24

soma = 0
contador = 0

while True:
    
    numero = int(input("Digite um número (ou digite 0 para parar): "))

    # Verifica se o usuário quer parar
    if numero == 0:
        break

    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

    
    soma += numero
    contador += 1


if contador > 0:
    # Calcula a média dos números
    media = soma / contador
    print(f"A soma dos números inseridos é: {soma}")
    print(f"A média dos números inseridos é: {media:.2f}")
else:
    print("Nenhum número foi inserido.")

print("Programa encerrado.")
