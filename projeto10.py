cod_alunoD = {}

# Dicionário vazia para adicionar chaves e valores mais tarde

banco_notas = {}

# Dicionário para as notas adicionadas mais tarde

lista_notas = []

# Lista vazia para adicionar as notas

banco_medias = {}

# Dicionário para guardar as médias dos alunos

while True:

# Laço de repetição até receber um break

    print('0 - CADASTRAR ALUNO \n1 - MOSTRAR CADASTRO \n2 - MOSTRAR NOTA')

    # Interação com o usuário para mostrar se ele quer cadastrar, mostrar cadastro, ou notas dos alunos

    conf = int(input('Digite sua opção: '))

    # Váriavel para receber a opção do usuário

    if (conf == 0):

        # Condição para caso o usuário escolha a opção 0

        cod_aluno = input('Digite um código numérico para o aluno: ')

        # Variável para receber o código do aluno

        nome_aluno = input('Digite o nome do aluno: ')

        # Variável para receber o nome do aluno

        nota1 = float(input('Digite a primeira nota do aluno: '))

        # Variável para receber a primeira nota do aluno

        nota2 = float(input('Digite a segunda nota do aluno: '))

        # Variável para receber a segunda nota do aluno

        nota3 = float(input('Digite a terceira nota do aluno: '))

        # Variável para receber a terceira nota do aluno

        media = (nota1 + nota2 + nota3) / 3

        # Variável para fazer a média dos alunos

        lista_notas.append(nota1)

        # Adicionando a nota 1 na lista vazia

        lista_notas.append(nota2)

        # Adicionando a nota 2 na lista vazia

        lista_notas.append(nota3)

        # Adicionando a nota 3 na lista vazia

        cod_alunoD[cod_aluno] = nome_aluno

        # Colocando as variáveis no dicionário para ser usado com chave e valores

        banco_notas[cod_aluno] = lista_notas

        # Colocando a variável código do aluno para ser a chave dos valores

        banco_medias[cod_aluno] = media

        # Colocando a variável código do aluno para ser a chave das médias

        lista_notas = []

        # Esvaziando a lista para que no próximo cadastro ela não esteja com as notas dos cadastros antigos

        print('O aluno cadastrado foi {} e suas notas estão no sistema.'.format(nome_aluno))

        # Interação para informar que o aluno foi cadastrado no sistema

    elif (conf == 1):

        # Condição para caso a opção seja 1

        print('Lista de alunos cadastrados: ')

        # Interação para mostrar a lista de candidatos

        print('-'*100)

        # Apenas para decorar o terminal

        print(cod_alunoD)

        # Mostrando os alunos através dos códigos e nomes

    elif (conf == 2):

        # Condição para caso a escolha seja 2

        Cod_Aluno = input('Digite o cod de cadastro do aluno: ')

        # Variável para receber o código do aluno

        nome_aluno = cod_alunoD.get(Cod_Aluno)

        # Variável para tirar a chave do dicionário e ficar apenas com o valor

        notas = banco_notas.get(Cod_Aluno)

        # Variável para tirar a chave do dicionário e ficar apenas com as notas

        media = banco_medias.get(Cod_Aluno)

        # Variável para tirar a chave do dicionário e ficar apenas com as notas

        print('As notas do aluno {} são: {}'.format(nome_aluno, notas))

        # Interação para mostrar o nome e notas dos alunos

        print('E sua média é: {}'.format(media))

        # Interação para mostrar a média do aluno

    print('')

    # Apenas para dar espaço

    print('='*100)

    # Apenas para decorar o terminal

    print('0 para CONTINUAR | 1 para SAIR')

    # Interação para mostrar se o usuário quer continuar ou sair

    if int(input()) == 1:

        # Condição para caso a escolha seja 1 (sair)

        break

        # Utilizando o break para quebrar o lçao de repetição e acabar com o processo