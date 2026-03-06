#ENUNCIADO
#Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem formar um triângulo.

#ALGORITMO
#1. ler as 3 retas
#2. verificar se nenhuma das retas sozinhas é maior do que as outras duas juntas (condição para formar um triângulo)
#3. mostrar o resultado

#CODIGO

r1 = float(input('Digite um valor para a primeira reta: '))
r2 = float(input('Digite um valor para a segunda reta: '))
r3 = float(input('Digite um valor para a terceira reta: '))

if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print('Não é possível formar um triângulo com estas medidas!')
else:
    print('Sim, é possível formar um triângulo com estas medidas!')