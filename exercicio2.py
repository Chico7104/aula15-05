'''2 - Crie um programa que leia o conceito de um aluno na disciplina BCC201 (INTRODUÇÃO A PROGRAMAÇÃO) 
 e imprima seu significado, de acordo com a tabela abaixo. Caso seja informado um conceito 
 inexistente, deve ser exibida a mensagem de erro.
 Conceito Significado
 A = Excelente
 B = Ótimo
 C = Bom
 D = Regular
 E = Ruim
 F = nos vemos de novo no ano que vem...'''
# Programa para verificar o conceito de um aluno na disciplina BCC201

# Solicita o conceito do aluno
conceito = input("Digite o conceito do aluno: ").upper()

# Verifica o conceito e imprime o significado correspondente
if conceito == "A":
    print("Excelente")
elif conceito == "B":
    print("Ótimo")
elif conceito == "C":
    print("Bom")
elif conceito == "D":
    print("Regular")
elif conceito == "E":
    print("Ruim")
elif conceito == "F":
    print("Nos vemos no próximo ano!")
else:
    print("Erro: Conceito inexistente!")