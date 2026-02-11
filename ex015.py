# Programa que pergunta a quantidade de km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
dias = float(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro rodou? '))
total = (dias * 60) + (km * 0.15)
print(f'O valor total do aluguel do carro é R${total:.2f}')
