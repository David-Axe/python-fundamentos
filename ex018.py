#Programa que lê um ângulo qualquer e mostra na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo_graus = float(input('Digite o valor de algum ângulo: '))
angulo_radianos = math.radians(angulo_graus)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)
print(f'O seno é {seno:.3f}, o cosseno é {cosseno:.3f} e a tangente é {tangente:.3f}')
