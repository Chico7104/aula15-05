'''Crie uma tabela de uma loja com as seguintes informações:
• Código - Produto - Valor
• 100 - Camisa - R$ 120,00
• 101 - Saia - R$ 220,00
• 102 - Calça - R$ 180,00
• 103 - Vestido - R$ 350,00
• 104 - Meia - R$ 7,50
• 
.Crie um programa que de acordo com o código, exiba o nome do produto e o valor.

* Desafio 1: Crie uma segunda versão em que o usuário além do código, informe também a quantidade e o programa
calcule de acordo com o código informado e exiba a seguinte mensagem por exemplo: A compra de 2 camisas foi de R$240,00
* Desafio 2: Crie uma terceira versão em que o programa aplique um desconto de 10% se o valor total for maior que R$500,00'''

# Tabela de produtos
produtos = {
    100: {"nome": "Camisa", "valor": 120.00},
    101: {"nome": "Saia", "valor": 220.00},
    102: {"nome": "Calça", "valor": 180.00},
    103: {"nome": "Vestido", "valor": 350.00},
    104: {"nome": "Meia", "valor": 7.50},
}

# Solicita o código do produto
codigo = int(input("Informe o código do produto: "))

# Verifica se o código é válido
if codigo in produtos:
    produto = produtos[codigo]
    print(f"O produto é {produto['nome']} e custa R${produto['valor']:.2f}")
    
    # Desafio 1: Solicita a quantidade e calcula o valor total
    quantidade = int(input("Informe a quantidade desejada: "))
    total = produto['valor'] * quantidade
    print(f"A compra de {quantidade} {produto['nome']}(s) foi de R${total:.2f}")
else:
    print("Código inválido!")

    