'''
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o critério, baseado no salário atual:
- salários até R$280,00 (incluindo): aumento de 20%
- salários entre R$280,00 e R$700,00: aumento de 15%
- salários entre R$700,00 e R$1500,00: aumento de 10%
- salários de R$1500,00 em diante: aumento de 5%
Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste
- o percentual de aumento aplicado
- o valor do aumento
- o novo salário, após o aumento.
'''

sal = float(input('Informe o salário: '))

if sal < 1500:
    if sal <= 280:
        va = (sal * 1.2)-sal
        sal1 = sal+va
        print('\n- Salário atual: R$ ', sal)
        print('- Percentual de aumento: 20%')
        print('- Valor do aumento: R$ ' ,va)
        print('- Novo Salário: R$ ',sal1)

    if 280 < sal <= 700:
        va = (sal * 1.15)-sal
        sal2 = sal + va
        print('\n- Salário atual: R$ ', sal)
        print('- Percentual de aumento: 15%')
        print('- Valor do aumento: R$ ', va)
        print('- Novo Salário: R$ ', sal2)

    if 700 < sal < 1500:
        va = (sal * 1.10)-sal
        sal3 = sal + va
        print('\n- Salário atual: R$ ', sal)
        print('- Percentual de aumento: 10%')
        print('- Valor do aumento: R$ ', va)
        print('- Novo Salário: R$ ', sal3)

else:
    va = (sal * 1.05)-sal
    sal4 = sal + va
    print('\n- Salário atual: R$ ', sal)
    print('- Percentual de aumento: 5%')
    print('- Valor do aumento: R$ ', va)
    print('- Novo Salário: R$ ', sal4)



