'''1 - Para entrar em um sistema o usuário deve informar a senha padrão: admin@2025.
 Crie um programa que peça ao usuário uma senha que verifique se ela é válida, se for deve ser exibido,
 "Autenticação realizada com sucesso!" se não, deve exibir: "Senha inválida!";'''
 
senha_padrao: str = "admin@2025"

senha_informada: str = input("informe a senha:")

if senha_informada == senha_padrao:
    print("autenticação realizada com sucesso!")
else:
    print("Senha inválida!")

# dontpad.com/prozcontagem

# Estudar os temas 01, 02 no aplicativo === GESTÃO PROZ ===





 

 
 
 