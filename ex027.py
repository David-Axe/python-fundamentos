#Programa que lê o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
#ex: ana maria de souza
#primeiro: ana
#ultimo: souza
nome = input('Digite o nome completo de alguém: ')
nome = nome.title()
palavras = nome.split()
print(f'Primeiro: {palavras[0]}')
print(f'Último: {palavras[-1]}')

