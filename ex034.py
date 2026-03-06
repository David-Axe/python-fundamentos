#ENUNCIADO
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

#ALGORITMO
#1. ler o salario do funcionario
#2. verificar se é superior ou inferior a R$1250,00
#3. mostrar o aumento, o salario e o futuro salario (salario + aumento)

#CODIGO

salario = float(input('Digite o salário do funcionário: '))
if salario > 1250:
    aumento = salario / 100 * 10
    salariofinal = salario + aumento
    print(f'O salário de R${salario:.2f}, obteve um aumento de {aumento:.2f} e o salário final será de {salariofinal:.2f}')
else:
    aumento = salario / 100 * 15
    salariofinal = salario + aumento
    print(f'O salário de R${salario:.2f}, obteve um aumento de {aumento:.2f} e o salário final será de {salariofinal:.2f}')