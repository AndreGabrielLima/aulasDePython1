nota1 = float(input('Digite aqui a primeira nota: '))

# Variável para pegar a notar 1 do aluno

nota2 = float(input('Digite aqui a segunda nota: '))

# Variável para pegar a notar 2 do aluno

nota3 = float(input('Digite aqui a terceira nota: '))

# Variável para pegar a notar 3 do aluno

media = (nota1 + nota2 + nota3) / 3

# Variável para fazer a média do aluno e ficar guardada

print('A média do aluno é : {}'.format(media))

# Interação para mostrar qual a média do aluno

if (media >= 7):

    # Condição caso a média do aluno seja maior ou igual a 7

    print('O aluno está aprovado!')

    # Interação para mostrar ao aluno que está aprovado

else:

    # Condição para caso a média não seja maior ou igual a 7

    print('O aluno está reprovado!')

    # Interação para mostrar ao aluno que está reprovado
