#Algoritmo que lê o preço de um produto e mostra seu novo preço, com 5% de desconto.
n1 = float(input('Qual é o valor do produto? '))
desconto = n1*0.05
print(f'O desconto é de R${desconto:.2f}. Portanto, o produto ficará por R${n1-desconto:.2f}')