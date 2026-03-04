#ENUNCIADO:
#Faça um programa que leia um ano qualquer e mostre se ele é bissexto ou não:


#ALGORITMO:
#1. programa pede ao usuario um ano qualquer
#2. usuario digita um ano qualquer
#3. programa calcula se o ano é múltiplo de 4 E não múltiplo de 100, OU se é múltiplo de 400
#4. caso o ano se encaixe nestas condições o programa informa o usuario de que o ano digitado é bissexto.
#5. caso contrario, o ano não é bissexto.



#CODIGO:
ano = int(input('Digite algum ano para saber se é bissexto: '))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto!')
else:
    print(f'O ano de {ano} NÃO é bissexto!')