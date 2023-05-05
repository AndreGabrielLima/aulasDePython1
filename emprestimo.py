salario = float(input('Digite aqui seu salário: '))
emprestimo = float(input('Digite aqui o valor do emprestimo desejado: '))

if (emprestimo <= salario * 0.5):
    print('O emprestimo foi aprovado!')
elif (emprestimo <= salario * 0.75):
    print('O emprestimo está em analise!!')
else:
    print('O emprestimo não está aprovado!')
