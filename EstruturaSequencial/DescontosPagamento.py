'''
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo- se que são descontados 11% para o
Imposto de Rendam 8% para o INSS e 5% para o Sindicato, faça um programa que nos dê:
a) salário bruto
b)quanto pagou ao INSS
c) quanto pagou ao sindicato.
d) o salário líquido
e) calcule os descontos e o salário líquido.
'''

pag_hora= float(input('Quanto você ganha por hora? '))
hora= int(input('Quantas horas você trabalha no mês? '))

sal_bruto= pag_hora*hora
inss= sal_bruto*0.08
ir= sal_bruto*0.11
sindicato= sal_bruto*0.05
sal_liq= sal_bruto-(inss+ir+sindicato)

print()
print('+ Salário Bruto : R$', sal_bruto)
print('- Imposto de Renda (%11): R$', ir)
print('- INSS (8%): R$',inss)
print('- Sindicato (5%): R$',sindicato)
print('- Descontos totais: R$',inss+ir+sindicato)
print('= Salário Líquido: R$',sal_liq )