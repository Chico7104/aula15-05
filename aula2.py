'''
Uma esposa solicitou ao marido que ele fosse buscá-la no trabalho.
Ele disse que não poderia porque estava muito ocupado, mas prometeu que iria buscá-la se ele 
encontra-se um funcionário para substituí-lo. 
Ele tinha que perguntar a 3 colegas de trabalho se eles poderiam substitui-lo.
Se um deles dissesse que sim, ele iria buscá-la.
Se não, ele não iria.
# Definindo a lista de colegas 1 - 2  - 3
e mostrando a resposta para a esposa dele:
se sim, Eu vou buscar você meu amor!
se não, Não posso buscar você meu amor!
 '''
colega1 =  "João"
colega2 =  "Maria"
colega3 =  "Carlos"

mensagem1 = str("Eu vou buscar você meu amor!")
mensagem2 = str("Não posso buscar você meu amor!")

#Esse trecho pergunta ao primeiro colega se ele pode substituir. Se ele disser "sim", imprime a mensagem2 e para. Se disser "não", continua perguntando para os próximos colegas.

##Exibe uma pergunta na tela para o colega1 (por exemplo, "João, você pode me substituir?").      
resposta = input(f"{colega1}, você pode me substituir? ").strip().lower() 
#.strip() remove espaços extras antes/depois da resposta.
#.lower() transforma a resposta em letras minúsculas (assim "Sim", "SIM" ou "sim" são tratados igual).

if resposta == "sim":
 #O usuário digita a resposta.   
    print(mensagem1)
else:
    #Se a resposta for "não", o código continua perguntando para os próximos colegas.
    resposta = input(f"{colega2}, você pode me substituir? ").strip().lower()
    if resposta == "sim":
        print(mensagem1)
    else:
        #Se o segundo colega também disser "não", pergunta para o terceiro colega.
        #Se a resposta for "sim", imprime a mensagem1 e para. Se disser "não", imprime a mensagem2.
         #O usuário digita a resposta.
        resposta = input(f"{colega3}, você pode me substituir? ").strip().lower()
        if resposta == "sim":
            print(mensagem1)
        else:
            print(mensagem2)

            #se todos os colegas respoderem "Não"  o código imprime a mensagem2.