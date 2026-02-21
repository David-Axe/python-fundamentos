#Programa que lê uma frase e mostre quantas vezes aparece a letra a; em que posição ela aparece a primeira vez; e em que posição ela aparece a última vez.
frase = input('Digite alguma frase: ')
frase = frase.lower()
quantidade = frase.count('a')
primeira = frase.find('a')+1
ultima = frase.rfind('a')+1
if quantidade > 0:
    print(f'A frase digitada tem {quantidade} letras A; A primeira aparece na posição {primeira} e a última aparece na posição {ultima}.')
else:
    print("A frase digitada não possui a letra A")
    
