try:
    vetor = list(range(4))
    print('Antes da execução!')
    print(vetor[4])
    print('Esse texto não será impresso!')

except IndexError as error:
    print('A quantidade de elementos solicitada é maior que o tamanho da lista')