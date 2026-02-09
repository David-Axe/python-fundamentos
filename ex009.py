#titulo do programa.
print('***** Bem vindo ao Tabulator! *****')
# aqui o usuario poem o seu nome.
nome = input('Qual é o seu nome? ')
# o usuario deve escolher algum numero para ser gerada a tabuada (de 1 a 10) do mesmo.
while True:
    try:
        n1 = int(input(f'{nome}, a tabuada de qual número você deseja conhecer? '))
        break
    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros.")

tabuada = '\n'.join([f'{i:2d} x {n1:2d} = {i * n1:2d}' for i in range(1, 11)])
print(f'Tabuada do {n1}!\n{tabuada}')