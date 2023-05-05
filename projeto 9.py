while True:

# Laço de repetição enquanto for verdade o código

    menu_list = ['Alugar um carro', 'Devolver o carro']

    # Variável do tipo lista armazenando opções de alugar e devolver

    for i, menu in enumerate(menu_list):

    # Um laço de repetição do tipo for já que tem um limite

        print('[{}] -- {}'.format(i, menu))

        # Interação para apresentar as opções

    conf = input('Digite sua opção: ')

    # Variável para o usuário digitar a opção que ele quer

    if (conf == '0'):

    # Condição para caso a opção seja 0

        print('Você quer alugar qual carro? ')

        # Interação para saber qual carro o usuário quer

    elif (conf == '1'):

    # Condição para caso a escolha seja 1

        print('Qual carro da lista você quer devolver?')

        # Interação para saber qual carro o usuário quer devolver

    print('='*8)

    # Apenas para organizar o terminal

    print('Digite 0 - para continuar | 1 - para sair')

    # Interação para saber qual a decisão do usuário

    if int(input()) == 1:

    # Condição para caso a escolha seja 1

        break

        # Forma para quebrar o laço de repetição