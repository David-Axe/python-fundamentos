#Programa que faz o computador 'pensar' em um numero inteiro entre 0 e 5 e pede para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
#O programa escreve na tela se o usuario venceu ou perdeu.

from random import randint

computador = randint(0, 5)
print('-=-' * 20)
print('Pensei em um número entre 0 e 5. Tente adivinhar!')
print('-=-' * 20)

usuario = int(input('Em que número pensei? '))

if usuario == computador:
    print(f'{'\033[1;32;47m'}PARABÉNS! Você acertou!{'\033[m'}')
else:
    print(f'{'\033[1;31;47m'}GANHEI! Eu pensei no número {computador} e não no {usuario}.{'\033[m'}')
