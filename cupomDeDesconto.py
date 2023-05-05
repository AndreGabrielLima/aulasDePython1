#ENTRADA:
cupom = str(input('Digite aqui seu cupom: '))
#PROCESSAMENTO
if (cupom == 'FUCTURA1' or cupom == 'FUCTURA2'):
#SAÍDA
    print('Você ganhou 15% de desconto!!')
elif (cupom == 'FUCTURA3'):
    print('Você ganhou 10% de desconto!!')
else:
    print('Esse cupom não é válido!')
