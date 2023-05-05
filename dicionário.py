dic = {}
print(type(dic))
dic_pernambuco = {'Sport': 41, 'Santa Cruz': 29, 'Nautico': 21}
print(dic_pernambuco)
#NO DICIONÁRIO É COM CHAVE E VALOR  chave:valor

#ADICIONANDO ELEMENTO NO DICIONÁRIO

dic_pernambuco ['Salgueiro'] = 1
print(dic_pernambuco)

#Buscando valor com base na chave
qnt_titulos = dic_pernambuco.get('Sport')
print('O sport tem {} títulos'.format(qnt_titulos))

#Remover elemento com base na chave
del dic_pernambuco['Salgueiro']
print(dic_pernambuco)

#Remove a chave e retorna seu valor
valor = dic_pernambuco.pop('Nautico')
print('O valor retornado da chave é {}'.format(valor))

#Verificar se uma chave existe no dicionário
print('Santa Cruz' in dic_pernambuco)

#Pegar todas as chaves do dicionário
print(dic_pernambuco.keys())

print(dic_pernambuco.values())

dic_paulista = {'Corinthias' : 29, 'Santos' : 22, 'Palmeira' : 22}
print(dic_paulista.popitem())
dic_pernambuco.update(dic_paulista)
print(dic_pernambuco)

#Transformando em lista
print(list(dic_pernambuco))
print(list(dic_pernambuco.values()))

