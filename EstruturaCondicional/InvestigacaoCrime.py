'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a) Telefonou para vitima?
b)Esteve no local do crime?
c)Mora perto da vitima?
d)Devia para vitima?
e)Já trabalhou com a vitima?
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "suspeita", entre 3 e 4
como "cúmplice" e 5 como "assassino". Caso contrário ela será classificada como "inocente".
'''

contS = 0

print('\n- Responda as perguntas a seguir com "s" para sim e "n" para não:')
a = str(input('Telefonou para vítima? '))
if a == 's':
    contS += 1

b = str(input('Esteve no local do crime? '))
if b == 's':
    contS += 1

c = str(input('Mora perto da vitima? '))
if c == 's':
    contS += 1

d = str(input('Devia para vitima? '))
if d == 's':
    contS += 1

e = str(input('Telefonou para vitima? '))
if e == 's':
    contS += 1

if contS >= 2:
    if contS == 2:
        print('\nSuspeita')
    if 3 <= contS <= 4:
        print('\nCúmplice')
    if contS == 5:
        print('\nAssassino')
else:
    print('\nInocente')
