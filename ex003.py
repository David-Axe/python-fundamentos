n1= int(input('Digite algum número: '))
n2= int(input('Agora, outro número: '))
soma = n1 + n2
print('A soma entre {} e {} vale {}{}{}!'.format(n1,n2,'\033[1;31m', soma, '\033[m'))
