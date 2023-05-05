'''produto = 0
while produto < 4:
    p = str(input('Digite o nome do produto: '))
    v = float(input('Digite o valor do produto: '))
    produto += 1'''

x = 0
while x <= 10:
    print('O valor de x é: {}'.format(x))
    x += 1


x = 0
while x < 10:
    print('O valor de x é: {}'.format(x))
    print('{} ainda é menor que 10, incrementando...'.format(x))
    x +=1
else:
    print('Concluido')

x = 0
while x < 10:
    print('O valor de x é: {}'.format(x))
    x += 1
    continue
    print('x ainda é menor que 10, incremento...')
else:
    print('Concluido')

x = 0
while x < 10:
    print('O valor de x é{}'.format(x))
    x += 1
    break
    print('wdljfwn')
print('Acabou')

while True:
    c = input('Digite 1 para parar | Digite 0 para continuar: ')
    if c == '1':
        print('Fechando')
        break
    elif c == '0':
        print('Repetindo')
    else:
        print('Vcoê não digitou um comando correto')
