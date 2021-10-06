'''
Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escreva:
F-Feminino, M- Masculino, Sexo Inválido.
'''

S = str(input("Digite f para Feminino ou m para Masculino: "))
f = "Sexo feminino"
m = "Sexo masculino"

if S == 'f':
    print(f'\n{f}')
elif S == 'm':
    print(f'\n{m}')
else:
    print('\nSexo inválido')
