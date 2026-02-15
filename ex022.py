#Programa que lê o nome de uma pessoa e mostre: o nome com todas as letras maiúsculas, minúsculas, quantas letras tem ao todo (sem considerar espaços), quantas letras tem o primeiro nome.
nome = str(input('Digite o seu nome: '))
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ','')))
dividido = nome.split()
print(len(dividido[0]))