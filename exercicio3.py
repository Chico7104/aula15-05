'''3 - Crie um programa que descubra se uma figura geométrica é um quadrado ou um retângulo:
 Um quadrado possui a base e a altura iguais enquanto um retângulo tem a base e a altura em valores 
 diferentes.'''
# Programa para verificar se a figura geométrica é um quadrado ou um retângulo

# Solicita os valores da base e da altura
base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

# Verifica se é um quadrado ou um retângulo
if base == altura:
    print("A figura geométrica é um quadrado.")
else:
    print("A figura geométrica é um retângulo.")