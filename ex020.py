#Programa que sortea a ordem de apresentação dos trabalhos de quatro alunos.
import random
n1 = input('Qual o nome do aluno? ')
n2 = input('Do segundo? ')
n3 = input('Do terceiro? ')
n4 = input('E do quarto? ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(lista)
