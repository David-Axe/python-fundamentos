#ENUNCIADO:
#Faça um programa que leia três números e mostre qual é o maior e qual é menor.


#ALGORITMO:
#1. ler os 3 numeros (podem ser inteiros ou reais)
#2. comparar os numeros para encontrar o maior
#3. comparar os numeros para encontrar o menor
#4. mostrar o resultado

#CODIGO:

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f'Menor: {menor}')
print(f'Maior: {maior}')