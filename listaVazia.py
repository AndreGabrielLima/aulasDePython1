a = []
a.append(1)
a.append('a')
a.append('b')
a.append('c')

print(a)

a.insert(2, 3)
print(a)

a.remove('a')
print(a)

indice = a.index('b')
print(indice)

del(a[indice])
print(a)

a.reverse()
print(a)
