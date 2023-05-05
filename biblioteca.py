agenda = {123: 'sheeza', 456: 'carlos', 789: 'sara'}

def retorna_valor(chave):
    if chave in agenda:
        return agenda[chave]
    else:
        print('Valor não encontrado!')
