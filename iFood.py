comida = ['Coxinha - R$3.5', 'Hot-dog - R$6.0',
          'Batata frita - R$6.0', 'Milkshake - R$7.0',
          'Hamburguer - R$8.0', 'Refrigerante - R$4.0']
usuarioD = {}
opcao_list = ['CADASTRAMENTO', 'PEDIDO']

while True:
    for i, cad in enumerate(opcao_list):
        print('[{}] - {}'.format(i, cad))

    opcao = input('Digite sua opção: ')

    if opcao == 0:
        use = str(input('Digite seu nome para usuário: ')).upper()
        usuarioD[use]
    for i, menu in enumerate(comida):
        print('[{}] -- {}'.format(i, menu))

    opcao = input('Digite a sua opção: ')

    if opcao == '0':
        quant = int(input('Vai querer quantas coxinhas? '))
        soma = quant * 3.5
        print('Deu R${}'.format(soma))

    elif opcao == '1':
       quant = int(input('Vai querer quantos Hot-dog? '))
       soma = quant * 6.0
       print('Deu R${}'.format(soma))
    elif opcao == '2':
        quant = int(input('Vai querer quantas Batatas fritas? '))
        soma = quant * 6.0
        print('Deu R${}'.format(soma))
    elif opcao == '3':
        quant = int(input('Vai querer quantos Milkshakes? '))
        soma = quant * 7.0
        print('Deu R${}'.format(soma))
    elif opcao == '4':
        quant = int(input('Vai querer quantos Hamburgueres? '))
        soma = quant * 8.0
        print('Deu R${}'.format(soma))
    elif opcao == '5':
        quant = int(input('Vai querer quantos Refrigerantes? '))
        soma = quant * 4.0
        print('Deu R${}'.format(soma))