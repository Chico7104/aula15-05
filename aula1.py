# Este é o ponto de entrada inicial no estudo do python.py

# This is the main entry point of the Python application.

# Example of variables and data types
nome = str("Alice")  # String
idade: int = int(input("Digite sua idade:")) 
if idade >= 18:
    print("É maior de idade")  
else:
    print("É menor de idade")    
altura = 1.65    # Float
if idade > 18:
    print("Não é estudade")
elif idade == 18:

# print("Nome:", nome)
    print("Idade:", idade)
print("Altura:", altura)

# Exemplo de uma lista
frutas = ["Maçã", "banana", "cereja"]
print("Frutas:", frutas)


dados = {
    "nome": "Alice",
    "Idade": (idade),
    "Altura": "1.65"
}
print("Dados:", dados)

# Control structures: if-else statement
if idade >= 18:
    print(nome, "é um adulto.")
else:
    print(nome, "é menor.")

# Exemplo de  funcão
def greet(nome):
    return f"Olá, {nome}!"

# Call the function
Saudacoes = greet(nome)
print(Saudacoes)

# Example of a loop
print(f"Lista de frutas da:{nome}:")
for frutas in frutas:
    print(frutas)