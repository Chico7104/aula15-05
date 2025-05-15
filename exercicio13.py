lucro_a: float = 0,45
lucro_b: float = 0,30

valor_produto: float = float(input("Informe o valor do produto:"))
valor_final_com_lucro: float = 0.0

if valor_produto < 20:
        percentual_real: float = (valor_produto * lucro_a)
        valor_final_com_lucro = valor_produto + percentual_real

print("O valor final do produto ficou em R$", valor_final_com_lucro)


