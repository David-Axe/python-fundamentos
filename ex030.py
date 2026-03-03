#ENUNCIADO
#Programa que lê um número inteiro e mostra na tela se ele é par ou ímpar.


#ALGORITMO
#1. recebe número inteiro do usuário
#2. calcula o resto da divisão por 2 do número recebido
    #3. se o resto da divisão for 0, o número é par
    #4. senão o número será ímpar
#5. Mostrar na tela a classificação do número (par ou ímpar)


#README
#Objetivo: receber um número inteiro qualquer e mostrar se ele é par ou ímpar
#Como usar:
# - o programa irá pedir um número inteiro ao usuário.
# - Após o usuario digitar o numero:
#       *o programa irá calcular o resto da divisão por 2 do numero digitado
#       *caso o resto seja 0, o pragama irá avisar o usuario de que o numero digitado é par
#       *em caso contrário o programa dirá que impar
#Resultado: 'par' ou 'impar'.


#CODIGO
n = int(input('Digite um número inteiro: '))
if n % 2 == 0:
    print(f'O número {n} é par!')
else:
    print(f'O número {n} é ímpar!')