#Algoritmo que lê o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Qual é o salário atual do funcionário? R$'))
aumento = (sal/100)*15
salreajustado = sal+aumento
print(f'O aumento será de R${aumento:.2f}. Portanto, o novo salário será de R${salreajustado:.2f}')
