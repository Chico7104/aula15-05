'''5 - Um sacolão dá desconto de 5 reais para compras acima de 20 reais em maçãs. CAda maçã custa 1,50.
 Crie um programa que receba um número de maçãs compradas e calcule o valor a pagar.'''


preco_maca : float = 1,50
desconto: float = 5,00
quantidade_macas: float = float(input("Informe a quantidade de maçãs:"))
valor_compra : float = quantidade_macas * preco_maca

if valor_compra >20:
        valor_compra = valor_compra- desconto
print("O valor da compra deu: R$", valor_compra)