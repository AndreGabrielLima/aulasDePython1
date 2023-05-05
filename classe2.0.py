# SOBRECARGA DE CLASSE

class fuctura1():

    def __init__(self, nome, matricula, telefone, email):
        self.aluno = nome
        self.matriculas = matricula
        self.telefone = telefone
        self.email = email

    def apresentação(self):
        print('Bem vindo a Fuctura {} !'.format(self.aluno))

class fuctura2():

    def __init__(self, nome, matricula, telefone, email):
        self.aluno = nome
        self.matriculas = matricula
        self.telefone = telefone
        self.email = email

    def apresentação(self):
        print('Bem vindo a filial 2 da Fuctura {} !'.format(self.aluno))

nome = input('Digite o nome do aluno: ')
matricula = input('Digite a matricula do aluno: ')
telefone = input('Digite o telefone do aluno: ')
email = input('Digite o email do aluno: ')

aluno1 = fuctura1(nome, matricula, telefone, email)
aluno1.apresentação()

nome = input('Digite o nome do aluno: ')
matricula = input('Digite a matricula do aluno: ')
telefone = input('Digite o telefone do aluno: ')
email = input('Digite o email do aluno: ')

aluno2 = fuctura2(nome, matricula, telefone, email)
aluno2.apresentação()