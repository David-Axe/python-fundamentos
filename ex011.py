#Programa que lê a largura e a altura de uma parede em metros, calcule a sua área e quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de de 2 metros quadrados.

altura = float(input('Qual é a altura da parede? (metros)'))
largura = float(input('Qual é a largura da parede? (metros)'))
print(f'A parede tem {altura*largura:.2f} metros quadrados e são necessários {(altura*largura)/2:.2f} litros de tinta para pintá-la.')
