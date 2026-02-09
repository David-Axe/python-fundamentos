#Programa que lê quantos reais uma pessoa tem no bolso; e passa o quanto ela pode trocar por dólar. Considerando US$ 1,00 e R$3,27
real= float(input('Quantos reais você tem?'))
print('Você tem R${} e pode trocar por US${} '.format(real, real*0.3))
