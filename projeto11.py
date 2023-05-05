import os

# Importando uma biblioteca

carros = [('Chevrolet Tracker', 120),
          ('Chevrolet Onix', 90),
          ('Chevrolet Spin', 150),
          ('Hyundai HB20', 85),
          ('Hyundai Tucson', 120),
          ('Fiat Uno', 60),
          ('Fiat Mobi', 70),
          ('Fiat Pulse', 130)
          ]

# Lista de carros

alugados = []

# Lista de carros alugados vazia

def mostrar_lista_de_carros(lista_de_carros):

# Função para mostrar a lista de caerros

    for i, car in enumerate(lista_de_carros):

    # Laço de repetição para mostrar a lista de carros com numeração

        print('[{}] {} - R$ {} / dia.'.format(i, car[0], car[1]))

    # Interação para deixar organizado

while True:

# Laço de repetição até quando o usuário quiser usar o programa

    os.system('cls')

    # Usando a biblioteca para limpar o terminal e ficar mais visível

    print('='*100)

    # Apenas para organizar o terminal

    print('Bem vindo a locadora Fuctura!')

    # Interação com o usuário

    print('='*100)

    # Apenas para organizar o terminal

    print('O que deseja fazer? ')

    # Interação perguntando o que o usuário deseja fazer

    print('0 - Mostrar portfólio | 1 - Alugar um carro | 2 - Devolver um carro')

    # Mostrando as opções de escolha para o usuário

    op = int(input())

    # Variável para receber a opção do usuário

    os.system('cls')

    # Utilizando a biblioteca para limpar novamente o terminal

    if op == 0:

    # Condição para caso a escolha seja 0

        mostrar_lista_de_carros(carros)

        # Chamando a função mostrar lista de carros

    elif op == 1:

    # Condição para caso a escolha seja 1

        mostrar_lista_de_carros(carros)

        # chamando a função lista de carros com um parâmetro

        print('='*100)

        # Apenas para organizar o terminal

        print('Escolha o código do carro: ')

        # Interação para escolher o código do carro

        cod_car = int(input())

        # Variável para receber o código do carro

        print('Por quantos dias você desejar alugar? ')

        # Interação para saber quantos dias o usuário vai alugar o carro

        dias= int(input())

        # Variável para receber a quantidade de dias

        os.system('cls')

        # Usando a biblioteca para limpar o terminal novamente

        print('Você escolher {} por {} dias'.format(carros[cod_car][0], dias))

        # Interação para mostrar o carro e os dias

        print('O aluguel totalizaria R$ {}. Deseja alugar?'.format(dias * carros[cod_car][1]))

        # Interação para mostrar quantos reais ficou o aluguel do carro

        print('0 - SIM | 1 - NÃO ')

        # Interação para confirmar o aluguel

        conf = int(input())

        # Variável para receber a escolha

        if conf == 0:

        # Condição para caso a escolha seja 0

            print('Parabéns você alugou o {} por {} dias.'.format(carros[cod_car][0], dias))

            # Interação para mostrar o carro e os dias que ele foi alugado

            alugados.append(carros.pop(cod_car))

            # Adicionando o carro alugado na lista de carros alugados

    elif op == 2:

    # Condição para caso a escolha seja 2

        if len(alugados) == 0:

        # Condição para caso o tamanho da lista alugados seja igual a 0

            print('Não há carros para devolver!')

            # Interação mostrando que não há carros alugados

        else:

        # Caso tenha carros alugados

            print('Segue lista de carros alugados. Qual você deseja devolver ?')

            # Interação mostrando a lista dos carros alugados

            mostrar_lista_de_carros(alugados)

            # Chamando a função de mostrar lista de carros, mas dessa vez com outro parâmetro

            print('')

            # Apenas para organizar o terminal

            print('Escolha o código do carro que deseja devolver:' )

            # Interação para pedir qual carro o usuário deseja devolver

            cod = int(input())

            # Variável para receber o código do carro

            if cod == 0:

            # Condição para caso a escolha seja 0

                print('Obrigado por devolver o carro {}.'.format(alugados[cod][0]))

                # Interação para mostrar qual carro o usuário devolveu

                carros.append(alugados.pop(cod))

                # Tirando o carro da lista de alugados e colocando na lista de carros disponíveis

    print('')

    # Apenas para organizar o terminal

    print('Digite 0 - CONTINUAR | 1 - SAIR')

    # Interação para mostrar ao usuário se ele quer continuar ou sair

    if int(input()) == 1:

    # Condição caso a escolha seja 1

        break

        # Quebrando o laço de repetição com o break