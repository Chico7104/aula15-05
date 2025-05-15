'''4 - Crie um programa que receba dois números e diga qual deles é o maior.'''
# Programa para verificar qual número é o maior

# Solicita dois números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Compara os números e exibe o maior
if numero1 > numero2:
    print(f"O maior número é: {numero1}")
elif numero2 > numero1:
    print(f"O maior número é: {numero2}")
else:
    print("Os dois números são iguais.")