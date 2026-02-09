#Programa que lê quantos reais uma pessoa tem no bolso; e passa o quanto ela pode trocar por dólar. Considerando US$ 1,00 e R$3,27
real = float(input('Quantos reais você tem?'))
print(f'Você tem R${real:.2f} e pode trocar por US${real/3.27:.2f}')
