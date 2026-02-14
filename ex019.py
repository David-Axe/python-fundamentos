#Programa que ajuda um professor a sortear um de seus alunos para apagar o quadro. Sendo que o total de alunos é quatro. O programa deve ler os nomes e sortear um deles.
import random
n1 = input('Qual é o nome do aluno? ')
n2 = input('Do outro? ')
n3 = input('E do outro? ')
n4 = input('E do último? ')
sorteado = [n1, n2, n3, n4]
print(f'O aluno sorteado foi {random.choice(sorteado)}')
