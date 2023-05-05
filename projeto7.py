lista_notas = []

# Aqui tem uma váriavel do tipo lista vazia para ser adicionado a nota do aluno

nota1 = float(input('Digite aqui a primeira nota do aluno: '))

# Variável do tipo float para armazenar a primeira nota do aluno

nota2 = float(input('Digite aqui a segunda nota do aluno: '))

# Variável do tipo float para armazenar a segunda nota do aluno

nota3 = float(input('Digite aqui a terceira nota do aluno: '))

# Variável do tipo float para armazenar a terceira nota do aluno

lista_notas.append(nota1)

# Utilizando o método append para adicionar a variável 1 na variável lista

lista_notas.append(nota2)

# Utilizando o método append para adicionar a variável 2 na variável lista

lista_notas.append(nota3)

# Utilizando o método append para adicionar a variável 3 na variável lista

print(lista_notas)

# Interação mostrando as notas do aluno

media = sum(lista_notas) / 3

# Variável para calcular a média do aluno

print(media)

# Interação mostrando a média do aluno

if (media >= 7):

    # Condição caso a média do aluno seja maior ou igual a 7

    print('O aluno está aprovado!!')

    # Interação mostrando que o aluno passou de ano

else:

    # Condição para caso o aluno não tenha a média maior ou igual a 7

    print('O aluno está reprovado!')

    # Interação mostrando que o aluno não passou de ano