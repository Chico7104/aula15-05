'''ATIVIDADE: CRIE UMA CALCULADORA DE ÁREAS
        CASO O USUÁRIO DIGITE C: O PROGRAMA DEVE CALCULAR A ÁREA DE UM CÍRCULO: A = PI * R²
        CASO O USUÁRIO DIGITE Q: O PROGRAMA DEVE CALCULAR A ÁREA DE UM QUADRADO: A = L²
        CASO O USUÁRIO DIGITE R: O PROGRAMA DEVE CALCULAR A ÁREA DE UM RETÂNGULO: A = BASE * ALTURA.
'''
# ATIVIDADE: CRIE UMA CALCULADORA DE ÁREAS
def calcular_area():
    opcao = input("Digite 'C' para círculo, 'Q' para quadrado ou 'R' para retângulo: ").upper()

    if opcao == 'C':
        raio = float(input("Digite o raio do círculo: "))
        area = 3.14159 * (raio ** 2)
        print(f"A área do círculo é: {area:.2f}")
    elif opcao == 'Q':
        lado = float(input("Digite o lado do quadrado: "))
        area = lado ** 2
        print(f"A área do quadrado é: {area:.2f}")
    elif opcao == 'R':
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area = base * altura
        print(f"A área do retângulo é: {area:.2f}")
    else:
        print("Opção inválida. Tente novamente.")

# Chamada da função
calcular_area()
