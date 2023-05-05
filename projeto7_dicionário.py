cod_alunoD = {}

# Variável do tipo dicionário para futuramente guardar informações

banco_notas = {}

# Variável do tipo dicionário para guardar as notas futuras

lista_notas = []

# Variáveç do tipo lista vazia para guardar as notas

cod_aluno = input('Digite um código númerico para o aluno: ')

# Variável do tipo string para guardar o código do aluno

nome_aluno = input('Digite o nome do aluno: ')

# Variável para guardar o nome do aluno

nota1 = float(input('Digite aqui a primeira nota: '))

# Variável para guardar nota 1 do aluno

nota2 = float(input('Digite aqui a segunda nota: '))

# Variável para guardar nota 2 do aluno

nota3 = float(input('Digite aqui a terceira nota: '))

# Variável para guardar nota 3 do aluno

lista_notas.append(nota1)

# Método append para adicionar a nota 1 na lista vazia

lista_notas.append(nota2)

# Método append para adicionar a nota 2 na lista vazia

lista_notas.append(nota3)

# Método append para adicionar a nota 3 na lista vazia

cod_alunoD[cod_aluno] = nome_aluno

# Utilizando o dicionário para guardar o nome do aluno juntamente com o seu código

banco_notas[cod_aluno] = lista_notas

# Utilizando o dicionário para guardar as notas do aluno no seu código

media = banco_notas.get(cod_aluno)

# Variável para buscar um valor de acordo com a chave do dicionário

print(media)

# Interação mostrando o valor da chave

media = sum(media) / 3

# Variável para calcular a média do aluno

print(media)

# Interação para mostrar a média do aluno

print('A média do aluno {} é: {}'.format(nome_aluno, media))

# Interação para mostrar nome do aluno de sua média

if (media >= 7):

    # Condição para caso a média do aluno seja maior ou igual a 7

    print('O aluno {} está aprovado'.format(nome_aluno))

    # Interação para dizer que o aluno está aprovado

else:

    # Condição para caso a média seja menor que 7

    print('O aluno {} está reprovado'.format(nome_aluno))

    # Interação para dizer que o aluno está reprovado