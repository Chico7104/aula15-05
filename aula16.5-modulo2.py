'''
    * CONDICIONAIS
    * REPETIÇÃO

    >> CONDICIONAL EXECUTA UM DETERMINADO TRECHO DE CÓDIGO DE ACORDO COM UMA CONDIÇÃO.
    >> REPETIÇÃO EXECUTA UM TRECHO DE CÓDIGO VÁRIAS VEZES, ENQUANTO ELE FOR VERDADEIRA.

    EXEMPLO: ENQUANTO ( HORÁRIO < 23:00 ) ENTÃO O CODIGO RESPONDE QUE TEM AULA.
    * CONDICIONAL SIMPLES: SE A CONDIÇÃO FOR VERDADEIRA ELE EXECUTA O TRECHO DO CÓDIGO ATÉ ACHAR UMA CONDIÇÃO FALSA.
    * CONDICIONAL COMPOSTA: SE A CONDIÇÃO FOR VERDADEIRA ELE EXECUTA O TRECHO DO CÓDIGO, SE NÃO ELE EXECUTA OUTRO
      TRECHO DE CÓDIGO.

    '''
'''
CONTADOR DE 1 A 100

'''
contador: int = 1
while contador < 101:
    print("estamos em" , contador)
    contador += 1
