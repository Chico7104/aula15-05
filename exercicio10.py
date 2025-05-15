'''
Faça um programa que leia um número, verifique se este número é positivo, negativo
ou Zero. Se for negativo mostre a mensagem "Você digitou um numero negativo", Se for
positivo mostre:" Você digitou um número positivo e se for zero mostre: “Você digitou
zero”.
'''

# Programa para verificar se um número é positivo, negativo ou zero

# Lê um número do usuário
numero = float(input("Digite um número: "))

# Verifica se o número é positivo, negativo ou zero
if numero > 0:
    print("Você digitou um número positivo.")
elif numero < 0:
    print("Você digitou um número negativo.")
else:
    print("Você digitou zero.")