'''
João, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele
traz um peso de peixes maior que o estabelecido (50kg) deve pagar uma  multa de R$ 4,00 por Kg excedente.
Faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Grave na variável
excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados com as mensagens adequadas.
'''

peso = int(input('Digite o peso dos peixes (kg): '))
excesso = peso-50
multa = 4*excesso

print(f'\nPeso dos peixes: {peso}kg\nExcesso: {excesso}kg\nValor da multa: R$ {multa}')