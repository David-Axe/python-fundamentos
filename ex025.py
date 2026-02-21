#Programa que lê o nome completo de uma pessoa e diz se la tem Silva no nome.
name = input('Qual é o seu nome completo? ')
if 'silva' in name.lower():
    print('Você tem Silva no nome!')
else:
    print('Você NÃO tem Silva no nome!')
