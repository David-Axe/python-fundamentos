#Programa que lê o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
c1 = float(input('Qual o comprimento do cateto oposto? '))
c2 = float(input('Qual o comprimento do cateto adjacente? '))
h = math.sqrt(c1**2+c2**2)
print(f'O comprimento da hipotenusa é {h:.3f}')
