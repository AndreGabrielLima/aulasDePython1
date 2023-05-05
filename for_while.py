for i in range(10):
    print('Está na posição: {}'.format(i))

for i in 'STRING':
    print('Está na letra: {}'.format(i))

for i in range(len('STRING')):
    print('Está na posição: {}'.format(i))

m =  [1, 2, 3]
l = [m, 1, 2, 3]

for i in l:
    print('Você está na posição: {}'.format(i))

for i in range(1, 9):
    v = int(input('Digite um número:'))
    if v % 2 == 0:
        print('{} é par!'.format(v))
    else:
        print('{} é ímpar'.format(v))

