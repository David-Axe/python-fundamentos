#ENUNCIADO:
#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA DE UMA VIAGEM EM KM. CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA VIAGENS DE ATÉ 200KM E R$0,45 PARA VIAGENS MAIS LONGAS.
# 
# 
# ALGORITMO:
#1. programa pergunta distancia
#2. usuario digita distancia
#3. programa guarda e processa o valor
#   4. se distancia =< 200 km, programa calcula R$0,50 por km
#       5. programa notifica ao usuario o valor total da viagem
#   6. senão, programa calcula R$0,45 por km
#       7. programa notifica ao usuario o valor total da viagem


#README:
# Programa: Cálculo de Passagem de Viagem

# Descrição
#Programa que calcula o valor da passagem com base na distância da viagem.

# Como usar
#1. Execute o programa
#2. Digite a distância da viagem em quilômetros
#3. O programa exibirá o valor total da passagem

# Regras de cálculo
# - Viagens de até 200km: R$0,50 por km
# - Viagens acima de 200km: R$0,45 por km

#Resultado: valor da viagem.

#CODIGO

distancia = float(input('Qual a distância da viagem que você deseja fazer? '))
valor1 = 0.50
valor2 = 0.45

if distancia <= 200:
    total = distancia * valor1
    print(f'A sua viagem de {distancia} km, custará R${total:.2f}')
else:
    total = distancia * valor2
    print(f'A sua viagem de {distancia} km, custará R${total:.2f}')