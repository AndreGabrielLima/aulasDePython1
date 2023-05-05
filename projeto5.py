salario = float(input('Digite aqui seu sálario: '))

# Variável para armazenar o salário do usuário

emprestimo = float(input('Digite o valor do emprestimo que deseja: '))

# Variável para armazenar o valor de emprestimo que a pessoa quer

if (emprestimo <= salario * 0.5):

    # Condição para caso o emprestimo seja 50% menor ou igual ao salário

    print('Seu empréstimo foi aprovado')

    # Interação para avisar que o emprestimo foi aprovado

elif (emprestimo <= salario * 0.75):

    # Condição para caso o emprestimo seja 75% menor ou igual ao salário

    print('Seu empréstimo está em análise')

    # Interação para avisar que  o emprestimo esta em análise

else:

    # Condição caso não seja os dois valores anteriores

    print('O empréstimo foi negado')

    # Interação para mostrar que o emprestimo foi negado
