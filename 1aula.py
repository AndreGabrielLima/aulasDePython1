#COMANDO PRINT É UMA FUNÇÃO PARA IMPRIMIR ALGO NA TELA
print('Bem vindo ao sistema Fuctura!')

#VARIÁVEL É UM MECANISMO DE ARMAZENAMENTO DE INFORMAÇÃO E SÓ PODE ARMAZENAR UMA INFORMAÇÃO POR VEZ#
x = '1'
y = '2'
print(x, y)

#A FUNÇÃO INPUT É UMA FUNÇÃO PARA PEGAR INFORMAÇÕES DO USUÁRIO
x = input('Digite um valor aqui: ')
y = input('Digite outro valor aqui ')
print('O valor que você digitou foi', x,'e', y)
print('O valor que você digitou foi: {} e {}'.format(x, y))

#LEMBRANDO QUE SE A GENTE QUISER DETERMINAR QUAL O TIPO DA INFORMAÇÃO TEMOS QUE DECLARAR ELA QUANDO ESTÁ SOLICITANDO AO USUÁRIO OU NO PROCESSAMENTO
x = int(input('Digite um valor aqui: '))
y = float(input('Digite outro valor aqui: '))
print('O valor que você digitou foi:', x, type(x), y, type(y))

#ISSO AQUI É UM COMENTÁRIO
'''isso aqui é um comentário'''
print('Aqui vai funcionar de boa!!')

#ABSTRAIR O PROBLEMA É IMPORTANTE PARA PODER ENTENDER O PASSO A PASSO DO QUE SE DEVE FAZER PARA CRIAR UMA SOLUÇÃO
entrada = 'Dados necessários para alimentar um programa'
processamento = 'Cálculo ou lógica utilizando a entrada'
saida = 'Resultado das operações feitas'
print('Entrada:', entrada)
print('Processamento:', processamento)
print('Saída:', saida)

