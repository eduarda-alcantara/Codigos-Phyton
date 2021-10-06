'''
Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) O produto  do dobro do primeiro com metade do segundo
b) A soma do triplo do primeiro com o terceiro
c) O terceiro elevado ao cubo
'''

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro:'))
n3 = int(input('Digite um número real: '))

a = ((n1*2)*(n2/2))
b = (n1*3)+3
c = n3**3

print(f'\nA= {a}\nB= {b}\nC= {c}')