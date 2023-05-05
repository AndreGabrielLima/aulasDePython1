usuarioD = {}
menu = ['\33[30:47mCoxinha\33[m R$3.5', '\33[30:47mHot-dog\33[m R$6', '\33[30:47mBatata frita\33[m R$7',
        '\33[30:47mMilkshake\33[m R$6', '\33[30:47mHamburguer\33[m R$8', '\33[30:47mRefrigerante\33[m R$4']

while True:

    opçao_list = ['Usuário novo', 'Cardápio/menu']

    for i, card in enumerate(opçao_list):
        print('[{}] -- {}'.format(i, card))

    print('\33[6:30:44m-\33[m'*100)
    decisao = input('Digite o que você quer: ')

    if (decisao == '0'):
        nome = input('Digite seu nome: ')
        senha = int(input('Digite uma senha: '))
        print('Seja bem vindo(a) {}.'.format(nome))
        usuarioD[senha] = nome

    elif (decisao == '1'):
        for i, carda in enumerate(menu):
            print('[{}] -- {}'.format(i, carda))

        pedido = int(input('Qual lanche você vai querer? '))

        if pedido == 0:
            quant = int(input('Quantas coxinhas você vai querer? '))
            valor = quant * 3.5
            print('O total de {} coxinhas fica por {}'.format(quant, valor))
            pg = input('Vai ser dinheiro ou cartão ?')
            if pg == 'dinheiro':
                print('Estamos sem troco no momento.')
            elif pg == 'cartão':
                print('Desculpa, mas estamos sem a maquininha')
            else:
                print('Se não for pagar irei chamar o segurança!!')

        elif pedido == 1:
            quant = int(input('Quantos Hot-dogs você vai querer? '))
            valor = quant * 6
            print('O total de {} Hot-dogs fica por {}'.format(quant, valor))
            pg = input('Vai ser dinheiro ou cartão ?')
            if pg == 'dinheiro':
                print('Estamos sem troco no momento.')
            elif pg == 'cartão':
                print('Desculpa, mas estamos sem a maquininha')
            else:
                print('Se não for pagar irei chamar o segurança!!')

        elif pedido == 2:
            quant = int(input('Quantas Batatas fritas você vai querer? '))
            valor = quant * 7
            print('O total de {} Batatas fritas fica por {}'.format(quant, valor))
            pg = input('Vai ser dinheiro ou cartão ?')
            if pg == 'dinheiro':
                print('Estamos sem troco no momento.')
            elif pg == 'cartão':
                print('Desculpa, mas estamos sem a maquininha')
            else:
                print('Se não for pagar irei chamar o segurança!!')

        elif pedido == 3:
            quant = int(input('Quantos Milkshakes você vai querer? '))
            valor = quant * 6
            print('O total de {} Milkshakes fica por {}'.format(quant, valor))
            pg = input('Vai ser dinheiro ou cartão ?')
            if pg == 'dinheiro':
                print('Estamos sem troco no momento.')
            elif pg == 'cartão':
                print('Desculpa, mas estamos sem a maquininha')
            else:
                print('Se não for pagar irei chamar o segurança!!')

        elif pedido == 4:
            quant = int(input('Quantos Hamburgueres você vai querer? '))
            valor = quant * 8
            print('O total de {} Hamburgueres fica por {}'.format(quant, valor))
            pg = input('Vai ser dinheiro ou cartão ?')
            if pg == 'dinheiro':
                print('Estamos sem troco no momento.')
            elif pg == 'cartão':
                print('Desculpa, mas estamos sem a maquininha')
            else:
                print('Se não for pagar irei chamar o segurança!!')

        elif pedido == 5:
            quant = int(input('Quantos Refrigerantes você vai querer? '))
            valor = quant * 4
            print('O total de {} Refrigerantes fica por {}'.format(quant, valor))
            pg = input('Vai ser dinheiro ou cartão ?')
            if pg == 'dinheiro':
                print('Estamos sem troco no momento.')
            elif pg == 'cartão':
                print('Desculpa, mas estamos sem a maquininha')
            else:
                print('Se não for pagar irei chamar o segurança!!')

    print('\33[1:33:40m-\33[m'*100)
    print('Deseja mais alguma coisa? ')
    print('Digite 1 para continuar | Digite 0 para encerrar')

    if int(input()) == 0:
        print('Obrigado pela preferência!!!')
        break
