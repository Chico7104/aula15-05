'''Faça um programa que leia três notas, calcule e mostre a média aritmética entre elas.'''


# Programa para calcular a média aritmética de três notas

# Leitura das três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média aritmética
media = (nota1 + nota2 + nota3) / 3

# Exibição do resultado
print(f"A média aritmética das notas é: {media:.2f}")