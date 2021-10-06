'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

tamanho = int(input('Digite o tamanho do arquivo (MB): '))
veloc = int(input('Digite a velocidade do link (Mbps): '))

tempo = tamanho/ (veloc/8)

print(f'\nO tempo de download será: {(tempo/60): .2f} minutos.')