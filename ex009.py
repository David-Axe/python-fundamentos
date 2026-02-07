#titulo do programa.
print('***** Bem vindo ao Tabulator! *****')
# aqui o usuario poem o seu nome.
nome= input('Qual é o seu nome? ')
# o usuario deve escolher algum numero para ser gerada a tabuada (de 1 a 10) do mesmo.
n1= int(input('{}, a tabuada de qual número você deseja conhecer? '.format(nome)))
print(
    'Tabuada do {}!'.format(n1),
    '\n1    X     {}  =  {}'.format(n1,1*n1),
    '\n2    x     {}  =  {}'.format(n1,2*n1),
    '\n3    x     {}  =  {}'.format(n1,3*n1),
    '\n4    x     {}  =  {}'.format(n1,4*n1),
    '\n5    x     {}  =  {}'.format(n1,5*n1),
    '\n6    x     {}  =  {}'.format(n1,6*n1),
    '\n7    x     {}  =  {}'.format(n1,7*n1),
    '\n8    x     {}  =  {}'.format(n1,8*n1),
    '\n9    x     {}  =  {}'.format(n1,9*n1),
    '\n10   x     {}  =  {}'.format(n1,10*n1),
)