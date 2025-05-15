''' PARA SER APROVADO EM UM CURSO, O ALUNO DEVEPOSSUIR
 NOTA MAIOR QUE 6 ENTÃO  SEU STATUS É APROVADO, SE FOR 
 MENOR QUE 4 ENTÃO SEU STATUS É REPROVADO E SE TIVER 
 ENTRE 4 E 6 ELE DE RECUPERAÇÃO.  CRIE UM PROGRMA QUE 
 RECEBA UMA NOTA E DIGA QUAL É O STATUS DO ALUNO.'''

nota: float = float(input("informe a nota do(a) aluno(a)"))

if nota > 6.0:
    print("O aluno está Aprovado!")
elif nota < 4.0:
    print("O aluno está de Reprovado!")
elif nota >= 6.0:
    print("O aluno está aprovado")

else:
    print("O aluno esta de recuperação")



