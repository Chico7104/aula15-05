''''
CRIE UM MENU DE OPÇÕES PARA USUÁRIO NAVEGAR NO SISTEMA:
O MENU TEM ÀS SEGUINTES OPÇÕES:
A - VER SALDO; 
B - DEPOSITAR;
C - SACAR;
D - ENCERRAR CONTA;
X - SAIR DO SISTEMA;

CASO O USUÁRIO ESCOLHA UMA OPÇÃO DIFERENTE EXIBA: OPÇÃO INVÁLIDA.
CASO ELE ESCOLHA UMA DAS OPÇÕES CORRETAS, INFORME PARA ELE EM QUAL PARTE DO
SISTEMA ELE ESTÁ:
EXEMPLO: A - SEU SALDO É R$1.000,00
'''
# Menu de opções para o usuário navegar no sistema
print("MENU DE OPÇÕES:")
print("A - VER SALDO")
print("B - DEPOSITAR")
print("C - SACAR")
print("D - ENCERRAR CONTA")
print("X - SAIR DO SISTEMA")

# Solicita a opção do usuário
opcao = input("Informe a opção desejada: ").upper()

# Verifica a opção escolhida
match opcao:
    case "A":
        print("A - SEU SALDO É R$1.000,00")
    case "B":
        print("B - VOCÊ ESTÁ NA OPÇÃO DE DEPÓSITO")
    case "C":
        print("C - VOCÊ ESTÁ NA OPÇÃO DE SAQUE")
    case "D":
        print("D - VOCÊ ESTÁ ENCERRANDO SUA CONTA")
    case "X":
        print("X - VOCÊ SAIU DO SISTEMA")
    case _:
        print("Opção Inválida")   