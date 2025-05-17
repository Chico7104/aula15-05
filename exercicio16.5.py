''' 
Para entrar em uma rede social é necessário infomrar um login e uma senha:
Para testes foi criado um usuário padrão proz@25 e a senha é admin123.
Crie um sistema de login que peça ao usuário um login e uma senha e exiba a mensagem: Logado com sucesso.
se não escreva: Login ou senha Inválidas.

'''

login  = str = input("informe o login:")
senha = str = input("infome a senha:")

if login == "proz@25" and senha == "admin123":

    print("Logado com sucesso!!")

else:

    print("Login ou senha falsa!!")