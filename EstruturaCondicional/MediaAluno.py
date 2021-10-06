'''
Faça um programa para leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por um aluno e apresentar:
A mensagem "aprovado", se a média for maior ou igual a sete;
A mensagem "reprovado", se a média for menor do que sete;
A mensagem "aprovado com distinção", se a média for igual a dez.
'''

n1= int(input('Digite a primeira nota: '))
n2= int(input('Digite a segunda nota: '))
media = (n1+n2)/2

if (media != 10):
   if media>=7:
      print('\nAprovado')
   else:
      print('\nReprovado')
else:
      print('\nAprovado com distinção')