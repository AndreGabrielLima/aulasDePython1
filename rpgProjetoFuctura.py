nome = str(input('Digite seu nome ou nickname: ')).strip()

# Aqui nós temos uma variável do tipo string com um input para informar o nome do jogador, além do .strip para não ter espaços desnecessários

print('Seja bem vindo {}, hoje você está iniciando sua jornada nesto mundo!!'.format(nome))

# Aqui temos uma frase de boas vindas com o nome do jogador


print('Agora vamos iniciar. Você se encontra no santuário antigo construído pelos deuses primordiais!!')

# Aqui temos um print para interagir mais com o jogador

print('E eles deixaram aqui materiais que podem lhe ajudar em sua jornada. Então, qual você vai escolher? ')

# Aqui temos mais outra interação com o jogador

import random

# Importei a biblioteca random para ter uma escolha aleatória dos números de 1 a 4, para mais tarde printar uma interação

num = random.randint(1, 4)

# Variável com uma tarefa da biblioteca random e os números 1 e 4, informando que tem que ser de 1 a 4

print('Eu escolheria a opção {}, pois ela combina bastante com seu estilo, mas não ligue para o que estou falando, e faça o que seu coração mandar!<3'.format(num))

# Interação com o jogador para dizer qual item combina mais com o jogador. Isso usando a forma aleatória da biblioteca

arma = str(input('Digite 1 para espada longa, 2 para um arco encantado, 3 para um livro antigo e 4 para uma armadura: '))

# Variável do tipo string para o jogador informar qual item ele quer

# Criei uma estrutura de decisão para ser tomada pelo jogador, e fui adicionando mais outras estruturas para mais tomadas de decisão

if (arma == '1'):

    # Condição para um dos tipos de arma

    print('Parabéns, você se tornou um bravo guerreiro!! Mas veja só!! Há um goblin verde logo na sua frente')

    # Interação para informar que há perigo na frente

    print('O que deseja fazer?? Digite 1 para atacar ou 2 para fugir')

    # Interação com o jogador para escolher o que ele quer fazer

    acao = str(input('Digite aqui sua ação: '))

    # Variável para saber a decisão do jogador

    if (acao == '1'):

        # Condição para caso o jogador faça a escolha de número 1

        print('Você atacou o goblin, porém ele não estava sozinho, e lhe feriu gravemente. Tente voltar mais tarde com reforços')

        # Interação com o jogador para mostrar o que houve quando ele tomou a decisão de número 1

    elif (acao == '2'):

        # Condição caso o jogador escolha a opção 2

        print('Correr é algo que não é bom para imagem de um guerreiro, ainda mais quando o goblin o acerta com uma pedra e fica caido no chão')

        # Interação com o jogador para mostrar o que houve quando ele tomou a decisão de número 2

    else:

        # Condição caso o jogador não escolha nenhuma das opções

        print('É melhor escolher um ou outro. Ficar parado é pior')

        # Interação para mostrar que precisa escolher entre um ou outro

elif (arma == '2'):

    # Outra condição caso a escolha do jogador seja a opção 2

    print('Parabéns, você se tornou um arqueiro!! Porém veja, arqueiros ancestrais mortos aparecem e começam a atirar em você')

    # Interação para mostrar ao jogador que há perigo na frente

    print('O que deseja fazer?? Digite 1 para contra atacar ou 2 para fugir')

    # Interação com o jogador para escolher o que ele quer fazer

    acao = str(input('Digite aqui sua ação: '))

    # Variável para saber a decisão do jogador

    if (acao == '1'):

        # Condição para caso o jogador faça a escolha de número 1

        print('Você atacou os arqueiros inimigos, porém eles eram muitos, e você'
              ' estava sem flechas o suficiente, e acabou sendo preso e levado para onde não sabemos')

        # Interação com o jogador para mostrar o que houve quando ele tomou a decisão de número 1

    elif (acao == '2'):

        # Condição para caso o jogador escolha a opção 2

        print('Você correu, querendo fugir para o mais longe. Porém caiu em uma armadilha feita por goblins. Agora não há fuga, somente milagres')

        # Interação com o jogador para mostrar o que houve quando ele tomou a decisão de número 2

    else:

        # Condição caso o jogador não escolha nenhuma das opções

        print('É melhor escolher um ou outro. Ficar parado é pior')

        # Interação para mostrar que precisa escolher entre um ou outro

elif (arma == '3'):

    # Outra condição caso a escolha do jogador seja a opção 3

    import random

    # Biblioteca para fazer uma escolha aleatória de palavras na lista

    element = ['água', 'fogo', 'ar', 'terra']

    # Variável com uma lista tendo palavras de elementos naturais

    print('Parabéns, você se tornou um mago elemental do tipo {}, e um monstro do tipo {} apareceu para testar seu poder'.format(random.choice(element), random.choice(element)))

    # Interação para mostrar qual o elemento do jogador e qual tipo de monstro apareceu também

    print('O que você deseja fazer?? Digite 1 para atacar e 2 para fugir')

    # Interação com o jogador para escolher o que ele quer fazer

    acao = str(input('Digite aqui sua ação: '))

    # Variável para saber a decisão do jogador

    if (acao == '1'):

        # Condição para caso o jogador faça a escolha de número 1

        print('Parabéns pela coragem, porém você é um mago recente, e não teve poder suficiente para lutar contra o monstro. Tente ficar mais forte')

        # Interação com o jogador para mostrar o que houve quando ele tomou a decisão de número 1

    elif (acao == '2'):

        # Condição para caso o jogador escolha a opção 2

        print('O monstro não deixou você fugir, e lhe deu apenas um ataque, que foi o suficiente para lhe abater')

        # Interação com o jogador para mostrar o que houve quando ele tomou a decisão de número 2

    else:

        # Condição caso o jogador não escolha nenhuma das opções

        print('É melhor escolher um ou outro. Ficar parado é pior')

        # Interação para mostrar que precisa escolher entre um ou outro

elif (arma == '4'):

# Outra condição caso a escolha do jogador seja a opção 4

    print('Você se tornou um enorme tank, e ficou gigante. No entanto, um gigante da terra de elbaf apareceu, e lhe desafiou para testar suas habilidades')

    # Interação para mostrar o que acontece quando o jogador escolhe a opção 4

    print('O que você deseja fazer?? Digite 1 para atacar e 2 para fugir')

    # Interação com o jogador para escolher o que ele quer fazer

    acao = str(input('Digite aqui sua ação: '))

    # Variável para saber a decisão do jogador

    if (acao == '1'):

        # Condição para caso o jogador faça a escolha de número 1

        print('Você tentou, mas o bravo guerreiro gigante de elbaf tem muita força, e você não resistiu')

        # Interação com o jogador para mostrar o que houve quando ele tomou a decisão de número 1

    elif (acao == '2'):

        # Condição para caso o jogador escolha a opção 2

        print('Você até tentou, porém ele além de gigante é rápido, e odiou sua covardia. Tive até pena de você!')

        # Interação com o jogador para mostrar o que houve quando ele tomou a decisão de número 2

else:

    # Condição caso o jogador digite um número diferente do informado

    print('Você precisa digitar um número entre 1 e 4, ou então não irá jogar!!')

    # Interação para mostrar que precisa escolher de 1 a 4, ou não joga