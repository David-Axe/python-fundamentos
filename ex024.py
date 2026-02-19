#Programa que lê o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
city = input('Digite o nome de alguma cidade: ')
if city.lower().startswith('santo'):
    print('Esta cidade começa com o nome Santo!')
else:
    print('Esta cidade NÃO começa com o nome Santo!')