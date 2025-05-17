'''CONECTORES LÓGICOS

USADOS PARA UNIR DUAS PROPOSIÇÕES E A PARTIR DISSO PRODUZIR UM RESULTADO LÓGICO.
---AND : PRODUZ UM RESULTADO VERDADEIRO.
QUANDO TODAS AS PROPOSIÇÕES (TESTE LÓGICO) FOREM VERDADEIRAS.
---OR : PRODUZ UM RESULTADO  FALSO QUANDO TODOS OS TESTES LÓGICOS FOREM FALSOS.
           ___E___                                   
------------------------------       A REGRA DO >>>AND<<< SEGUE A LÓGICA DE SER              
 A    |      AND     |   B           VERDADEIRO SOMENTE QUANDO TODA A CONDIÇÃO LÓGICA FOREM
------------------------------       VERDADEIRAS
 V          F            F
------------------------------
 F          F            V
------------------------------
 F          F            F
------------------------------        
 V          V            V
------------------------------


         ___OU___
------------------------------        A REGRA DO >>>>OR<<<<< SEGUE A LÓGICA QUE PRA
  A          OR          B            SE TER UMA CONDIÇÃO VERDADEIRA OU FALSA, TODAS ÀS AFIRMAÇÕES 
------------------------------        DEVEM SER VERDADEIRAS OU FALSAS.
  V          V           V
------------------------------
  F          V           V
------------------------------
  V          V           F
------------------------------
  F          F           F
------------------------------     '''
''' Exemplo de 
'''

print("============INSS============")
idade: int = int(input("Informe a idade do contribuinte:"))
tempo_de_contribuicao: int = int(input("Informe o tempo de contribuição:"))
if (idade >= 65) or (tempo_de_contribuicao) >= 30:
    print("aposentadoria concedida")
else:
    print("Aposentadoria Negada!! Continue trabalhando")

    '''
    * CONDICIONAIS
    * REPETIÇÃO

    >> CONDICIONAL EXECUTA UM DETERMINADO TRECHO DE CÓDIGO DE ACORDO COM UMA CONDIÇÃO.
    >> REPETIÇÃO EXECUTA UM TRECHO DE CÓDIGO VÁRIAS VEZES, ATÉ QUE UMA CONDIÇÃO SEJA VERDADEIRA OU FALSA.

    EXEMPLO: ENQUANTO ( HORÁRIO < 23:00 ) ENTÃO O CODIGO RESPONDE QUE TEM AULA.
    * CONDICIONAL SIMPLES: SE A CONDIÇÃO FOR VERDADEIRA ELE EXECUTA O TRECHO DO CÓDIGO ATÉ ACHAR UMA CONDIÇÃO FALSA.
    * CONDICIONAL COMPOSTA: SE A CONDIÇÃO FOR VERDADEIRA ELE EXECUTA O TRECHO DO CÓDIGO, SE NÃO ELE EXECUTA OUTRO
      TRECHO DE CÓDIGO.

    '''