'''
Exercício em sala de aula'''


codigo_digitado: int = int(input('''Informe o código do produto: 100 101 102 103 104:'''))
quantidade: int = int(input('''Informe a quantidade desejada: '''))
produto: str = ""
preco_final: float = 0.0


match codigo_digitado:
    case 100:
        preco_final = 50 * quantidade
        print(f"O produto é camisa e custa R${50:.2f}")
        produto = "camisa"
        
    case 101:
        preco_final = 70 * quantidade
        print(f"O produto é saia e custa R${70:.2f}")
        prodduto = "saia"

    case 102:
        preco_final = 180 * quantidade
        produto = "calça"
        
        
    case 103:
        preco_final = 170 * quantidade
        produto = "vestido"

    case 104:
        preco_final =  7.50 * quantidade
        produto = "meia"
    
    case _:
        print("Código inválido!")
    
if preco_final >= 500:
    desconto: float = preco_final * 0.10
    preco_final = preco_final - desconto
    print(f"Você recebeu um desconto de 10%! O valor com desconto é R${preco_final:.2f}")
                  
        
        