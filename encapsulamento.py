class Pessoa():

    def __init__(self, nome, idade):

        self.__nome = nome
        self.__idade = idade

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def setNome(self, nome):
        self.__nome = nome

    def setIdade(self, idade):
        self.__idade = idade

    def imprimir(self):
        print('Me chamo {} e tenho {} anos'.format(self.getNome(),self.getIdade()))

pessoa = Pessoa('André', 18)
pessoa.imprimir()