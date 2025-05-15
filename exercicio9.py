'''
Faça um programa que leia um número, verifique se este número é positivo ou
negativo. Se for negativo mostre a mensagem "Você digitou um numero negativo", Senão
mostre:" Voce digitou um número positivo.'''


# Programa para verificar se um número é positivo ou negativo

# Lê um número do usuário
numero = float(input("Digite um número: "))

# Verifica se o número é positivo ou negativo
if numero < 0:
    print("Você digitou um número negativo")
else:
    print("Você digitou um número positivo")


