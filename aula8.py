numero_1: float = 0
numero_2: float = 0
total: float = 0

numero_1: float = float(input("informe o numero:"))
numero_2: float = float(input("informe o numero:"))
operador_matematico: str = input("informe a operação desejada: +, -, *, /")

if operador_matematico == "+":
    total = numero_1 + numero_2
elif operador_matematico == "-":
    total = numero_1 - numero_2
elif operador_matematico == "*":
    total = numero_1 * numero_2
elif operador_matematico == "/":
    total = numero_1 / numero_2

else:
    print("opção inválida")

print("O resultado do calculo é:", total)          


