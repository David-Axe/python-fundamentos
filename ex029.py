#ENUNCIADO
#Programa que lê a velocidade de um carro.
# Se ele ultrapassar 80km/h o programa mostra uma mensagem dizendo que ele foi multado.
# A multa custa R$7,00 por cada km acima do limite.


#ALGORITMO
#1. Receber a velocidade do carro (float).
#2. Condicional if para caso o carro tenha passado os 80km/h
    #3. valor da multa = (velocidade do carro - 80km/h) * 7
    #4. print: você foi multado! Sua multa é de R$X
#5. print: você não foi multado, parabéns!


#README
#===============================
#PROGRAMA DE MULTA DE VELOCIDADE
#===============================
#Objetivo: receber a velocidade do carro, verificar se ele ultrapassou o limite permitido e, em caso, afirmativo multar o motorista numa proporção de R$7,00 por km/h excedente ao limite.

#Como usar:
#-Digite a velocidade do carro
#-O programa irá:
#   *verificar se passou do limite de velocidade;
#       *caso passou, irá calcular o valor da multa
#       *mostrar na tela o valor da multa.
#   *caso não tenha passado irá apenas informar
# 
#Resultado: 'Multado' ou 'Não multado'
# ==========================================
#    

vel = float(input('Quantos km/h estava o seu carro? '))
if vel > 80:
    multa = (vel - 80) * 7
    print(f'Você foi multado! Sua multa é de R${'\033[1;31m'}{multa:.2f}{'\033[m'}')
else:
    print(f'{'\033[1;32m'}Parabéns! Você não foi multado!{'\033[m'}')