#Programa que lê um número real qualquer e mostre a sua porção inteira
import math
num = float(input('Digite um número real qualquer: '))
parte = math.trunc(num)
print(f'A porção inteira de {num} é {parte}')
