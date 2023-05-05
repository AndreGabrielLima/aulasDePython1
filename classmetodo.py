class Fuctura():

    def __init__(self, nome, matricula, telefone, email):
        self.aluno = nome
        self.matriculas = matricula
        self.telefone = telefone
        self.email = email

    def apresentação(self):
        print('Bem vindo a Fuctura {} !'.format(self.aluno))

nome = input('Digite seu nome: ')
matricula = input('Digite a matricula do aluno: ')
telefone = input('Digite seu telefone: ')
email = input('Digite seu email: ')

aluno1 = Fuctura(None, None, None, None)
aluno1.apresentação()
nome = input('Digite o nome do aluno: ')
matricula = input('Digite a matricula do aluno: ')
telefone = input('Digite o telefone do aluno: ')
email = input('Digite seu email: ')

aluno2 = Fuctura(None, None, None, None)
aluno2.apresentação()