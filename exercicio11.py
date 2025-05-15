'''Faça um programa que leia a idade de um nadador e classifique-o numa das
seguintes categorias abaixo:
• Adulto (idade >= 18);
• Juvenil (idade >= 14);
• Infantil (idade >=9);
• Mirim (Idade < 9).'''

# Programa para classificar nadadores por idade

# Lê a idade do nadador
idade = int(input("Digite a idade do nadador: "))

# Classifica o nadador com base na idade
if idade >= 18:
    categoria = "Adulto"
elif idade >= 14:
    categoria = "Juvenil"
elif idade >= 9:
    categoria = "Infantil"
else:
    categoria = "Mirim"

# Exibe a categoria
print(f"A categoria do nadador é: {categoria}")