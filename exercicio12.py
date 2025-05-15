'''Faça um programa que leia dois números e efetua a adição. Se o valor somado for
maior que 20, este deverá ser apresentado somando-se a ele 8; se o valor somado for
menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.
'''

# Leia dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Efetua a adição
soma = num1 + num2

# Verifica a condição e ajusta o valor
if soma > 20:
    resultado = soma + 8
else:
    resultado = soma - 5

# Apresenta o resultado
print(f"O resultado é: {resultado}")