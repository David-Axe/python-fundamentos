#Programa que faz o computador 'pensar' em um numero inteiro entre 0 e 5 e pede para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
#O programa escreve na tela se o usuario venceu ou perdeu.

from random import randint

computador = randint(0, 5)
print('-=-' * 20)
print('Pensei em um número entre 0 e 5. Tente adivinhar!')
print('-=-' * 20)

usuario = int(input('Em que número pensei? '))

if usuario == computador:
    print('PARABÉNS! Você acertou!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {usuario}.')
