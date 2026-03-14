#Programa que lê o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
#ex: ana maria de souza
#primeiro: ana
#ultimo: souza
nome = input('Digite o nome completo de alguém: ')
nome = nome.title()
palavras = nome.split()
print(f'Primeiro: {'\033[1;7;37m'}{palavras[0]}{'\033[m'}')
print(f'Último: {'\033[1;31;47m'}{palavras[-1]}{'\033[m'}')

