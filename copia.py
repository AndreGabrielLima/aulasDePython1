L = [6, 7, 8, 9, 5]
V = L[:]
Z = list(L)
L.append(4)
print(L, V, Z)

#FUNÇÃO IGUAL AO INSERT

V[0] = -100
Z[4] = -8
print(L, V, Z)

#FUNÇÃO IGUAL AO INSERT

i = [10, 20, 30]
soma = sum(i)
print(type(soma))
