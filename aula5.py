#Crie um programa que receba um nome, uma cidade e uma idade do usuário e exiba os dados em frases no console.

nome: str = input("Digite seu nome: ")
cidade: str = input("Digite sua cidade: ")
idade:  int = (input("Digite sua idade: "))

# Exibindo os dados com as frases
print("Eu sou a", nome)
print("Moro em", cidade)
print("Tenho", idade + "anos")