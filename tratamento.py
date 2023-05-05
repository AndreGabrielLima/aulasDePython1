v1 = [4, 8, 16, 32, 64, 128]
v2 = [2, 0, 4, 8, 0],

for i in range(len(v1)):
    try:
        div = v1[i]/v2[i]
        print('%d / %d = %d' %(v1[i], v2[i], div))
    except (ZeroDivisionError, IndexError):
        print('Zero não é divisível, as listas tem tamanhos diferentes')